"""SEC EDGAR: company financials (companyfacts) and recent filings (8-K etc.).

SEC requires a User-Agent with contact details on every request. Set the
`SEC_USER_AGENT` environment variable to a value like "Full Name email@example.com".
"""
from __future__ import annotations

import json
import logging
import os
import time
from datetime import date, timedelta

import requests

from . import config

log = logging.getLogger(__name__)
_LAST = [0.0]


def _ua() -> dict:
    return {"User-Agent": os.environ.get("SEC_USER_AGENT", "investment_tracker research bot"),
            "Accept-Encoding": "gzip, deflate"}


def _get(url: str) -> dict | None:
    wait = 0.12 - (time.time() - _LAST[0])  # ~8 requests/s, SEC limit is 10
    if wait > 0:
        time.sleep(wait)
    _LAST[0] = time.time()
    try:
        r = requests.get(url, headers=_ua(), timeout=30)
        r.raise_for_status()
        return r.json()
    except Exception as e:  # noqa: BLE001
        log.warning("SEC %s: %s", url, e)
        return None


def cik_map() -> dict[str, int]:
    cache = config.CACHE_DIR / f"sec_tickers_{date.today().isoformat()}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    data = _get("https://www.sec.gov/files/company_tickers.json") or {}
    m = {v["ticker"].upper(): int(v["cik_str"]) for v in data.values()}
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(m))
    return m


_REVENUE_TAGS = ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                 "SalesRevenueNet"]


def _quarterly(facts: dict, tag: str, unit: str = "USD") -> list[dict]:
    try:
        rows = facts["facts"]["us-gaap"][tag]["units"][unit]
    except KeyError:
        return []
    q = [r for r in rows if (r.get("fp") or "").startswith("Q") or r.get("form") == "10-Q"]
    # only ~3-month periods
    out = {}
    for r in q:
        if "start" not in r:
            continue
        span = (date.fromisoformat(r["end"]) - date.fromisoformat(r["start"])).days
        if 80 <= span <= 100:
            out[r["end"]] = {"end": r["end"], "val": r["val"], "filed": r.get("filed")}
    return sorted(out.values(), key=lambda x: x["end"])


def fundamentals(symbol: str, as_of: date | None = None) -> dict:
    """Last 8 quarters of revenue/net income and YoY growth. Filings after as_of are excluded."""
    as_of = as_of or date.today()
    cik = cik_map().get(symbol.upper())
    if not cik:
        return {"available": False, "reason": "CIK not found"}
    facts = _get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json")
    if not facts:
        return {"available": False, "reason": "companyfacts unavailable"}

    def series(tags):
        # Companies switch tags over time: pick the tag with the most recent quarter
        best = []
        for t in tags:
            s = [r for r in _quarterly(facts, t) if (r["filed"] or "9999") <= as_of.isoformat()]
            if s and (not best or s[-1]["end"] > best[-1]["end"]):
                best = s
        return best[-8:]

    rev = series(_REVENUE_TAGS)
    ni = series(["NetIncomeLoss"])

    def yoy(s):
        # The series can have gaps (Q4 is not reported as a 3-month period in the 10-K):
        # find the quarter one year earlier by date (365 +/- 20 days).
        if not s:
            return None
        last = s[-1]
        d1 = date.fromisoformat(last["end"])
        for r in reversed(s[:-1]):
            gap = (d1 - date.fromisoformat(r["end"])).days
            if 345 <= gap <= 385:
                return round(last["val"] / r["val"] - 1, 4) if r["val"] else None
        return None

    stale = bool(rev) and (as_of - date.fromisoformat(rev[-1]["end"])).days > 200
    return {"available": True, "cik": cik, "revenue_q": rev, "net_income_q": ni,
            "stale_warning": "latest revenue quarter is older than 200 days" if stale else None,
            "revenue_yoy": yoy(rev), "net_income_yoy": yoy(ni)}


def recent_filings(symbol: str, days: int = 10, forms=("8-K", "10-Q", "10-K", "S-3", "424B5")) -> list[dict]:
    cik = cik_map().get(symbol.upper())
    if not cik:
        return []
    sub = _get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json")
    if not sub:
        return []
    r = sub.get("filings", {}).get("recent", {})
    cutoff = (date.today() - timedelta(days=days)).isoformat()
    out = []
    for form, filed, acc, doc, items in zip(r.get("form", []), r.get("filingDate", []),
                                            r.get("accessionNumber", []),
                                            r.get("primaryDocument", []),
                                            r.get("items", [""] * len(r.get("form", [])))):
        if filed < cutoff:
            break
        if form in forms:
            out.append({"form": form, "filed": filed, "items": items,
                        "url": f"https://www.sec.gov/Archives/edgar/data/{cik}/"
                               f"{acc.replace('-', '')}/{doc}"})
    return out
