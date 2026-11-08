"""Position sizing engine (stage 6). Weights come from this module, never from an LLM.

    python -m scanner.sizing --run-dir reports/nasdaq/2026-11-09/premarket

All amounts are expressed against a notional portfolio (default 1,000 units, see
config/portfolio.yaml). No currency or real account size is stored in the repo.

Inputs (inside run-dir):
    research/<TICKER>.json   research-manager cards (rating, confidence, entry, stop, target)
    regime_view.json         macro-regime decision {"regime": "risk-on|neutral|risk-off"}
    risk_review.json         (optional) risk-officer vetoes and reductions
    ohlcv.pkl                price history (correlation, volatility, last price)
    packets/<TICKER>.json    earnings date and indicators
Output:
    proposals.json           engine weights, rejected candidates and reasons
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from . import config, factors

RESEARCH_FIELDS = ["ticker", "rating", "confidence", "stop", "target"]


def _bdays_until(d: str | None, today: date) -> int | None:
    if not d:
        return None
    try:
        target = pd.Timestamp(str(d)[:10]).date()
    except Exception:  # noqa: BLE001
        return None
    if target < today:
        return None
    return int(np.busday_count(today, target))


def _last_close(px: pd.DataFrame, t: str) -> float | None:
    g = px[px["symbol"] == t]
    return float(g.sort_values("date")["close"].iloc[-1]) if not g.empty else None


def _load_cards(run_dir: Path) -> list[dict]:
    cards = []
    for p in sorted((run_dir / "research").glob("*.json")):
        c = json.loads(p.read_text(encoding="utf-8"))
        c["_missing"] = [f for f in RESEARCH_FIELDS if c.get(f) in (None, "")]
        cards.append(c)
    return cards


def _packet(run_dir: Path, t: str) -> dict:
    p = run_dir / "packets" / f"{t}.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def portfolio_value(state: dict, px: pd.DataFrame) -> tuple[float, list[dict]]:
    """Mark the notional portfolio to market. Position value = units * price / entry_price."""
    held = []
    for p in state.get("positions", []):
        price = _last_close(px, p["ticker"]) or p["entry_price"]
        value = p["units"] * price / p["entry_price"]
        held.append({**p, "price": price, "value": value})
    total = state.get("cash_units", 0) + sum(h["value"] for h in held)
    return total, held


def size(run_dir: Path, today: date | None = None) -> dict:
    today = today or date.today()
    rk, pc = config.risk(), config.portfolio_config()
    state = config.portfolio_state()
    px = pd.read_pickle(run_dir / "ohlcv.pkl") if (run_dir / "ohlcv.pkl").exists() \
        else pd.DataFrame(columns=["symbol", "date", "close"])
    regime_path = run_dir / "regime_view.json"
    regime = json.loads(regime_path.read_text())["regime"] if regime_path.exists() else "neutral"
    review_path = run_dir / "risk_review.json"
    review = json.loads(review_path.read_text()) if review_path.exists() else {}
    vetoes = {v["ticker"]: v.get("reason", "") for v in review.get("vetoes", [])}
    reductions = {r["ticker"]: r for r in review.get("reductions", [])}

    # --- current portfolio ---
    value, held = portfolio_value(state, px)
    if value <= 0:
        value = float(pc["notional_base"])
    peak = max(state.get("peak_value", value), value)
    drawdown = 1 - value / peak
    dd_mult = 0.0 if drawdown >= rk["drawdown_breaker"] else 1.0
    regime_mult = rk["regime_mult"].get(regime, 0.7)

    positions, rejected = [], []
    for h in held:
        w = h["value"] / value
        flags = []
        if h.get("stop") and h["price"] <= h["stop"]:
            flags.append("stop hit: exit suggested")
        if drawdown >= rk["drawdown_breaker"]:
            w_target = w * rk["drawdown_gross_mult"]
            flags.append("drawdown breaker: position halved")
        else:
            w_target = 0.0 if flags else w
        positions.append({"ticker": h["ticker"], "status": "held", "sector": h.get("sector"),
                          "price": h["price"], "current_weight": w, "engine_weight": w_target,
                          "stop": h.get("stop"), "target": h.get("target"), "flags": flags})
    held_tickers = {h["ticker"] for h in held}

    # --- new candidates ---
    new = []
    for c in _load_cards(run_dir):
        t = c.get("ticker")
        if t in held_tickers:
            continue

        def rej(reason):
            rejected.append({"ticker": t, "reason": reason})
        if c["_missing"]:
            rej(f"missing fields: {', '.join(c['_missing'])} (REVIEW)")
            continue
        conv = rk["conviction_mult"].get(c["rating"], 0.0)
        if conv <= 0:
            rej(f"rating {c['rating']}: no new buy")
            continue
        if t in vetoes:
            rej(f"risk-officer veto: {vetoes[t]}")
            continue
        pkt = _packet(run_dir, t)
        ind = pkt.get("technical", {}).get("indicators", {})
        price = float(c.get("entry") or _last_close(px, t) or ind.get("close") or 0)
        if price <= 0:
            rej("no price")
            continue
        stop = float(c["stop"])
        if not stop or stop >= price:
            atr_v = ind.get("atr")
            if not atr_v:
                rej("no valid stop")
                continue
            stop = price - rk["atr_stop_mult"] * atr_v
        stop_pct = (price - stop) / price
        target = float(c["target"])
        rr = (target - price) / (price - stop)
        if rr < rk["min_reward_risk"]:
            rej(f"reward/risk {rr:.2f} < {rk['min_reward_risk']}")
            continue
        p = min(max(float(c["confidence"]), 0.0), 1.0)
        kelly = p - (1 - p) / rr
        if kelly <= 0:
            rej(f"negative Kelly (confidence {p:.2f}, reward/risk {rr:.2f})")
            continue
        bd = _bdays_until(c.get("earnings_date") or pkt.get("profile", {}).get("earnings_date"), today)
        if bd is not None and bd <= rk["earnings_blackout_days"]:
            rej(f"earnings in {bd} business days")
            continue
        flags = []
        w_risk = rk["risk_per_trade"] / stop_pct
        w_kelly = kelly * rk["kelly_fraction"]
        w = min(w_risk, w_kelly, rk["max_position"]) * conv * regime_mult * dd_mult
        binding = min((("risk", w_risk), ("kelly", w_kelly), ("max", rk["max_position"])),
                      key=lambda x: x[1])[0]
        if t in reductions:
            f = float(reductions[t].get("factor", 1.0))
            w *= f
            flags.append(f"risk-officer reduction x{f}: {reductions[t].get('reason', '')}")
        if dd_mult == 0:
            flags.append("drawdown breaker: no new buys")
        new.append({"ticker": t, "status": "new",
                    "sector": c.get("sector") or pkt.get("profile", {}).get("sector"),
                    "price": price, "stop": round(stop, 4), "target": target, "rr": round(rr, 2),
                    "rating": c["rating"], "confidence": p, "kelly": round(kelly, 4),
                    "stop_pct": round(stop_pct, 4), "binding": binding,
                    "engine_weight": w, "priority": kelly * conv, "flags": flags})

    # position count
    new.sort(key=lambda x: x["priority"], reverse=True)
    slots = max(rk["max_positions"] - sum(1 for h in positions if h["engine_weight"] > 0), 0)
    for x in new[slots:]:
        rejected.append({"ticker": x["ticker"], "reason": "max positions reached"})
    new = [x for x in new[:slots] if x["engine_weight"] > 0]

    # correlation
    tick = [x["ticker"] for x in new] + [h["ticker"] for h in positions]
    if len(tick) > 1 and not px.empty:
        corr = factors.correlation(px, tick, rk["corr_lookback"])
        for i, a in enumerate(new):
            for b in new[:i] + [h for h in positions if h["engine_weight"] > 0]:
                if a["ticker"] in corr and b["ticker"] in corr and \
                        corr.loc[a["ticker"], b["ticker"]] > rk["corr_threshold"]:
                    a["engine_weight"] /= 2
                    a["flags"].append(f"correlation with {b['ticker']} "
                                      f"{corr.loc[a['ticker'], b['ticker']]:.2f}: halved")
                    break

    # sector cap (only new positions are scaled)
    sectors = {}
    for x in positions + new:
        sectors.setdefault(x.get("sector") or "Unknown", []).append(x)
    for sec_name, items in sectors.items():
        total = sum(x["engine_weight"] for x in items)
        if total > rk["max_sector"]:
            held_w = sum(x["engine_weight"] for x in items if x["status"] == "held")
            new_w = total - held_w
            room = max(rk["max_sector"] - held_w, 0)
            f = room / new_w if new_w else 0
            for x in items:
                if x["status"] == "new":
                    x["engine_weight"] *= f
                    x["flags"].append(f"sector cap ({sec_name}) x{f:.2f}")

    # cash buffer
    invested = sum(x["engine_weight"] for x in positions + new)
    cap = 1 - rk["min_cash"]
    if invested > cap:
        held_w = sum(x["engine_weight"] for x in positions)
        new_w = invested - held_w
        f = max(cap - held_w, 0) / new_w if new_w else 0
        for x in new:
            x["engine_weight"] *= f
            x["flags"].append(f"cash buffer x{f:.2f}")

    # portfolio volatility target
    port_vol = None
    live = [x for x in positions + new if x["engine_weight"] > 0]
    if live and not px.empty:
        cov = factors.covariance(px, [x["ticker"] for x in live], rk["corr_lookback"])
        names = [x["ticker"] for x in live if x["ticker"] in cov.index]
        if names:
            def vol(ws):
                v = np.array([ws[n] for n in names])
                return float(math.sqrt(max(v @ cov.loc[names, names].values @ v, 0)))
            new_names = {x["ticker"] for x in new}
            ws = {x["ticker"]: x["engine_weight"] for x in live}
            port_vol = vol(ws)
            if port_vol > rk["target_vol"]:
                lo, hi = 0.0, 1.0
                for _ in range(30):
                    mid = (lo + hi) / 2
                    trial = {k: (v * mid if k in new_names else v) for k, v in ws.items()}
                    lo, hi = (mid, hi) if vol(trial) <= rk["target_vol"] else (lo, mid)
                for x in new:
                    x["engine_weight"] *= lo
                    x["flags"].append(f"volatility target x{lo:.2f}")
                port_vol = vol({x["ticker"]: x["engine_weight"] for x in live})

    # notional amounts
    for x in new:
        x["engine_weight"] = round(x["engine_weight"], 4)
        x["amount_units"] = round(x["engine_weight"] * value, 2)
    new = [x for x in new if x["engine_weight"] > 0]
    for x in positions:
        x["engine_weight"] = round(x["engine_weight"], 4)
        x["amount_units"] = round(x["engine_weight"] * value, 2)

    out_pos = positions + new
    cash_w = round(1 - sum(x["engine_weight"] for x in out_pos), 4)
    result = {
        "as_of": today.isoformat(), "notional_base": pc["notional_base"],
        "portfolio_value_units": round(value, 2), "peak_value_units": round(peak, 2),
        "drawdown": round(drawdown, 4), "regime": regime, "regime_mult": regime_mult,
        "risk_per_trade": rk["risk_per_trade"], "portfolio_vol": port_vol,
        "positions": out_pos, "cash_weight": cash_w, "rejected": rejected,
    }
    config.write_json(run_dir / "proposals.json", result)
    return result


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--run-dir", required=True)
    a = p.parse_args(argv)
    r = size(Path(a.run_dir))
    print(json.dumps({"positions": [(x["ticker"], x["engine_weight"]) for x in r["positions"]],
                      "cash_weight": r["cash_weight"], "rejected": len(r["rejected"])}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
