# NASDAQ preclose review: 2026-11-17

## 1. Summary
- **Regime:** risk-off (confidence 0.8). QQQ is below its 50- and 200-day averages (ret_21 -6.77%), the VIX is at the 0.877 1-year percentile and ^TNX is at 5.141. Staples, healthcare and financials lead.
- **Funnel:** the morning screen ran 2984 symbols through to 997 liquid, 60 in the info pool and 25 candidates, which gave 4 morning recommendations. All 4 were re-checked this session and 3 remain recommendations (GCT is cancelled).
- **Book:** 2.17% invested (21.7 units) and 97.83% cash (978.3 units), against a notional base of 1,000 units. No holdings are recorded.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| CROX | buy-confirm | 0.95% | 9.5 | 155.0-158.5 | 148.8 | 178.9 | Overweight | 0.42 |
| HAS | trim (14.2 to 7.6 units) | 0.76% | 7.6 | 117.4-118.7 | 116.0 | 124.62 | Overweight | 0.40 |
| GMAB | trim (8.5 to 4.6 units) | 0.46% | 4.6 | 50.9-51.71 | 49.5 | 59.0 | Overweight | 0.35 |
| GCT | cancel | 0.00% | 0 | (61.8-62.0 watch only) | 55.8 | 71.3 | Hold | 0.40 |

All weights equal the engine weights. No PM adjustments were made.

## 3. Current holdings and morning orders
- `state/portfolio.json` has no positions, so there are no stop or target alerts on recorded holdings, and the risk officer raised no held alerts.
- **Fills against the morning zones today:**
  - **HAS:** the morning zone 119.0-121.0 was traded through (low 118.17). A resting morning limit order would have filled. The levels have now moved to stop 116.0 and target 124.62 (they were 116.7 and 132.1). At those levels, a fill above about 119.45 has R/R below the 1.5 minimum, and a fill at 120 has R/R of about 1.2. Any fill should be cut to 7.6 units. If the fill price is above 119.45, the owner may prefer to exit it entirely.
  - **CROX:** the morning zone 155.5-159.0 was touched (low 158.65). A fill near 159 has R/R of about 1.95 against 148.8 and 178.9, which is acceptable. The total should be 9.5 units, and the remaining units should rest only in 155.0-158.5.
  - **GMAB:** the morning zone 50.7-51.6 was also touched (open 50.99, low 50.86). Any fill should be cut to 4.6 units.
  - **GCT:** the morning zone 62.0-63.0 never filled (low 63.22). Cancel the order.
- The owner should record any fills in `state/portfolio.json` so that the next session treats them as held.

## 4. Theses
**CROX (buy-confirm, 9.5 units)**
- The 10/29 earnings re-rating is holding at 159.02 (net income +48.65% YoY, forward P/E 9.9), well above the 149.5 swing low and SMA20 145.42.
- R/R is about 2.8 from the zone midpoint and about 1.95 at the last price. The 178.9 target needs a breakout through 164.24, which has rejected price twice.
- Beta is 1.5, short interest is about 13% and debt/equity is 124 in a risk-off tape, so size stays small and entry is on pullbacks only.
- *Invalidation:* a daily close below 148.8, or a failed break above 164.24 that closes back under 160 on rising volume.

**HAS (trim, 7.6 units)**
- The stock is consolidating the 10/20 earnings re-rating (revenue +15% YoY, net income +69% YoY) in a 117.13-124.62 base, and beta of 0.36 suits the regime.
- Today's -1.9% pullback came on light volume with no news and held above the 117.13 swing low. R/R is about 2.2 at 118.71 and about 3.2 from the zone midpoint.
- The target is capped at the twice-rejected 124.62 high, the stop is only 0.86 ATR away and debt/equity is 410, so there is no extra size.
- *Invalidation:* a daily close below 116.0 (under the 117.13 swing low).

**GMAB (trim, 4.6 units)**
- The uptrend is strong (SMA50 41.88, SMA200 31.73), and today the stock recovered from 50.86 to 51.71, above SMA20 51.28. Healthcare leads the tape.
- R/R is about 3.3 to the 59.0 target, kept under the 59.97 52-week high.
- The 10/28 +28% gap is unexplained, the CEO and the commercial chief have sold shares, and the Nov 20 expiry is close, so the risk officer halved the size.
- *Invalidation:* a daily close below 49.5, or any close below the 50.68 swing low.

## 5. Rejected and vetoed
- **GCT (cancel):** downgraded to Hold. With the reset levels (stop 55.8, target 71.3), R/R is about 1.0 at 63.50, below the 1.5 minimum, and it has beta 1.6 in a tech-led sell-off. Re-check it only on a pullback to 61.8-62.0 that holds SMA20, or on a close above 67.40 on volume.
- The risk officer issued no vetoes. Reductions: GMAB x0.5 and CROX x0.75.

## 6. Data notes
- **CROX price field:** the engine sized from the 156.75 zone midpoint, not the 159.02 last price. The risk officer's x0.75 cut corrects for the wider real stop distance (about 6.4%).
- **GMAB stop and target:** research kept the morning stop of 49.5 and target of 59.0 rather than the technical card's 50.30 and 59.5, because the card's stop sits about 0.65 ATR from price and is likely to be hit by noise.
- **GMAB gap:** the cause of the 10/23 and 10/28 gaps is not in the packet, and the 6-K filings of 11/12 have no content.
- **HAS changes from the morning:** the stop moved from 116.7 to 116.0 and the target from 132.1 to 124.62. The morning measured-move target was replaced by the resistance level.
- **GCT data:**
  - The morning stop and target (57.7 and 72.0) could not be traced to packet levels and were reset.
  - About half of the GCT news items concern GCT Semiconductor (GCTS) and were excluded.
  - The sector is listed as Consumer Cyclical in the morning allocation and as Technology in candidates and research.
- **Session coverage:**
  - There was no bull/bear debate and no sentiment card this session.
  - Intraday volume is partial; prices are about 15 minutes delayed.
  - The regime-only refresh failed to download XLF (local cache lock); the morning `regime_view.json` was reused.
  - The next earnings dates for all four names are missing from the packet. They are estimated to fall outside the horizon.

This report is not investment advice; decisions and orders are the owner's.
