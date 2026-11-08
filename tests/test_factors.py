from scanner import factors
from tests.conftest import synthetic_ohlcv


def test_compute_and_score_ranks_strong_trend_first():
    syms = ["QQQ", "UP", "FLAT", "DOWN"]
    px = synthetic_ohlcv(syms, drift={"QQQ": 0.0005, "UP": 0.004, "FLAT": 0.0, "DOWN": -0.004})
    f = factors.compute(px, "QQQ")
    assert set(f["symbol"]) == set(syms)
    s = factors.score(f[f["symbol"] != "QQQ"])
    assert s.iloc[0]["symbol"] == "UP"
    assert s.iloc[-1]["symbol"] == "DOWN"
    up = f.set_index("symbol").loc["UP"]
    assert 0 < up["atr_pct"] < 0.1
    assert up["rs_63"] > 0


def test_short_history_is_skipped():
    px = synthetic_ohlcv(["QQQ", "NEW"], days=100)
    assert factors.compute(px, "QQQ").empty
