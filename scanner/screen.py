"""Screening funnel (stages 1-3): universe -> liquidity filter -> factor score -> top N.

    python -m scanner.screen --session premarket [--exchange nasdaq] [--limit 0]

Outputs (reports/<exchange>/<date>/<session>/):
    screen.csv        factors and score for every stock that passed the filters
    candidates.json   top N candidates for triage (with sector, market cap, earnings date)
    regime.json       index / VIX / rates / sector data for the macro-regime agent
    ohlcv.pkl         price history for later steps (packets, correlation)
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timezone

import numpy as np
import pandas as pd

from . import config, data, factors, universe

log = logging.getLogger("screen")


def liquidity_filter(f: pd.DataFrame, flt: dict) -> pd.DataFrame:
    return f[(f["close"] >= flt["min_price"]) & (f["dollar_volume_20"] >= flt["min_dollar_volume"])]


def regime_snapshot(ex: dict, days: int) -> dict:
    rs = ex["regime_symbols"]
    syms = rs["index"] + rs["sectors"] + [rs["volatility"], rs["rates"]]
    px = data.history(syms, days=days)
    out = {"as_of": datetime.now(timezone.utc).isoformat(), "series": {}}
    for s, g in px.groupby("symbol"):
        c = g.sort_values("date")["close"]
        if len(c) < 60:
            continue
        last = float(c.iloc[-1])
        out["series"][s] = {
            "last": round(last, 3),
            "ret_5": round(float(last / c.iloc[-6] - 1), 4),
            "ret_21": round(float(last / c.iloc[-22] - 1), 4),
            "ret_63": round(float(last / c.iloc[-64] - 1), 4) if len(c) > 64 else None,
            "above_sma50": bool(last > c.tail(50).mean()),
            "above_sma200": bool(last > c.tail(200).mean()) if len(c) >= 200 else None,
            "pct_rank_1y": round(float((c.tail(252) < last).mean()), 3),
        }
    return out


def run(session: str, exchange_code: str = "nasdaq", limit: int = 0) -> dict:
    ex = config.exchange(exchange_code)
    flt, scr = ex["filters"], ex["screen"]
    out_dir = config.run_dir(session, exchange_code=exchange_code)

    uni = universe.load(exchange_code)
    symbols = uni["symbol"].tolist()
    if limit:
        symbols = symbols[:limit]
    log.info("universe: %d symbols", len(symbols))

    px = data.history(symbols + [ex["benchmark"]], days=flt["history_days"], suffix=ex["symbol_suffix"])
    px.to_pickle(out_dir / "ohlcv.pkl")
    f = factors.compute(px, ex["benchmark"])
    f = f[f["symbol"] != ex["benchmark"]]
    n_hist = len(f)
    f = liquidity_filter(f, flt)
    n_liq = len(f)
    f = factors.score(f)
    f = f.merge(uni, on="symbol", how="left")

    pool = f.head(scr["info_pool"])["symbol"].tolist()
    with ThreadPoolExecutor(max_workers=8) as tp:
        infos = list(tp.map(lambda s: data.info(s, ex["symbol_suffix"]), pool))
    info_df = pd.DataFrame(infos)
    f = f.merge(info_df, on="symbol", how="left")
    keep = f["symbol"].isin(pool) & (f["marketCap"].fillna(0) >= flt["min_market_cap"])
    cands = f[keep].head(scr["top_n"])

    f.to_csv(out_dir / "screen.csv", index=False)
    cols = ["symbol", "name", "sector", "industry", "marketCap", "close", "score", "ret_5",
            "ret_21", "ret_63", "rs_63", "trend", "rsi14", "atr_pct", "dist_high", "vol_ratio",
            "ext_20", "dollar_volume_20", "earnings_date", "forwardPE", "revenueGrowth"]
    recs = cands[[c for c in cols if c in cands.columns]].replace({np.nan: None}).to_dict("records")
    for r in recs:  # one-line headlines for triage
        r["headlines"] = [n["title"] for n in data.news(r["symbol"], ex["symbol_suffix"], max_items=3)]
    summary = {
        "exchange": ex["code"], "session": session, "date": date.today().isoformat(),
        "funnel": {"universe": len(symbols), "with_history": n_hist, "liquid": n_liq,
                   "info_pool": len(pool), "candidates": len(recs)},
        "candidates": recs,
    }
    config.write_json(out_dir / "candidates.json", summary)
    config.write_json(out_dir / "regime.json", regime_snapshot(ex, flt["history_days"]))
    return {"run_dir": str(out_dir), **summary["funnel"]}


def main(argv=None) -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    p = argparse.ArgumentParser()
    p.add_argument("--session", required=True, choices=["premarket", "preclose"])
    p.add_argument("--exchange", default="nasdaq")
    p.add_argument("--limit", type=int, default=0, help="truncate the universe for testing")
    p.add_argument("--regime-only", action="store_true", help="only write regime.json")
    a = p.parse_args(argv)
    if a.regime_only:
        ex = config.exchange(a.exchange)
        out_dir = config.run_dir(a.session, exchange_code=a.exchange)
        config.write_json(out_dir / "regime.json", regime_snapshot(ex, ex["filters"]["history_days"]))
        print(json.dumps({"run_dir": str(out_dir)}))
        return 0
    print(json.dumps(run(a.session, a.exchange, a.limit), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
