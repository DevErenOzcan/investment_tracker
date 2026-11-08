import json
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from scanner import config

ROOT = Path(__file__).resolve().parent.parent


def synthetic_ohlcv(symbols, days=300, seed=0, drift=None):
    rng = np.random.default_rng(seed)
    dates = pd.bdate_range(end="2026-11-06", periods=days)
    rows = []
    for i, s in enumerate(symbols):
        mu = (drift or {}).get(s, 0.0005 * (i % 5))
        r = rng.normal(mu, 0.02, days)
        close = 50 * np.exp(np.cumsum(r))
        high = close * (1 + rng.uniform(0, 0.02, days))
        low = close * (1 - rng.uniform(0, 0.02, days))
        vol = rng.integers(500_000, 3_000_000, days)
        rows.append(pd.DataFrame({"symbol": s, "date": dates, "open": close, "high": high,
                                  "low": low, "close": close, "volume": vol}))
    return pd.concat(rows, ignore_index=True)


@pytest.fixture
def sandbox(tmp_path, monkeypatch):
    """Copy the real config and point state/reports at a temp dir."""
    shutil.copytree(ROOT / "config", tmp_path / "config")
    (tmp_path / "state").mkdir()
    (tmp_path / "reports").mkdir()
    (tmp_path / "data" / "cache").mkdir(parents=True)
    (tmp_path / "state" / "portfolio.json").write_text(json.dumps(
        {"cash_units": 1000, "peak_value": 1000, "positions": []}))
    monkeypatch.setattr(config, "ROOT", tmp_path)
    monkeypatch.setattr(config, "CONFIG_DIR", tmp_path / "config")
    monkeypatch.setattr(config, "STATE_DIR", tmp_path / "state")
    monkeypatch.setattr(config, "REPORTS_DIR", tmp_path / "reports")
    monkeypatch.setattr(config, "CACHE_DIR", tmp_path / "data" / "cache")
    return tmp_path
