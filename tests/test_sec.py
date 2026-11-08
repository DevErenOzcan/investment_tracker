from datetime import date

from scanner import sec


def _row(start, end, val, filed, fp="Q1"):
    return {"start": start, "end": end, "val": val, "filed": filed, "fp": fp, "form": "10-Q"}


def test_yoy_matches_same_quarter_last_year_despite_gaps(monkeypatch):
    rows = [  # Q4s missing: s[-5] would hit the wrong quarter
        _row("2025-01-01", "2025-03-31", 100, "2025-05-01"),
        _row("2025-04-01", "2025-06-30", 110, "2025-08-01"),
        _row("2025-07-01", "2025-09-30", 120, "2025-11-01"),
        _row("2026-01-01", "2026-03-31", 130, "2026-05-01"),
        _row("2026-04-01", "2026-06-30", 140, "2026-08-01"),
        _row("2026-07-01", "2026-09-30", 150, "2026-11-01", fp=None),
    ]
    old = [_row("2018-01-01", "2018-03-31", 999, "2018-05-01")]
    facts = {"facts": {"us-gaap": {
        "Revenues": {"units": {"USD": old}},
        "RevenueFromContractWithCustomerExcludingAssessedTax": {"units": {"USD": rows}},
        "NetIncomeLoss": {"units": {"USD": rows}}}}}
    monkeypatch.setattr(sec, "cik_map", lambda: {"XYZ": 1})
    monkeypatch.setattr(sec, "_get", lambda url: facts)
    f = sec.fundamentals("XYZ", as_of=date(2026, 11, 8))
    assert f["revenue_q"][-1]["end"] == "2026-09-30"   # stale tag not chosen
    assert f["revenue_yoy"] == 0.25                     # 150 / 120 - 1
    assert f["stale_warning"] is None
