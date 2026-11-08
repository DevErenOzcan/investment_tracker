"""Universe: ordinary common stocks listed on the exchange."""
from __future__ import annotations

import io
import re
from datetime import date

import pandas as pd
import requests

from . import config

UA = {"User-Agent": "Mozilla/5.0 (investment_tracker research)"}

# drop SPACs, warrants, rights, units, preferreds and debt instruments
_EXCLUDE_NAME = re.compile(
    r"\b(?:warrant|warrants|right|rights|unit|units|acquisition corp|acquisition co|"
    r"preferred|notes due|debentures|trust preferred)\b",
    re.IGNORECASE,
)


def parse_nasdaqlisted(text: str) -> pd.DataFrame:
    lines = [ln for ln in text.splitlines() if ln and not ln.startswith("File Creation Time")]
    df = pd.read_csv(io.StringIO("\n".join(lines)), sep="|", dtype=str).fillna("")
    df = df[
        (df["Test Issue"] == "N")
        & (df["ETF"] == "N")
        & (df.get("NextShares", pd.Series("N", index=df.index)) != "Y")
        & (df["Financial Status"].isin(["N", ""]))
    ]
    df = df[~df["Security Name"].str.contains(_EXCLUDE_NAME)]
    df = df[df["Symbol"].str.fullmatch(r"[A-Z]{1,5}")]
    return df.rename(columns={"Symbol": "symbol", "Security Name": "name",
                              "Market Category": "market_category"})[
        ["symbol", "name", "market_category"]].reset_index(drop=True)


def load(exchange_code: str = "nasdaq", day: date | None = None) -> pd.DataFrame:
    ex = config.exchange(exchange_code)
    day = day or date.today()
    cache = config.CACHE_DIR / f"universe_{ex['code']}_{day.isoformat()}.csv"
    if cache.exists():
        return pd.read_csv(cache, dtype=str)
    src = ex["universe"]
    if src["source"] == "nasdaqtrader":
        r = requests.get(src["url"], headers=UA, timeout=30)
        r.raise_for_status()
        df = parse_nasdaqlisted(r.text)
    elif src["source"] == "csv":
        df = pd.read_csv(config.ROOT / src["path"], dtype=str)
    else:
        raise ValueError(f"unknown universe source: {src['source']}")
    cache.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(cache, index=False)
    return df
