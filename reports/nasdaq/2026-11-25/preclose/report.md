# NASDAQ pre-close review, 2026-11-25

## 1. Summary
- Regime: **risk-off** (confidence 0.93). QQQ 638.1 is below its 50- and 200-day averages (ret_21 -10.4%), VIX is 31.19 (1y percentile 0.991), semis and tech lead the selling, and XLP, XLV and XLY are holding up.
- Funnel (morning): 2971 universe → 997 liquid → 25 candidates → 3 recommendations plus 1 veto. Pre-close re-checked the 3 morning recommendations, and all 3 are confirmed.
- Invested weight is **2.44%** (24.4 units) and cash is **97.56%** (975.6 units). All three engine weights are lower than in the morning.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| GMAB | buy-confirm | 0.85% | 8.5 | 54.8-55.8 | 49.9 | 69.7 | Overweight | 0.42 |
| PGNY | buy-confirm | 0.90% | 9.0 | 35.6-36.2 | 34.8 | 39.5 | Overweight | 0.42 |
| CROX | buy-confirm | 0.69% | 6.9 | 156.0-159.0 | 153.4 | 174.6 | Overweight | 0.40 |

All three buys are pullback-only. Each last price is at or above its zone top (GMAB 56.78, PGNY 36.23, CROX 159.57), so do not chase. If a name does not trade inside its zone, the plan lapses. Every PM weight equals the engine weight, with no adjustment.

Changes from the morning:
- **GMAB:** weight 0.92% → 0.85%. The zone floor moves from 54.2 to 54.8.
- **PGNY:** weight 1.03% → 0.90%. The zone top moves from 36.3 to 36.2.
- **CROX:** weight 0.95% → 0.69%. The stop moves up from 152.5 to 153.4, the target moves down from 176.0 to 174.6, and the zone changes from 155.5-159.0 to 156.0-159.0.

## 3. Current holdings
No holdings: `state/portfolio.json` is all cash (1000 units), so there are no stop or target alerts. Risk-officer held alerts: none.

Portfolio alert: all three names are the same kind of trade. Each was re-rated on news or earnings, sits near its 52-week high, and is up about 30% over 21 days with RSI 62-69. A momentum unwind in this tape could hit all three at once. GMAB and PGNY together make up about 1.75% of healthcare exposure (lessons item 8).

## 4. Theses
**GMAB** (0.85%, 8.5 units)
- Thesis:
  - Profitable biotech (operating margin 30.6%) whose October Phase III re-rating has held in a 50.24-59.02 base.
  - Today it dipped to 54.91, inside the zone, and trades at 56.78 late in the session, above SMA20 53.77. RBC published a supportive note today.
  - R/R is 2.67 from the zone and 1.88 at the last price. The target needs a break above 59.97, and the 59.0-60.0 resistance is only about 1R away, so scale out there. The volume behind the bounce is light (vol_ratio 0.75).
- Invalidation: a daily close below 50.24, or a close under SMA20 (about 53.8) on rising volume.

**PGNY** (0.90%, 9.0 units)
- Thesis:
  - Q3 re-rating: revenue +8.9% YoY, net income +89% YoY, forward P/E 15.1. The stock is consolidating at 34.94-37.21 above SMA20 34.32.
  - Today's range was 35.90-36.61 on light volume. R/R at the last price is about 2.3 to the 39.5 measured move.
  - First resistance at 37.21 is close (R/R about 0.7 from the last price), so take partial profit there. News support is mostly Zacks screens.
- Invalidation: a daily close below 34.80, or a high-volume rejection at 37.21 that closes below 35.5.

**CROX** (0.69%, 6.9 units)
- Thesis:
  - Post-earnings consolidator at 153.9-164.2 with forward P/E about 10 and rising estimates. XLY is holding up while tech sells off.
  - Today it dipped to 154.46, held the 153.92 swing low and recovered to 159.57, above a rising SMA20 of 157.14.
  - It has the lowest confidence on the slate and carries beta 1.5, leverage and 10.5% short interest. Resistance at 164.24 has rejected it three times, so scale out there.
- Invalidation: a daily close below 153.4.

## 5. Rejected and vetoed
- **PLMR:** the morning veto stands. R/R was below 1.5 at both the last and pre-market prices, and there is undated investor-day and follow-on offering risk. The re-assessment condition was a price inside 163.5-167.0, but there is no pre-close packet, so the name stays vetoed and was not reviewed.
- The risk-officer issued no new vetoes at pre-close, and the engine rejected nothing.

## 6. Data notes
- Intraday prices are about 15 minutes delayed, and volumes are partial-session.
- **GMAB:** the SEC quarterly series is empty (foreign issuer, 6-K filings are not visible), so the growth trend is unverified. The engine `price` field is the 55.3 zone midpoint, while the last price is 56.78 (`last_price` in allocation.json). Its sector label was normalised to "Healthcare" so the engine's sector cap groups it with PGNY.
- **PGNY:** the research file has `earnings_date: null`; the packet profile date 2026-11-04 is the past Q3 report. The next date is unknown, likely early 2027.
- **News:** many RSS items are title-only, and none of today's news is a new catalyst except the GMAB RBC note.
- **Funnel:** there is no pre-close `candidates.json`, so the funnel counts above come from the morning run.

This report is not investment advice; decisions and orders are the owner's.
