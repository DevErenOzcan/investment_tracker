from datetime import datetime, timezone

from scanner import clock


def _at(s):
    return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)


def test_premarket_window_winter_time():
    # Mon 9 Nov 2026, EST (UTC-5): open 14:30 UTC, window 13:30-14:25
    assert clock.check("premarket", now=_at("2026-11-09T13:50:00"))["run"]
    assert not clock.check("premarket", now=_at("2026-11-09T12:50:00"))["run"]


def test_preclose_window_and_half_day():
    # Normal day: close 21:00 UTC, window 19:45-20:40
    assert clock.check("preclose", now=_at("2026-11-09T20:15:00"))["run"]
    # 27 Nov 2026 (day after Thanksgiving) early close: 18:00 UTC
    r = clock.check("preclose", now=_at("2026-11-27T17:15:00"))
    assert r["half_day"] and r["run"]


def test_holiday_and_weekend():
    assert not clock.check("premarket", now=_at("2026-11-26T13:50:00"))["run"]  # Thanksgiving
    assert not clock.check("premarket", now=_at("2026-11-07T13:50:00"))["run"]  # Saturday
