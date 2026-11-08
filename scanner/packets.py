"""Data packets for finalists (the only source agents read).

    python -m scanner.packets --run-dir reports/nasdaq/2026-11-09/premarket --tickers NVDA,AMD
    python -m scanner.packets --run-dir ... --positions     # for portfolio holdings

Each packet packets/<TICKER>.json holds technicals (last 60 days + indicators + levels),
fundamentals (yfinance profile + SEC EDGAR quarters), news, SEC filings and the earnings date.
Agents never invent numbers; every number comes from these packets.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path

import pandas as pd

from . import config, data, factors, sec


def technical(g: pd.DataFrame, bench_ret63: float | None, atr_n: int) -> dict:
    g = g.sort_values("date")
    f = factors.per_symbol(g, bench_ret63, atr_n) or {}
    tail = g.tail(60)
    weekly = g.set_index("date")["close"].resample("W-FRI").last().tail(26)
    return {
        "indicators": {k: (round(v, 4) if isinstance(v, float) else v) for k, v in f.items()},
        "levels": {
            "swing_low_10": float(g["low"].tail(10).min()),
            "swing_low_20": float(g["low"].tail(20).min()),
            "swing_high_20": float(g["high"].tail(20).max()),
            "high_52w": float(g["high"].tail(252).max()),
            "low_52w": float(g["low"].tail(252).min()),
        },
        "last_60_days": [
            {"d": r.date.date().isoformat(), "o": round(r.open, 2), "h": round(r.high, 2),
             "l": round(r.low, 2), "c": round(r.close, 2), "v": int(r.volume)}
            for r in tail.itertuples()
        ],
        "weekly_closes_26": [round(float(x), 2) for x in weekly.values],
    }


def build(run_dir: Path, tickers: list[str], exchange_code: str = "nasdaq",
          intraday: bool = False) -> list[str]:
    ex = config.exchange(exchange_code)
    rk = config.risk()
    pkl = run_dir / "ohlcv.pkl"
    px = pd.read_pickle(pkl) if pkl.exists() else pd.DataFrame(columns=data.COLS)
    need = [t for t in tickers + [ex["benchmark"]] if t not in set(px["symbol"])]
    if need:
        px = pd.concat([px, data.history(need, days=ex["filters"]["history_days"],
                                         suffix=ex["symbol_suffix"])])
        px.to_pickle(pkl)
    b = px[px["symbol"] == ex["benchmark"]].sort_values("date")["close"]
    b63 = float(b.iloc[-1] / b.iloc[-64] - 1) if len(b) > 64 else None

    live = data.last_prices(tickers, ex["symbol_suffix"]) if intraday else {}
    written = []
    for t in tickers:
        g = px[px["symbol"] == t]
        if g.empty:
            continue
        pkt = {
            "ticker": t, "exchange": ex["code"],
            "as_of": datetime.now(timezone.utc).isoformat(),
            "data_note": "In the pre-market session the last price is the previous close; in the pre-close session it is ~15 min delayed.",
            "technical": technical(g, b63, rk["atr_period"]),
            "profile": data.info(t, ex["symbol_suffix"]),
            "sec_fundamentals": sec.fundamentals(t) if ex["code"] in ("NASDAQ", "NYSE") else None,
            "sec_filings_10d": sec.recent_filings(t) if ex["code"] in ("NASDAQ", "NYSE") else [],
            "news_7d": data.news(t, ex["symbol_suffix"]),
        }
        if intraday:
            prev = float(g.sort_values("date")["close"].iloc[-1])
            pkt["intraday"] = {"last": live.get(t), "prev_close_in_history": prev,
                               "note": "about 15 min delayed"}
        path = run_dir / "packets" / f"{t}.json"
        config.write_json(path, pkt)
        written.append(str(path))
    return written


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--run-dir", required=True)
    p.add_argument("--tickers", default="")
    p.add_argument("--positions", action="store_true")
    p.add_argument("--exchange", default="nasdaq")
    p.add_argument("--intraday", action="store_true", help="add the intraday last price (pre-close session)")
    a = p.parse_args(argv)
    tickers = [t.strip().upper() for t in a.tickers.split(",") if t.strip()]
    if a.positions:
        tickers += [p["ticker"] for p in config.portfolio_state().get("positions", [])]
    tickers = list(dict.fromkeys(tickers))
    print(json.dumps({"packets": build(Path(a.run_dir), tickers, a.exchange, a.intraday)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
