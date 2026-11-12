from datetime import datetime, timedelta, timezone
from email.utils import format_datetime

from scanner import data


def _rss(*items):
    body = "".join(
        f"<item><title>{t}</title><link>https://example.com/{i}</link>"
        f"<pubDate>{format_datetime(d)}</pubDate><source url='https://example.com'>Pub</source></item>"
        for i, (t, d) in enumerate(items))
    return f"<?xml version='1.0'?><rss><channel>{body}</channel></rss>"


def test_parse_google_rss_drops_old_items_and_sorts_newest_first():
    now = datetime.now(timezone.utc)
    xml = _rss(("older", now - timedelta(days=2)), ("stale", now - timedelta(days=30)),
               ("newest", now - timedelta(hours=1)))
    out = data.parse_google_rss(xml, days=7)
    assert [x["title"] for x in out] == ["newest", "older"]
    assert out[0]["publisher"] == "Pub"


def test_news_falls_back_to_rss_when_yahoo_fails(monkeypatch):
    def boom(*a, **k):
        raise RuntimeError("proxy 403")
    monkeypatch.setattr(data, "_yahoo_news", boom)
    monkeypatch.setattr(data, "_google_rss_news", lambda *a, **k: [{"title": "x"}])
    r = data.news_with_status("NVDA")
    assert (r["status"], r["source"], len(r["items"])) == ("ok", "google_rss", 1)
    assert r["errors"] and "yahoo" in r["errors"][0]


def test_news_unavailable_when_every_source_fails(monkeypatch):
    def boom(*a, **k):
        raise RuntimeError("blocked")
    monkeypatch.setattr(data, "_yahoo_news", boom)
    monkeypatch.setattr(data, "_google_rss_news", boom)
    r = data.news_with_status("NVDA")
    assert r["status"] == "unavailable" and r["items"] == []


def test_rss_fills_days_older_than_yahoo(monkeypatch):
    y = [{"title": "Today", "published": "2026-11-12T10:00:00+00:00"}]
    r_ = [{"title": "today", "published": "2026-11-12T09:00:00+00:00"},
          {"title": "Earlier", "published": "2026-11-09T09:00:00+00:00"}]
    monkeypatch.setattr(data, "_yahoo_news", lambda *a, **k: y)
    monkeypatch.setattr(data, "_google_rss_news", lambda *a, **k: r_)
    r = data.news_with_status("NVDA")
    assert [x["title"] for x in r["items"]] == ["Today", "Earlier"]
    assert r["source"] == "yahoo+google_rss"


def test_spread_by_day_keeps_earlier_days():
    items = [{"title": f"t{i}", "published": "2026-11-12T10:00:00"} for i in range(10)]
    items += [{"title": "old", "published": "2026-11-06T10:00:00"}]
    out = data._spread_by_day(items, 3)
    assert "old" in [x["title"] for x in out] and len(out) == 3
