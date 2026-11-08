"""Configuration and path helpers."""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT / "config"
CACHE_DIR = ROOT / "data" / "cache"
STATE_DIR = ROOT / "state"
REPORTS_DIR = ROOT / "reports"


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def exchange(code: str = "nasdaq") -> dict:
    return load_yaml(CONFIG_DIR / "exchanges" / f"{code.lower()}.yaml")


def risk() -> dict:
    return load_yaml(CONFIG_DIR / "risk.yaml")


def portfolio_config() -> dict:
    return load_yaml(CONFIG_DIR / "portfolio.yaml")


def portfolio_state() -> dict:
    path = STATE_DIR / "portfolio.json"
    if not path.exists():
        base = portfolio_config().get("notional_base", 1000)
        return {"cash_units": base, "peak_value": base, "positions": []}
    return json.loads(path.read_text(encoding="utf-8"))


def run_dir(session: str, day: date | None = None, exchange_code: str = "nasdaq") -> Path:
    day = day or date.today()
    d = REPORTS_DIR / exchange_code.lower() / day.isoformat() / session
    d.mkdir(parents=True, exist_ok=True)
    return d


def clean(o):
    """JSON-safe conversion: NaN/inf -> None, numpy/pandas types -> Python types."""
    import math

    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if hasattr(o, "isoformat") and not isinstance(o, str):  # date, datetime, pd.Timestamp
        return o.isoformat()
    if hasattr(o, "item") and not isinstance(o, (str, bytes)):  # numpy scalars
        try:
            o = o.item()
        except Exception:  # noqa: BLE001
            pass
    if isinstance(o, float) and (math.isnan(o) or math.isinf(o)):
        return None
    if isinstance(o, (str, int, float, bool)) or o is None:
        return o
    if hasattr(o, "isoformat"):
        return o.isoformat()
    return str(o)


def write_json(path: Path, obj) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(clean(obj), indent=2, ensure_ascii=False), encoding="utf-8")


def read_json(path: Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))
