import json

import pytest

from scanner import config, sizing, validate
from tests.conftest import synthetic_ohlcv


def _setup_run(sandbox, cards, regime="risk-on", syms=None):
    run = sandbox / "reports" / "nasdaq" / "2026-11-09" / "premarket"
    (run / "research").mkdir(parents=True)
    syms = syms or [c["ticker"] for c in cards]
    synthetic_ohlcv(["QQQ"] + syms, seed=1).to_pickle(run / "ohlcv.pkl")
    for c in cards:
        (run / "research" / f"{c['ticker']}.json").write_text(json.dumps(c))
    (run / "regime_view.json").write_text(json.dumps({"regime": regime}))
    return run


def card(t, rating="Buy", conf=0.6, price=100, stop=95, target=112, sector="Technology"):
    return {"ticker": t, "rating": rating, "confidence": conf, "entry": price, "stop": stop,
            "target": target, "sector": sector, "horizon_days": 10}


def test_risk_based_weight_and_amount(sandbox):
    run = _setup_run(sandbox, [card("AAA")])
    r = sizing.size(run)
    p = r["positions"][0]
    # risk: 0.0075 / 0.05 = 0.15; kelly: 0.6 - 0.4/2.4 = 0.433 -> /4 = 0.108; max 0.10 -> 0.10
    assert p["binding"] == "max"
    assert p["engine_weight"] == pytest.approx(0.10, abs=0.001)
    assert p["amount_units"] == pytest.approx(100.0, abs=0.5)  # 10% of 1000 units


def test_rejections(sandbox):
    cards = [card("LOWRR", target=103), card("HOLD", rating="Hold"),
             card("NEGK", conf=0.2), {"ticker": "MISS", "rating": "Buy"}]
    r = sizing.size(_setup_run(sandbox, cards))
    reasons = {x["ticker"]: x["reason"] for x in r["rejected"]}
    assert "reward/risk" in reasons["LOWRR"]
    assert "Hold" in reasons["HOLD"]
    assert "Kelly" in reasons["NEGK"]
    assert "missing fields" in reasons["MISS"]
    assert r["positions"] == []


def test_regime_and_sector_caps(sandbox):
    cards = [card(f"T{i}") for i in range(5)]  # 5 x 0.10 in one sector
    r = sizing.size(_setup_run(sandbox, cards, regime="risk-on"))
    tech = sum(p["engine_weight"] for p in r["positions"])
    assert tech <= 0.30 + 1e-3


def test_risk_off_scales_down(sandbox):
    r = sizing.size(_setup_run(sandbox, [card("AAA")], regime="risk-off"))
    assert r["positions"][0]["engine_weight"] == pytest.approx(0.04, abs=0.001)


def test_veto_and_drawdown(sandbox):
    run = _setup_run(sandbox, [card("AAA"), card("BBB", sector="Health")])
    (run / "risk_review.json").write_text(json.dumps({"vetoes": [{"ticker": "AAA", "reason": "x"}]}))
    r = sizing.size(run)
    assert [p["ticker"] for p in r["positions"]] == ["BBB"]
    (sandbox / "state" / "portfolio.json").write_text(json.dumps(
        {"cash_units": 870, "peak_value": 1000, "positions": []}))
    r = sizing.size(run)
    assert r["positions"] == []  # 13% drawdown: no new buys


def _allocation(run, r, bump=1.0):
    pos = [{"ticker": p["ticker"], "status": p["status"], "sector": p["sector"],
            "engine_weight": p["engine_weight"], "weight": round(p["engine_weight"] * bump, 4),
            "rationale": "test"} for p in r["positions"]]
    a = {"as_of": "2026-11-09", "session": "premarket", "exchange": "NASDAQ",
         "regime": r["regime"], "positions": pos,
         "cash_weight": round(1 - sum(p["weight"] for p in pos), 4)}
    path = run / "allocation.json"
    path.write_text(json.dumps(a))
    return path


def test_validate_accepts_engine_and_rejects_overrides(sandbox):
    run = _setup_run(sandbox, [card("AAA", stop=90, target=130), card("BBB", sector="Health")])
    r = sizing.size(run)
    assert validate.check(_allocation(run, r)) == []
    errs = validate.check(_allocation(run, r, bump=1.6))
    assert any("limit" in e for e in errs)


def test_held_position_marked_to_market(sandbox):
    run = _setup_run(sandbox, [], syms=["HLD"])
    import pandas as pd
    px = pd.read_pickle(run / "ohlcv.pkl")
    last = float(px[px["symbol"] == "HLD"]["close"].iloc[-1])
    (sandbox / "state" / "portfolio.json").write_text(json.dumps({
        "cash_units": 900, "peak_value": 1000,
        "positions": [{"ticker": "HLD", "units": 100, "entry_price": last, "sector": "Tech"}]}))
    r = sizing.size(run)
    assert r["portfolio_value_units"] == pytest.approx(1000, abs=0.01)
    assert r["positions"][0]["engine_weight"] == pytest.approx(0.10, abs=0.001)
