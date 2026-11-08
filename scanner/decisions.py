"""Decision log: record every recommendation, score it against the benchmark after 5 and 20 business days.

    python -m scanner.decisions append --allocation reports/.../allocation.json
    python -m scanner.decisions score            # scores matured decisions into state/scorecard.csv
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import numpy as np
import pandas as pd

from . import config, data

LOG = config.STATE_DIR / "decisions.jsonl"
SCORECARD = config.STATE_DIR / "scorecard.csv"


def append(allocation_path: Path) -> int:
    a = json.loads(Path(allocation_path).read_text(encoding="utf-8"))
    research_dir = Path(allocation_path).parent / "research"
    n = 0
    with open(LOG, "a", encoding="utf-8") as f:
        for p in a["positions"]:
            card_path = research_dir / f"{p['ticker']}.json"
            card = json.loads(card_path.read_text()) if card_path.exists() else {}
            rec = {
                "id": f"{a['as_of']}:{a['session']}:{p['ticker']}",
                "date": a["as_of"], "session": a["session"], "exchange": a["exchange"],
                "ticker": p["ticker"], "status": p["status"], "weight": p["weight"],
                "price": p.get("price"), "stop": p.get("stop"), "target": p.get("target"),
                "rating": card.get("rating", p.get("rating")),
                "confidence": card.get("confidence"),
                "expected_return": card.get("expected_return"),
                "horizon_days": card.get("horizon_days"),
                "thesis": card.get("thesis"),
            }
            f.write(json.dumps(config.clean(rec), ensure_ascii=False) + "\n")
            n += 1
        for v in a.get("vetoed", []):
            f.write(json.dumps({"id": f"{a['as_of']}:{a['session']}:{v['ticker']}:veto",
                                "date": a["as_of"], "session": a["session"],
                                "ticker": v["ticker"], "status": "vetoed",
                                "reason": v.get("reason")}, ensure_ascii=False) + "\n")
    return n


def _fwd(px: pd.DataFrame, t: str, d0: str, n: int) -> float | None:
    g = px[px["symbol"] == t].sort_values("date").reset_index(drop=True)
    idx = g.index[g["date"] >= pd.Timestamp(d0)]
    if len(idx) == 0:
        return None
    i0 = idx[0]
    if i0 + n >= len(g):
        return None
    return float(g["close"].iloc[i0 + n] / g["close"].iloc[i0] - 1)


def score(benchmark: str = "QQQ") -> pd.DataFrame:
    if not LOG.exists() or LOG.stat().st_size == 0:
        return pd.DataFrame()
    recs = [json.loads(ln) for ln in LOG.read_text(encoding="utf-8").splitlines() if ln.strip()]
    df = pd.DataFrame(recs)
    horizons = config.portfolio_config().get("score_horizons", [5, 20])
    px = data.history(sorted(set(df["ticker"]) | {benchmark}), days=400)
    for n in horizons:
        df[f"ret_{n}"] = [_fwd(px, r.ticker, r.date, n) for r in df.itertuples()]
        df[f"bench_{n}"] = [_fwd(px, benchmark, r.date, n) for r in df.itertuples()]
        df[f"excess_{n}"] = df[f"ret_{n}"] - df[f"bench_{n}"]
    df.to_csv(SCORECARD, index=False)
    return df


def summary(df: pd.DataFrame) -> dict:
    if df.empty:
        return {"decisions": 0}
    out = {"decisions": int(len(df))}
    for col in [c for c in df.columns if c.startswith("excess_")]:
        s = df[df["status"] != "vetoed"][col].dropna()
        v = df[df["status"] == "vetoed"][col].dropna()
        out[col] = {"n": int(len(s)), "mean": float(s.mean()) if len(s) else None,
                    "hit_rate": float((s > 0).mean()) if len(s) else None,
                    "vetoed_mean": float(v.mean()) if len(v) else None}
    return out


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    ap = sub.add_parser("append")
    ap.add_argument("--allocation", required=True)
    sub.add_parser("score")
    a = p.parse_args(argv)
    if a.cmd == "append":
        print(json.dumps({"appended": append(Path(a.allocation))}))
    else:
        print(json.dumps(summary(score()), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
