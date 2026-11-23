# NASDAQ premarket report: 2026-11-23

## 1. Summary
- **Regime:** risk-off (confidence 0.95). QQQ is below its 50- and 200-day averages (21-day -13.63%), VIX is 31.34 (1-year percentile 0.991), and only XLP, XLV and XLU hold above their 50-day. Engine regime multiplier is 0.4.
- **Funnel:** 2,977 universe → 993 liquid → 25 candidates → 8 finalists → 4 recommendations (all small Overweight buys).
- **Book:** 2.99% invested (29.9 units of 1,000) and 97.01% cash. All four names are one correlated defensive-healthcare bet.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| SIBN | buy | 1.05% | 10.5 | 23.20 - 23.80 | 22.55 | 25.92 | Overweight | 0.45 |
| AMPH | buy | 0.75% | 7.5 | 27.90 - 28.35 | 27.35 | 31.00 | Overweight | 0.37 |
| GMAB | buy | 0.65% | 6.5 | 50.40 - 51.30 | 49.40 | 57.30 | Overweight | 0.36 |
| CRVL | buy (limit ≤ 87.25, skip if not filled) | 0.54% | 5.4 | 86.50 - 87.25 | 81.60 | 95.90 | Overweight | 0.45 |
| Cash | | 97.01% | 970.1 | | | | | |

All weights equal the engine weights. No PM adjustment was made: the engine has already applied the risk-off multiplier and the risk officer's cuts (SIBN x0.75, AMPH x0.6, GMAB x0.5), and the regime gives no reason to size up.

## 3. Current holdings
No holdings (`state/portfolio.json` has 1,000 cash units and no positions). There are no stop or target alerts and no held alerts from the risk officer.

## 4. Theses
**SIBN (Overweight, 0.45)**
- Small-cap medtech re-rated after earnings (revenue +14.5% YoY, loss narrowing, net cash), pulling back in an orderly way to SMA20 (23.32) inside an uptrend with rs_63 +0.36.
- Buying 23.2-23.8 with a stop under the 22.72 swing low targets the 25.92 high, about 2.5 R/R at the 23.5 mid.
- Sized down for about 0.7M average volume (gap risk) and an unexplained CEO sale on 11/19.
- *Invalidation:* a daily close below 22.55.

**AMPH (Overweight, 0.37)**
- Uptrending specialty pharma (above SMA20/50/200, 63-day +31%) pulling back to SMA20 and the floor of its 28-29.7 range, on a forward P/E of 8.4.
- About 3.9 R/R from 28.1 to the 31.0 high against 27.35.
- Kept small because of 21.7% short interest, a 'Reduce' consensus with the price above the 24.5 mean target, and a stop only about 0.7 ATR away.
- *Invalidation:* a daily close below 27.35, or a close below SMA20 (about 28.0) on rising volume.

**GMAB (Overweight, 0.36)**
- Profitable, high-margin oncology royalty name (FCF 854.9M) digesting its late-October re-rating on fading volume (ratio 0.66) above a rising SMA50.
- About 4.4 R/R from 50.85 to 57.3, so positive expectancy even at a low hit rate.
- Lowest conviction in the book: lower highs and lower lows since 10/28, and a gap through 49.4 could run to the 44-45 gap-fill zone.
- *Invalidation:* a daily close below 49.4, which opens a gap-fill toward 43.98.

**CRVL (Overweight, 0.45)**
- High-quality, cash-rich compounder (revenue +11.5%, net income +22.2% YoY, cash 270M vs debt 33M) in a clean uptrend with rs_63 +0.377 and no event before 2027-02-02.
- **Limit entry at or below 87.25 only, skip if not filled:** R/R is 1.53 at 87.25 but about 1.14 at the 88.28 close, below the 1.5 floor.
- Kept small for a P/E of 37, the rejection at 90.71 and officer Form 144 sales near the high.
- *Invalidation:* a daily close below the 81.84 swing low (stop 81.6). A close below SMA20 (about 84.9) on rising volume is an early warning.

**Portfolio-level risk:** the four names are one correlated defensive-rotation bet (lessons item 8). A rotation out of XLV would hit all of them at once. Combined exposure is about 3%.

## 5. Rejected and vetoed
- **IDXX** (Hold): R/R is 1.28 at 676.21. It only works on a fill at or below about 668; recheck at pre-close.
- **IPAR** (Hold): R/R is about 0.9 at the last price, RSI is near 70, and Goldman's downgrade this morning is not yet in the price.
- **PLMR** (Hold): R/R is 1.40 at the close and 1.32 pre-market, below the 1.5 floor. Watch for a pullback into 159.5-162.5.
- **WMG** (Hold): R/R is under 1 at the close and pre-market quote, with high leverage in a risk-off tape. Watch only.
- Dropped at triage: XERS, SGRY, INSM, BRZE, NTSK, CRAI, EXPO, SLN, VRDN, ADMA, COLM, CROX, AXGN, ARHS, VERX, APPN, REPL. Reasons were over-extension (RSI or ext_20), binary event risk (SGRY, INSM), lagging tech sector, or broken setups.
- **Vetoed:** none.

## 6. Data notes
- **CRVL sector conflict:** the screener lists CRVL as Financial Services (Insurance Brokers), but research and the engine use Healthcare. This does not matter at these sizes. If the screener is right, healthcare exposure is slightly lower.
- Engine prices are the research entry midpoints, not the last closes. Last closes were SIBN 23.73, AMPH 28.25, GMAB 50.60 and CRVL 88.28. At the close, SIBN R/R falls to about 1.9 and CRVL to about 1.14.
- All news feeds are title-only RSS, and no sentiment cards were in the packets. GMAB's foreign-issuer filing feed is thin (SEC quarterly series empty).
- The next earnings date is unknown for SIBN, AMPH and GMAB (Q3 results were reported Nov 2-5, so none is likely inside the horizon). IDXX valuation data is null.
- `state/portfolio.json` has `as_of: null`; it was treated as an all-cash book of 1,000 units.

This report is not investment advice; decisions and orders are the owner's.
