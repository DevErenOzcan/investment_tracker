# NASDAQ pre-close review — 2026-11-09

## Summary
- **Regime: risk-off** (confidence 0.9, unchanged from the morning): QQQ below its 50- and 200-day averages (21-day -12.24%), VIX 1-year percentile 0.876; defensives (XLV, XLP, XLRE) lead.
- **Review list:** 4 morning recommendations (morning funnel 2,986 → 25 candidates → 8 finalists → 4), no holdings. **What changed:** EXEL, AMPH and KDP ran above their entry zones without filling and were downgraded to Hold (reward/risk below 1.5), so they are cancelled; CRVL is confirmed at a slightly lower weight.
- **Invested weight 0.0092 (9.2 units), cash 0.9908 (990.8 units)** of the 1,000-unit notional base, versus 0.0247 / 0.9753 this morning. Engine weights are kept unchanged.

## Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| CRVL | buy-confirm | 0.0092 | 9.2 | 80.80–82.40 | 78.80 | 89.76 | Overweight | 0.46 |
| EXEL | cancel | 0 | 0 | 69.40–70.45 | 67.70 | 76.00 | Hold | 0.44 |
| AMPH | cancel | 0 | 0 | 28.50–28.80 | 27.35 | 31.00 | Hold | 0.40 |
| KDP | cancel | 0 | 0 | 35.60–36.10 | 34.18 | 38.92 | Hold | 0.40 |
| Cash | — | 0.9908 | 990.8 | — | — | — | — | — |

CRVL (last 82.32) is inside its zone; do not fill above 82.40. Morning versus afternoon: CRVL weight 0.0100 → 0.0092, stop 78.9 → 78.8, zone 81.5–83.2 → 80.8–82.4.

## Current holdings
No holdings are recorded in `state/portfolio.json` (1,000 cash units), so there are no stop or target alerts. The risk review raised no held-position alerts.

## Thesis
**CRVL** (Financial Services, insurance services)
- Uptrend intact (last 82.32 above SMA50 76.39 and SMA200 62.92), pulled back to a flat SMA20 at 82.33; revenue +11.5% and net income +22.2% YoY.
- Reward/risk about 2.1 from 82.32 to the 89.76 high against a 78.8 stop; no earnings until 2027-02-02.
- Capped at Overweight: today's push to 85.33 faded back to 82.32, lower closes since 2026-11-04, trailing P/E 34.6 after a 34.5% 63-day run, thin liquidity; the risk officer cut it x0.75 again.
- *Invalidation:* daily close below 78.8 (under the 79.19 swing low); a close below SMA50 (76.39) breaks the uptrend.

## Cancelled calls
- **EXEL:** ran to 71.555, above the morning 67.0–69.6 zone (RSI 70.2, 8.1% above SMA20); reward/risk about 1.15. Revives on a pullback into 69.4–70.45 while above 67.7.
- **AMPH:** ran to 29.48 (RSI 71.2, 10.5% above SMA20) against a 31.0 target that was already rejected; reward/risk about 0.71. Revives on a dip into 28.5–28.8 with no close below 27.35.
- **KDP:** the conditional 35.6–36.1 zone was never reached (today's low 36.27); reward/risk from 36.79 about 0.82. Revives on a dip into 35.6–36.1 or a confirmed breakout above 37.89; fundamentals still unverified (unexplained revenue step, today's 10-Q unreviewed).

**Vetoed by the risk officer:** none.

## Data notes
- **News feed blocked:** the news feed was still blocked by the network proxy, so `news_7d` is empty for every ticker. This is missing data, not proof that there were no events; it drove the CRVL reduction.
- Intraday prices are about 15 minutes delayed.
- SEC filing content (8-K/10-Q) was not reviewed; KDP's 10-Q filed today is unread.
- Afternoon technical cards changed several levels versus the morning (stops, targets and zones); the table uses the afternoon levels.
- `candidates.json` in this folder is a copy of the morning funnel; the universe was not re-screened.

This report is not investment advice; decisions and orders are the owner's.
