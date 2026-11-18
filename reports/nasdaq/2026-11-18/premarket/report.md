# NASDAQ premarket report, 2026-11-18

## 1. Summary
- **Regime:** risk-off (confidence 0.85). QQQ is below its 50- and 200-day averages with a 21-day return of -8.55%, VIX is at its 0.905 one-year percentile and ^TNX is 5.115. Defensives (XLP, XLV) and XLF lead.
- **Funnel:** 2,976 screened → 997 liquid → 25 candidates → 8 finalists researched → 4 recommendations (1 vetoed, 3 rated Hold).
- **Allocation:** 3.46% invested (34.6 units of a 1,000-unit notional book) and 96.54% cash. All weights are the engine weights unchanged.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| GMAB | buy | 0.72% | 7.2 | 50.90-52.00 | 49.90 | 57.30 | Overweight | 0.40 |
| CROX | buy (pullback only) | 0.93% | 9.3 | 154.50-158.50 | 148.80 | 178.98 | Overweight | 0.42 |
| AZTA | buy (pullback only) | 0.83% | 8.3 | 44.20-45.29 | 42.85 | 50.06 | Overweight | 0.40 |
| AMPH | buy (pullback only) | 0.98% | 9.8 | 28.30-29.00 | 26.95 | 32.50 | Overweight | 0.42 |
| Cash | | 96.54% | 965.4 | | | | | |

Healthcare totals 2.53% (GMAB, AZTA, AMPH), well under the 30% sector cap, but see the correlation note below.

## 3. Current holdings
None. `state/portfolio.json` shows no positions, so there are no stop or target alerts. The risk officer raised no held-position alerts.

## 4. Theses
**GMAB (Overweight, 0.40)**
- Uptrend above SMA20/50/200 with RS63 +0.60. It is pulling back to SMA20 on fading volume after the 10/28 gap-and-run.
- Profitable, low-beta (0.52) biotech in XLV, the sector leading this risk-off tape. R/R is about 3.8 from 51.45.
- Cut x0.5 by the risk officer: the spike catalyst is unverified, the CEO and board sold on 11/12, and highs have been lower since 11/9.
- *Invalidation:* a daily close below 50.68 (stop 49.9). That opens a gap-fill toward 44-45.

**CROX (Overweight, 0.42)**
- Re-rated on the 10/29 Q3 print and has held the 149.5 base while QQQ fell. Earnings are accelerating and the forward P/E is about 9.9.
- R/R is 2.9 from the 156.5 mid toward 178.98. The 164.24 52-week high, rejected on 11-16, is about 1R overhead.
- Cut x0.7: it is extended (+32% in 21 days, RSI 66) and has beta 1.5 and rate sensitivity while yields rise. Last price 158.79 is above the zone.
- *Invalidation:* a daily close below 149.5, or a failure back under the 150 gap area on rising volume.

**AZTA (Overweight, 0.40)**
- The post-earnings gap (revenue beat, FY2027 guidance, gene-synthesis deals, insider buying) is holding above the pre-earnings 40.5 level.
- Net cash and no scheduled catalyst before 2027-02-03. R/R is about 2.8 at the 44.75 mid. The zone top was trimmed to 45.29 to keep R/R above 1.5.
- Cut x0.75: the gap already faded from 50.06, the stop is about 0.66 ATR away, valuation is rich (forward P/E 51.5) and short interest is 21.7%. Last price 45.81 is above the zone.
- *Invalidation:* a daily close below 43.15. A close below about 40.5 fills the gap.

**AMPH (Overweight, 0.42)**
- Clean stacked uptrend (close above SMA20 > SMA50 > SMA200) digesting the 11-05 Q3 beat on fading volume. Forward P/E is about 8.7.
- R/R is 2.26 to 32.5 from the 28.65 mid. The first leg to the 31.00 high is only about 1.38, so treat 31.00 as the partial-profit zone.
- No risk-officer cut, but price is above the mean analyst target and short interest is 21.7%. Last price 29.10 is above the zone.
- *Invalidation:* a daily close below 27.09. A close below 26.95 voids the setup.

**Portfolio note:** three of the four names are healthcare, so they are largely one correlated bet on XLV leadership (lessons item 6). If the regime rotates, they could stop out together.

## 5. Rejected and vetoed
- **SEZL (vetoed):** beta 6.6 and 23% short float in a risk-off tape, with the stop about 0.7 ATR below entry so a gap through it is likely. The 11-12 DEFA14A has not been checked.
- **ASO (Hold):** R/R about 1.26 at mid, below the 1.5 floor. Price is above the mean analyst target and there is no sourced catalyst.
- **CHA (Hold):** R/R about 1.1. Earnings (11-27) and a special-dividend ex-date of unknown timing both fall inside the window.
- **VTRS (Hold):** R/R 1.33 at mid with 21.20 resistance overhead. The 11-17 8-K (Item 2.01) has not been read.

## 6. Data notes
- CROX, AZTA and AMPH last traded above their entry zones (158.79, 45.81 and 29.10). Fills are uncertain, and filled and unfilled entries should be logged (lessons item 2). GMAB (51.96) is inside its zone.
- The engine `price` is the zone-midpoint entry, not the last trade. R/R at last price is lower: CROX about 2.0 and AMPH about 1.58.
- GMAB: the catalyst behind the 10/05-10/28 jumps is unverified and the SEC quarterly series is empty, so growth is unverified.
- CROX: the packet has no guidance detail and there is no sentiment card (Phase 3 not active).
- Unread filings: SEZL DEFA14A (11-12) and 8-K 7.01 (11-10); VTRS 8-K 2.01 (11-17).
- CHA: the SEC quarterly series is empty and the 52-week-high fields conflict between sources.
- CRCT has a null sector and industry in the candidate list.
- Yahoo Finance returned HTTP 401/429 errors for part of the info fetch during screening; a few fields may be missing.

This report is not investment advice; decisions and orders are the owner's.
