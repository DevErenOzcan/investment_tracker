"""Offline end-to-end smoke test: screen -> packets -> sizing -> validation."""
import json
from pathlib import Path

import pandas as pd

from scanner import config, data, packets, screen, sec, sizing, universe, validate
from tests.conftest import synthetic_ohlcv

SYMS = [f"S{i:02d}" for i in range(40)]


def _patch(monkeypatch):
    px = synthetic_ohlcv(SYMS + ["QQQ", "SPY", "IWM", "^VIX", "^TNX", "XLK", "XLC", "XLY", "XLV",
                                 "XLF", "XLI", "XLE", "XLP", "XLU", "XLB", "XLRE", "SMH"], seed=3)
    monkeypatch.setattr(universe, "load", lambda *a, **k: pd.DataFrame(
        {"symbol": SYMS, "name": SYMS, "market_category": "Q"}))
    monkeypatch.setattr(data, "history", lambda syms, **k: px[px["symbol"].isin(syms)].copy())
    monkeypatch.setattr(data, "info", lambda s, *a, **k: {
        "symbol": s, "sector": ["Technology", "Healthcare", "Industrials"][int(s[1:]) % 3],
        "marketCap": 5e9, "earnings_date": None})
    monkeypatch.setattr(data, "news", lambda *a, **k: [{"title": "headline"}])
    monkeypatch.setattr(sec, "fundamentals", lambda *a, **k: {"available": False})
    monkeypatch.setattr(sec, "recent_filings", lambda *a, **k: [])


def test_end_to_end(sandbox, monkeypatch):
    _patch(monkeypatch)
    res = screen.run("premarket")
    run = Path(res["run_dir"])
    assert res["candidates"] == 25
    cands = json.loads((run / "candidates.json").read_text())["candidates"]
    assert json.loads((run / "regime.json").read_text())["series"]["QQQ"]
    finalists = [c["symbol"] for c in cands[:6]]
    packets.build(run, finalists)
    (run / "research").mkdir()
    for t in finalists:
        pk = json.loads((run / "packets" / f"{t}.json").read_text())
        close = pk["technical"]["indicators"]["close"]
        atr = pk["technical"]["indicators"]["atr"]
        (run / "research" / f"{t}.json").write_text(json.dumps({
            "ticker": t, "rating": "Buy", "confidence": 0.55, "entry": close,
            "stop": close - 2 * atr, "target": close + 5 * atr,
            "sector": pk["profile"]["sector"]}))
    (run / "regime_view.json").write_text(json.dumps({"regime": "neutral"}))
    r = sizing.size(run)
    assert r["positions"], r["rejected"]
    assert r["cash_weight"] >= 0.10
    pos = [{"ticker": p["ticker"], "status": p["status"], "sector": p["sector"],
            "weight": p["engine_weight"], "engine_weight": p["engine_weight"], "rationale": "x"}
           for p in r["positions"]]
    (run / "allocation.json").write_text(json.dumps({
        "as_of": "2026-11-09", "session": "premarket", "exchange": "NASDAQ",
        "regime": r["regime"], "positions": pos,
        "cash_weight": round(1 - sum(p["weight"] for p in pos), 4)}))
    assert validate.check(run / "allocation.json") == []
    assert validate.latest() == run / "allocation.json"
