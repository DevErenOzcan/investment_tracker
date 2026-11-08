"""allocation.json validation: schema + risk limits + consistency with the engine.

    python -m scanner.validate reports/nasdaq/2026-11-09/premarket/allocation.json
    python -m scanner.validate --latest [--max-age-min 240]

Exit code 0 = valid, 2 = errors (messages on stderr).
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from . import config

REQUIRED_TOP = ["as_of", "session", "exchange", "regime", "positions", "cash_weight"]
REQUIRED_POS = ["ticker", "status", "weight", "engine_weight", "sector", "rationale"]


def check(path: Path) -> list[str]:
    errs: list[str] = []
    try:
        a = json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"unreadable: {e}"]
    rk = config.risk()
    for k in REQUIRED_TOP:
        if k not in a:
            errs.append(f"missing field: {k}")
    if errs:
        return errs
    prop_path = Path(path).parent / "proposals.json"
    engine = {}
    if prop_path.exists():
        engine = {p["ticker"]: p for p in json.loads(prop_path.read_text())["positions"]}
    else:
        errs.append("proposals.json missing: weights did not go through the engine")

    total, sectors, n_live = 0.0, {}, 0
    lim = rk["pm_adjust_limit"]
    for p in a["positions"]:
        for k in REQUIRED_POS:
            if k not in p:
                errs.append(f"{p.get('ticker', '?')}: missing field {k}")
        w, ew = float(p.get("weight", 0)), float(p.get("engine_weight", 0))
        t = p.get("ticker")
        if w < 0 and rk.get("long_only", True):
            errs.append(f"{t}: negative weight (long only)")
        if w > rk["max_position"] + 1e-6:
            errs.append(f"{t}: weight {w:.4f} > single-position cap {rk['max_position']}")
        if engine:
            if t not in engine:
                if w > 0:
                    errs.append(f"{t}: position not proposed by the engine")
            else:
                ew_engine = float(engine[t]["engine_weight"])
                if abs(ew - ew_engine) > 1e-4:
                    errs.append(f"{t}: engine_weight {ew} does not match the engine ({ew_engine})")
                if p.get("status") == "new" and w > ew_engine * (1 + lim) + 1e-6:
                    errs.append(f"{t}: weight {w:.4f} exceeds the engine's +{int(lim * 100)}% limit "
                                f"(engine {ew_engine:.4f})")
                if p.get("status") == "new" and ew_engine == 0 and w > 0:
                    errs.append(f"{t}: engine proposed 0")
        total += w
        if w > 0:
            n_live += 1
            s = p.get("sector") or "Unknown"
            sectors[s] = sectors.get(s, 0) + w
    if n_live > rk["max_positions"]:
        errs.append(f"position count {n_live} > {rk['max_positions']}")
    for s, w in sectors.items():
        if w > rk["max_sector"] + 1e-6:
            errs.append(f"sector {s}: {w:.4f} > {rk['max_sector']}")
    cash = float(a["cash_weight"])
    if abs(total + cash - 1) > 0.01:
        errs.append(f"weights + cash = {total + cash:.4f}, must be 1")
    if cash < rk["min_cash"] - 1e-6:
        errs.append(f"cash {cash:.4f} < minimum {rk['min_cash']}")
    return errs


def latest(max_age_min: int | None = None) -> Path | None:
    files = sorted(config.REPORTS_DIR.glob("*/*/*/allocation.json"), key=lambda p: p.stat().st_mtime)
    if not files:
        return None
    f = files[-1]
    if max_age_min is not None and time.time() - f.stat().st_mtime > max_age_min * 60:
        return None
    return f


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("path", nargs="?")
    p.add_argument("--latest", action="store_true")
    p.add_argument("--max-age-min", type=int, default=None)
    a = p.parse_args(argv)
    path = Path(a.path) if a.path else latest(a.max_age_min)
    if path is None:
        print("no allocation.json to validate")
        return 0
    errs = check(path)
    if errs:
        print(f"{path}: {len(errs)} error(s)", file=sys.stderr)
        for e in errs:
            print(f"- {e}", file=sys.stderr)
        return 2
    print(f"{path}: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
