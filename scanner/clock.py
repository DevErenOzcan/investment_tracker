"""Market clock gate.

Scheduled runs fire on a fixed time. This module checks the exchange's local time and
holiday calendar and says whether now is inside the right window for the session.

    python -m scanner.clock --session premarket [--exchange nasdaq] [--at 2026-11-09T13:50Z]

Exit code 0 = run, 3 = outside the window / holiday (the session should stop at once).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone

import exchange_calendars as xcals
import pandas as pd

from . import config


def check(session: str, exchange_code: str = "nasdaq", now: datetime | None = None) -> dict:
    ex = config.exchange(exchange_code)
    cal = xcals.get_calendar(ex["calendar"])
    now = now or datetime.now(timezone.utc)
    now_ts = pd.Timestamp(now).tz_convert("UTC")
    local_day = now_ts.tz_convert(ex["timezone"]).normalize().tz_localize(None)

    out = {"session": session, "exchange": ex["code"], "now_utc": now_ts.isoformat(),
           "local_date": local_day.date().isoformat(), "run": False}

    if not cal.is_session(local_day):
        out["reason"] = "exchange closed today"
        return out

    open_ts = cal.session_open(local_day)
    close_ts = cal.session_close(local_day)
    s = ex["sessions"][session]
    if session == "premarket":
        start = open_ts - timedelta(minutes=s["minutes_before_open_start"])
        end = open_ts - timedelta(minutes=s["minutes_before_open_end"])
    elif session == "preclose":
        start = close_ts - timedelta(minutes=s["minutes_before_close_start"])
        end = close_ts - timedelta(minutes=s["minutes_before_close_end"])
    else:
        raise ValueError(f"unknown session: {session}")

    out.update({
        "open_local": open_ts.tz_convert(ex["timezone"]).isoformat(),
        "close_local": close_ts.tz_convert(ex["timezone"]).isoformat(),
        "window_utc": [start.isoformat(), end.isoformat()],
        "half_day": (close_ts - open_ts) < pd.Timedelta(hours=6),
    })
    if start <= now_ts <= end:
        out["run"] = True
    else:
        out["reason"] = "outside the window"
    return out


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--session", required=True, choices=["premarket", "preclose"])
    p.add_argument("--exchange", default="nasdaq")
    p.add_argument("--at", help="ISO time (UTC) for testing")
    p.add_argument("--force", action="store_true", help="ignore the window (manual run)")
    a = p.parse_args(argv)
    now = datetime.fromisoformat(a.at.replace("Z", "+00:00")) if a.at else None
    res = check(a.session, a.exchange, now)
    if a.force:
        res["run"], res["forced"] = True, True
    print(json.dumps(res, ensure_ascii=False))
    return 0 if res["run"] else 3


if __name__ == "__main__":
    sys.exit(main())
