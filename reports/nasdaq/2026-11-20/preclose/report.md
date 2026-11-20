# NASDAQ preclose review: 2026-11-20

## 1. Summary
- **Regime:** risk-off (confidence 0.93). QQQ is below its 50/200-day averages (ret_21 -11.05%) and VIX is 31.37 (percentile 0.995). XLP, XLV and XLU lead; SMH, XLK and XLE lag.
- **Funnel:** morning 2,971 screened → 995 liquid → 25 candidates → 8 finalists → 4 morning recommendations. At preclose, 3 are confirmed (ADMA, CROX, AZTA) and 1 is cancelled (PGNY).
- **Book:** 2.31% invested (23.1 of 1,000 units) and 97.69% cash, which is well above the 10% minimum. All weights equal the engine weights; the PM made no adjustments.

## 2. Actions

| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| ADMA | buy-confirm | 1.15% | 11.5 | 12.90-13.25 | 12.40 | 15.90 | Overweight | 0.40 |
| CROX | buy-confirm | 0.72% | 7.2 | 151.50-155.00 | 148.00 | 179.00 | Overweight | 0.37 |
| AZTA | trim (6.1 → 4.4 units) | 0.44% | 4.4 | 44.00-45.20 | 42.90 | 50.06 | Overweight | 0.35 |
| PGNY | cancel | 0.00% | 0.0 | (34.90-35.60 re-entry) | 33.10 | 39.45 | Hold | 0.40 |
| Cash | - | 97.69% | 976.9 | - | - | - | - | - |

Changes from the morning ticket:
- ADMA goes from 11.0 to 11.5 units, with a slightly lower zone.
- CROX goes from 5.9 to 7.2 units, with a lower zone and the stop moved from 148.5 to 148.0.
- AZTA goes from 6.1 to 4.4 units, with a re-based zone and the target cut from 56.9 to 50.06.
- PGNY is cancelled (9.4 units back to cash).

All entries are limit-in-zone only.

## 3. Current holdings and near-stop alerts
`state/portfolio.json` shows 1,000 cash units and no positions, so no held stops or targets are active. The risk officer raised no held alerts. These recommendations have a last price close to their stop:
- **AZTA (closest):** last 44.815 vs stop 42.90, which is 4.3% away or about 0.65 ATR (ATR 2.93). The intraday low was 44.20. A loss of 43.15 on rising volume is the early warning.
- **CROX:** last 154.43 vs stop 148.00, which is 4.2% away or about 1.1 ATR (ATR 5.87). Options expiry today may distort the close.
- **ADMA:** last 13.15 vs stop 12.40, which is 5.7% away or about 1.2 ATR. The stop now equals the rising 20-day SMA (12.40).
- **PGNY (cancelled):** last 35.855 vs stop 33.10, which is 7.7% away and not near.

Portfolio-level alert: today is Friday and monthly options expiry. All three are post-earnings pullback longs with stops 0.6-1.2 ATR away. A weekend gap could hit every stop at Monday's open together, and ADMA and AZTA are one correlated healthcare bet.

## 4. Theses

**ADMA (1.15%, buy-confirm)**
- A profitable, cash-generative biotech (forward P/E 14.2) in an uptrend above SMA20/50/200. Healthcare still leads in this risk-off tape.
- The last price of 13.15 is inside 12.90-13.25 on light volume (ratio 0.78), with no new news or filings. R/R is about 3.7 from the last price to 15.9.
- The target needs a break of 14.2, which has CEO/director sales nearby and gives only about 1.4 R/R. The risk officer kept the x0.75 cut for the unverified short-seller headline.
- *Invalidation:* a daily close below 12.40 (under the 12.48 swing low and the 20-day SMA), especially on rising volume.

**CROX (0.72%, buy-confirm)**
- The 10/29 post-earnings gap is holding in a stacked uptrend. Net income is +48.65% YoY and forward P/E is 9.8. It is the only non-healthcare name.
- The fade from about 157.2 to 154.43 came on light volume (ratio 0.85) with no negative news, so the price is in the 151.5-155.0 zone. R/R is about 3.8 from the last price.
- Three failures at 164.24 (about 1.5 R/R to there, so scale out there), leverage (D/E about 124) with ^TNX near 4.98% and beta 1.5 led the risk officer to keep the x0.5 cut.
- *Invalidation:* a daily close below 149.0 (the 10/30 and 11/6 swing lows); the stop is 148.0.

**AZTA (0.44%, trim vs the morning ticket)**
- The fiscal Q4 beat gap (40.48 to 48.90) and the net-cash balance sheet still support the trend: 44.815 is above SMA20 41.95, SMA50 38.12 and SMA200 28.73.
- The pullback went past the morning zone (46.10 open, 44.20 low) on a -4.8% day with no news while XLV held. The target is cut to the 50.06 52-week high, so R/R is about 2.7 from the last price.
- High beta (1.47), 21.7% short interest, forward P/E 52.9, the Nov 30 conference and an unreviewed 10-K keep the size small, and confidence fell from 0.38 to 0.35.
- *Invalidation:* a daily close below 42.9, which fills the 11/11 earnings gap. An intraday loss of 43.15 on volume is the early warning.

## 5. Cancelled, rejected and vetoed
- **PGNY (cancel, Hold):** the price bounced to 35.855, above the zone, so R/R at the last price is about 1.30, below the 1.5 floor. The engine rejected it as Hold. This is a mechanical downgrade, and the thesis is not broken. *Re-entry condition:* a pullback into 34.90-35.60 with the stop at 33.10 (R/R about 1.95 at the 35.25 mid), confirmed by a fresh engine weight at the next session. The setup is void on a daily close below 33.34.
- **Morning rejects** (AMPH, ASO, COLM, CRAI, all Hold): unchanged and not re-assessed.
- **Vetoed:** none. The risk officer kept its reductions only (ADMA x0.75, CROX x0.5, AZTA x0.5).

## 6. Data notes
- **Morning zones that traded:** the AZTA morning zone (45.0-46.8) and the ADMA and CROX morning zones traded today. If the owner already placed the morning orders, they may be filled at the morning sizes. In that case AZTA is a trim from 6.1 to 4.4 units, and the CROX stop should move to 148.0.
- **PGNY fill:** it is not known whether the PGNY morning zone (34.60-35.50) traded before the bounce. If a fill happened, treat it as a held Hold with stop 33.10, not a new add.
- **ADMA short interest:** the morning 10.04% figure is null in the preclose packet, so it is unverified. The short-seller mention is still a title only.
- **News and filings:** news is RSS titles only for all names. The AZTA 10-K filed 2026-11-19 has not been reviewed.
- **Earnings dates:** next earnings dates for ADMA, PGNY and CROX are missing. They are estimated to fall outside the 10-day horizon.
- **Partial volume:** intraday volume is partial (AZTA 342k vs 1.04M average; CROX about 0.57M), so today's drops are not confirmed.
- **Bull/bear debate:** skipped for every name in this preclose re-assessment (no rating moved by two notches).
- **Regime data:** the preclose regime refresh could not fetch ^TNX; the morning regime view was reused.
- **Sector labels:** CROX is labelled "Consumer Discretionary" in research and "Consumer Cyclical" in candidates. The sector cap is not binding.
- **Portfolio state:** `state/portfolio.json` has `as_of: null`, and no preclose `candidates.json` exists, so the funnel shown is the morning one.

This report is not investment advice; decisions and orders are the owner's.
