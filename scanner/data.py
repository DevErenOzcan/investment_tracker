"""Market data: yfinance (primary), Stooq (daily fallback), per-day cache.

All functions return a "long" OHLCV table:
    columns = [symbol, date, open, high, low, close, volume]
"""
from __future__ import annotations

import hashlib
import io
import logging
import time
from datetime import date, datetime, timedelta, timezone

import pandas as pd
import requests

from . import config

log = logging.getLogger(__name__)
UA = {"User-Agent": "Mozilla/5.0 (investment_tracker research)"}
COLS = ["symbol", "date", "open", "high", "low", "close", "volume"]


def _yf():
    import yfinance as yf  # lazy import so tests run offline
    return yf


def _wide_to_long(df: pd.DataFrame, symbols: list[str]) -> pd.DataFrame:
    if df is None or df.empty:
        return pd.DataFrame(columns=COLS)
    frames = []
    if isinstance(df.columns, pd.MultiIndex):
        level0 = set(df.columns.get_level_values(0))
        for s in symbols:
            if s not in level0:
                continue
            sub = df[s].copy()
            sub["symbol"] = s
            frames.append(sub)
    else:
        sub = df.copy()
        sub["symbol"] = symbols[0]
        frames.append(sub)
    out = pd.concat(frames)
    out = out.reset_index().rename(columns=str.lower)
    out = out.rename(columns={"index": "date", "datetime": "date"})
    out["date"] = pd.to_datetime(out["date"]).dt.tz_localize(None).dt.normalize()
    out = out.dropna(subset=["close"])
    return out[COLS]


def history(symbols: list[str], days: int = 300, chunk: int = 150, suffix: str = "",
            use_cache: bool = True) -> pd.DataFrame:
    """Daily OHLCV. Reads from the per-day cache for the same symbol list."""
    today = date.today().isoformat()
    key = hashlib.sha1(f"{sorted(symbols)}|{days}|{suffix}".encode()).hexdigest()[:12]
    cache = config.CACHE_DIR / f"ohlcv_{today}_{key}.pkl"
    if use_cache and cache.exists():
        return pd.read_pickle(cache)

    yf = _yf()
    start = (date.today() - timedelta(days=days)).isoformat()
    frames = []
    for i in range(0, len(symbols), chunk):
        part = symbols[i:i + chunk]
        tickers = [s + suffix for s in part]
        for attempt in range(3):
            try:
                raw = yf.download(tickers, start=start, group_by="ticker", auto_adjust=True,
                                  progress=False, threads=True)
                long = _wide_to_long(raw, tickers)
                if suffix:
                    long["symbol"] = long["symbol"].str.removesuffix(suffix)
                frames.append(long)
                break
            except Exception as e:  # noqa: BLE001
                log.warning("yfinance batch %s failed (%s), retrying", i, e)
                time.sleep(2 * (attempt + 1))
    out = pd.concat(frames) if frames else pd.DataFrame(columns=COLS)

    missing = sorted(set(symbols) - set(out["symbol"].unique()))
    if missing and len(missing) <= 50:  # Stooq fallback only for a few missing symbols
        for s in missing:
            st = stooq_history(s, days)
            if not st.empty:
                out = pd.concat([out, st])
    out = out.sort_values(["symbol", "date"]).reset_index(drop=True)
    cache.parent.mkdir(parents=True, exist_ok=True)
    out.to_pickle(cache)
    return out


def stooq_history(symbol: str, days: int = 300, market: str = "us") -> pd.DataFrame:
    url = f"https://stooq.com/q/d/l/?s={symbol.lower()}.{market}&i=d"
    try:
        r = requests.get(url, headers=UA, timeout=20)
        r.raise_for_status()
        df = pd.read_csv(io.StringIO(r.text))
    except Exception as e:  # noqa: BLE001
        log.warning("stooq %s: %s", symbol, e)
        return pd.DataFrame(columns=COLS)
    if "Close" not in df.columns:
        return pd.DataFrame(columns=COLS)
    df = df.rename(columns=str.lower)
    df["date"] = pd.to_datetime(df["date"])
    df = df[df["date"] >= pd.Timestamp(date.today() - timedelta(days=days))]
    df["symbol"] = symbol
    return df[COLS]


def info(symbol: str, suffix: str = "") -> dict:
    """Market cap, sector, fundamental ratios and earnings date."""
    yf = _yf()
    t = yf.Ticker(symbol + suffix)
    out = {"symbol": symbol}
    try:
        i = t.info or {}
    except Exception as e:  # noqa: BLE001
        log.warning("info %s: %s", symbol, e)
        i = {}
    keep = ["shortName", "sector", "industry", "marketCap", "trailingPE", "forwardPE",
            "priceToSalesTrailing12Months", "enterpriseToEbitda", "profitMargins",
            "operatingMargins", "grossMargins", "revenueGrowth", "earningsGrowth",
            "returnOnEquity", "debtToEquity", "freeCashflow", "totalCash", "totalDebt",
            "beta", "shortPercentOfFloat", "heldPercentInstitutions",
            "recommendationMean", "numberOfAnalystOpinions", "targetMeanPrice",
            "fiftyTwoWeekHigh", "fiftyTwoWeekLow", "averageVolume", "preMarketPrice",
            "regularMarketPrice", "regularMarketPreviousClose"]
    out.update({k: i.get(k) for k in keep})
    out["earnings_date"] = None
    try:
        cal = t.calendar
        ed = cal.get("Earnings Date") if isinstance(cal, dict) else None
        if ed:
            out["earnings_date"] = str(ed[0] if isinstance(ed, list) else ed)
    except Exception:  # noqa: BLE001
        pass
    return out


def news(symbol: str, suffix: str = "", max_items: int = 12, days: int = 7) -> list[dict]:
    """Recent news items; see news_with_status for where they came from."""
    return news_with_status(symbol, suffix, max_items, days)["items"]


def news_with_status(symbol: str, suffix: str = "", max_items: int = 12, days: int = 7) -> dict:
    """Yahoo Finance news, falling back to the Google News RSS search when Yahoo fails or is empty.

    Returns {"status": "ok"|"empty"|"unavailable", "source": "yahoo"|"google_rss"|None,
    "errors": [...], "items": [...]}. "unavailable" means every source failed, which is not the
    same as "no news".
    """
    errors: list[str] = []
    try:
        items = _yahoo_news(symbol, suffix, max_items, days)
        if items:
            return {"status": "ok", "source": "yahoo", "errors": errors, "items": items}
    except Exception as e:  # noqa: BLE001
        log.warning("news %s (yahoo): %s", symbol, e)
        errors.append(f"yahoo: {e}"[:200])
    try:
        items = _google_rss_news(symbol, max_items, days)
        if items:
            return {"status": "ok", "source": "google_rss", "errors": errors, "items": items}
    except Exception as e:  # noqa: BLE001
        log.warning("news %s (google rss): %s", symbol, e)
        errors.append(f"google_rss: {e}"[:200])
    status = "unavailable" if len(errors) == 2 else "empty"
    return {"status": status, "source": None, "errors": errors, "items": []}


def _google_rss_news(symbol: str, max_items: int = 12, days: int = 7) -> list[dict]:
    r = requests.get("https://news.google.com/rss/search",
                     params={"q": f"{symbol} stock when:{days}d", "hl": "en-US", "gl": "US",
                             "ceid": "US:en"}, headers=UA, timeout=20)
    r.raise_for_status()
    return parse_google_rss(r.text, max_items, days)


def parse_google_rss(xml_text: str, max_items: int = 12, days: int = 7) -> list[dict]:
    import xml.etree.ElementTree as ET
    from email.utils import parsedate_to_datetime

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    out = []
    for it in ET.fromstring(xml_text).iter("item"):
        try:
            when = parsedate_to_datetime(it.findtext("pubDate") or "")
        except (TypeError, ValueError):
            when = None
        if when and when < cutoff:
            continue
        src = it.find("source")
        out.append({
            "title": it.findtext("title"),
            "publisher": src.text if src is not None else None,
            "published": when.isoformat() if when else None,
            "summary": "",
            "url": it.findtext("link"),
        })
    out.sort(key=lambda x: x["published"] or "", reverse=True)
    return out[:max_items]


def _yahoo_news(symbol: str, suffix: str = "", max_items: int = 12, days: int = 7) -> list[dict]:
    yf = _yf()
    items = yf.Ticker(symbol + suffix).news or []
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    out = []
    for it in items:
        c = it.get("content", it)
        ts = c.get("pubDate") or c.get("providerPublishTime")
        try:
            when = (datetime.fromtimestamp(ts, timezone.utc) if isinstance(ts, (int, float))
                    else datetime.fromisoformat(str(ts).replace("Z", "+00:00")))
        except Exception:  # noqa: BLE001
            when = None
        if when and when < cutoff:
            continue
        url = (c.get("canonicalUrl") or {}).get("url") if isinstance(c.get("canonicalUrl"), dict) \
            else c.get("link")
        out.append({
            "title": c.get("title"),
            "publisher": (c.get("provider") or {}).get("displayName") if isinstance(
                c.get("provider"), dict) else c.get("publisher"),
            "published": when.isoformat() if when else None,
            "summary": (c.get("summary") or "")[:400],
            "url": url,
        })
        if len(out) >= max_items:
            break
    return out


def last_prices(symbols: list[str], suffix: str = "") -> dict[str, float]:
    """Intraday last price (about 15 min delayed). For the pre-close session."""
    yf = _yf()
    out = {}
    if not symbols:
        return out
    raw = yf.download([s + suffix for s in symbols], period="1d", interval="5m",
                      group_by="ticker", progress=False, auto_adjust=True)
    long = _wide_to_long(raw, [s + suffix for s in symbols])
    for s, g in long.groupby("symbol"):
        out[s.removesuffix(suffix) if suffix else s] = float(g["close"].iloc[-1])
    return out
