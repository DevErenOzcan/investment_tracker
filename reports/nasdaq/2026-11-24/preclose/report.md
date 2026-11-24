# NASDAQ preclose report: 2026-11-24

## 1. Summary
- **Regime:** risk-off (confidence 0.85). QQQ is below its 50- and 200-day averages (21-day -7.58%), VIX is 29.99 (1-year percentile 0.981), and only 5 of 15 sectors are above their 50-day; XLY, XLP and XLU lead while SMH and XLK lag. Engine regime multiplier is 0.4.
- **Funnel:** morning 2,971 universe → 997 liquid → 25 candidates → 8 finalists → 5 recommendations; preclose re-check of those 5 → 1 kept (CROX, halved by the risk officer), 4 cancelled (PGNY, ASO, SIBN, AMPH).
- **Book:** 0.72% invested (7.2 units of 1,000) if the CROX limit fills, and 99.28% cash. No recorded holdings, but the morning PGNY and CROX limits may have partly filled (see section 3).

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| CROX | buy-confirm (resize to 7.2 units total, limit ≤ 157.00) | 0.72% | 7.2 | 154.50 - 157.00 | 152.50 | 164.24 | Overweight | 0.45 |
| PGNY | cancel (hold any morning fill) | 0.00% | 0 | re-entry 35.00 - 35.60 | 34.65 | 37.21 | Hold | 0.55 |
| ASO | cancel | 0.00% | 0 | re-entry 67.80 - 69.50 | 66.70 | 73.82 | Hold | 0.52 |
| SIBN | cancel | 0.00% | 0 | re-entry 23.69 - 23.86 | 22.50 | 25.92 | Hold | 0.50 |
| AMPH | cancel | 0.00% | 0 | re-entry 28.50 - 28.90 | 27.50 | 31.00 | Hold | 0.45 |
| Cash | | 99.28% | 992.8 | | | | | |

CROX weight equals the engine weight (0.0072, after the risk-officer x0.5); no PM adjustment. The morning CROX order was 13.0 units at up to 157.38. Cut it to 7.2 units total in 154.50-157.00 and cancel the 157.00-157.38 part. Any morning fill counts toward the 7.2. The engine gave 0 to the four cancelled names, so the PM cannot add weight to them. Re-entry zones are the analysts' levels for a future session, not orders for today.

## 3. Current holdings
`state/portfolio.json` shows 1,000 cash units and no positions, so there are no recorded stop or target alerts. Two morning limits may have filled without being recorded:

- **PGNY: possible fill at 35.39-35.60.** Today's low of 35.39 touched the 35.00-35.60 zone, so only limits at 35.39-35.60 could have filled, up to the morning 12.6 units. The 35.30 midpoint did not trade.
  - **If filled:** hold. Use the 34.65 stop (not hit; the low was 35.39) and the 37.21 target (not hit; the last was 36.49). R/R from a fill is about 1.7-2.5.
  - **Alert:** the target is only about 0.65 ATR above the last price, RSI is 70.5 at the 52-week high, and the next earnings date is unconfirmed. A reversal is plausible, so do not add.
  - **Exit:** a daily close below 34.65, or below SMA20 (about 33.90) on rising volume.
- **CROX: possible fill at 157.24-157.38.** Today's low of 157.24 touched the top of the 155.00-157.38 zone, so it may have filled, up to the morning 13.0 units.
  - **Stop:** moves from the morning 152.80 to 152.50 (not hit). The target is 164.24 (the last was 157.815). R/R from that fill is only about 1.41-1.48, under the 1.5 minimum.
  - **If the fill is 7.2 units or more:** do not add. Trimming the excess down to 7.2 units would match the engine weight; that is the owner's call.
  - **If the fill is smaller:** the rest of the 7.2 units can only be bought inside 154.50-157.00.
  - **Exit:** a daily close below 152.50.
- **Exposure:** if both fills were full, unrecorded exposure is up to 25.6 units (12.6 PGNY + 13.0 CROX). The engine's sizing, sector and cash checks did not include it. The owner should record any fill (units and entry price) in `state/portfolio.json` before the next run.
- **Other orders:** ASO (low 69.96), SIBN (low 24.74) and AMPH (low 29.61) stayed above their zones, so those orders did not fill.

## 4. Theses
**CROX (buy-confirm, limit only)**
- Cheap (forward P/E 9.86) with accelerating earnings (net income +48.7% YoY), consolidating in a 150-164 base above SMA20 155.07 after the 10/29 earnings gap, in XLY, a leading sector.
- No earnings before 2027-02-11 and no offering filings. R/R is 2.61 at the 155.75 midpoint and 1.61 at 157.00, but only about 1.21 at the 157.815 last, so do not chase.
- Size halved: the stop is only about 0.6 ATR below entry in a gap-prone risk-off tape, supply sits at 163-164, volume is light (ratio 0.73) after a +33% 21-day run, and the leverage and margin-squeeze headlines were not re-checked.
- *Invalidation:* daily close below 152.50 (under the 152.78 Nov 5 low and the 153.92 10-day swing low).

**PGNY (cancel; hold any fill)**
- Uptrend and post-earnings re-rating intact (36.49 above SMA20 33.90, SMA50 29.74, SMA200 25.29), with no new negative news.
- The entry ran away: the stock bounced 2.7% to within 1.9% of the 37.21 target, and R/R is about 0.39 at the last price.
- New buying only in 35.00-35.60 (R/R at least 1.5 up to about 35.67). The technical card's 35.4-36.0 zone gives only about 1.44 and is not used.
- *Invalidation:* daily close below 34.65, or below SMA20 (about 33.90) on rising volume.

**ASO (cancel)**
- Uptrend and XLY leadership intact, but there is no company-specific catalyst. The stock rallied 4.3% to 72.28 and never reached the zone (low 69.96).
- R/R is about 0.28 at the last price against the 66.70 stop and 73.82 target (the reversed Nov 18 high). It is above the 63.58 mean analyst target, and short interest is 19.9%.
- Earnings on 2026-12-08 fall inside the window: any future entry needs a dip into 67.80-69.50 and an exit by the 2026-12-07 close.
- *Invalidation:* daily close below 66.70 (under SMA20 near 67.2), or a failed retest of 73.82 followed by lower closes.

**SIBN (cancel)**
- Post-earnings uptrend intact (25.32 above SMA20 23.69), with a reimbursement tailwind in place, but the technical card now finds no setup.
- Target cut from 27.50 to the 25.92 52-week high and stop moved to 22.50. R/R is about 0.21 at the last price.
- Reopens only on a pullback to about 23.86 or lower (near SMA20) or on a volume-confirmed close above 25.92.
- *Invalidation:* daily close below 22.50 (under the 22.72 Nov 18 swing low), or below SMA20 (about 23.69) on rising volume.

**AMPH (cancel)**
- Fundamentals are solid (revenue +8.2% YoY, forward P/E 8.9), but the stock faded from 30.57 to 29.76, a second rejection under the 31.00 high.
- Target cut to 31.00 and stop moved to 27.50. R/R is about 0.55 at the last price and reaches 1.5 only at or below 28.90.
- Sell-side consensus is Reduce (mean target 24.5), the CFO is selling, and the short float is 21.7%.
- *Invalidation:* daily close below 27.50, or a second rejection at 30.5-31.0 followed by a close under SMA20 (about 28.42) on rising volume.

## 5. Rejected and vetoed
- **PGNY:** rejected by the engine, rating Hold (entry ran away, R/R about 0.39 at the last price).
- **ASO:** rejected by the engine, rating Hold (entry ran away, R/R about 0.28, earnings inside the window).
- **SIBN:** rejected by the engine, rating Hold (entry ran away, target capped at 25.92, R/R about 0.21).
- **AMPH:** rejected by the engine, rating Hold (rejection under 31.00, R/R about 0.55).
- **Risk-officer vetoes:** none. One reduction: CROX x0.5 (unknown real exposure, thin R/R away from the midpoint, tight stop, headlines not re-checked).

## 6. Data notes
- **Unrecorded fills:** the main data gap. `state/portfolio.json` may understate real exposure by up to 25.6 units, so the engine's cash, sector and correlation checks may be too lenient.
- **Debate skipped:** the bull/bear debate was skipped for all five names (preclose procedure; no rating moved two notches). Judgement rests on the technical and news cards only.
- **CROX:** the leverage and footwear margin-squeeze headlines were not re-verified in this packet.
- **Levels changed since the morning:** CROX stop 152.80 → 152.50; SIBN target 27.50 → 25.92 and stop 22.65 → 22.50; AMPH target 32.16 → 31.00 and stop 27.60 → 27.50; ASO target 73.80 → 73.82.
- **Missing earnings dates:** next earnings for PGNY and AMPH are not in the packet. PGNY's catalyst is still inferred from price and SEC data only.
- **Sector labels:** ASO is now labelled Consumer Cyclical (morning: Consumer Discretionary), so it is grouped with CROX in the XLY bucket. No limit is affected at these sizes.
- **Sources:** the funnel counts come from the morning report (the preclose run does not screen the universe).
- **Prices:** intraday prices are about 15 minutes delayed, and volume figures are partial-day. Fill prices inside the touched zone edges are uncertain.

This report is not investment advice; decisions and orders are the owner's.
