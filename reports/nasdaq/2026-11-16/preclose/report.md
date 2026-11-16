# NASDAQ pre-close review, 2026-11-16

## 1. Summary
- **Regime:** risk-off (confidence 0.65). QQQ is below its 50- and 200-day averages (ret_21 -6.6%). Healthcare, staples and financials lead; semis and tech lag. ^TNX is at the 0.914 percentile.
- **Funnel:** 2982 screened → 1004 liquid → 25 candidates → 6 morning picks re-assessed → 3 confirmed (HAS, PLMR, GMAB) and 3 cancelled (EXEL, CDNA, ASO).
- **Book:** 0.0243 invested (24.3 units), 0.9757 cash (975.7 units). All three engine weights are kept unchanged. Each is lower than this morning because of the risk-officer cuts.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| HAS | buy-confirm | 0.0105 (am 0.0177) | 10.5 | 118.0-120.0 | 116.85 | 127.77 | Overweight | 0.45 |
| PLMR | buy-confirm (limit, zone only) | 0.0083 (am 0.0111) | 8.3 | 155.5-159.0 | 150.9 | 175.0 | Overweight | 0.40 |
| GMAB | buy-confirm | 0.0055 (am 0.0066) | 5.5 | 50.7-52.0 | 49.6 | 59.5 | Overweight | 0.37 |
| EXEL | cancel | 0 (am 0.0071) | 0 | - | - | - | Hold | 0.32 |
| CDNA | cancel | 0 (am 0.0058) | 0 | - | - | - | Underweight | 0.30 |
| ASO | cancel | 0 (am 0.0049) | 0 | - | - | - | Hold | 0.36 |

If any morning order already filled above the new weight, trim it to the weight shown.

## 3. Current holdings
`state/portfolio.json` shows no positions and all cash, so no stops or targets are live. The risk officer raised no held-position alerts. One alert applies only to fills not yet recorded: if CDNA was filled this morning (premarket 76.85 was inside its zone), last 74.36 is already below the 74.9 morning stop, so exit it. If EXEL was filled, keep the 66.8 stop, which is only 0.37 ATR away.

## 4. Theses
**HAS (Overweight, 0.45).** This is a post-earnings pullback after the 2026-10-20 Q3 beat and raised guidance (revenue +15% YoY). Last 119.945 is inside the zone and on SMA20 (118.85), above the 117.13 base. R/R is 2.5 at the last price, but only about 1.5 to the 124.62 high, which has rejected price twice, so take partial profit there. Four lower closes in a risk-off tape limit the size.
*Invalidation:* a daily close below 117.13. The hard stop is 116.85, and the 109.5-114 gap zone below it is a gap-through risk.

**PLMR (Overweight, 0.40).** A low-beta (0.24) specialty P&C insurer in a leading sector (XLF). Revenue is +58% YoY at a forward P/E of 13.7, and it has held the Nov 5 earnings gap for 7 sessions. It is extended (RSI 71, 8.3% above SMA20) and was rejected at 162.38 intraday. Last 159.82 is above the zone, where R/R is about 1.7, so this is a limit-only entry at 155.5-159.0 (zone R/R 2.8).
*Invalidation:* a daily close below 151.5. A close under SMA20 (about 147.6) would confirm the breakout has failed.

**GMAB (Overweight, 0.37).** A healthcare leader (rs_63 +0.65) pulling back after the October spike. Last 51.875 is inside the zone and above SMA20 (50.66), and today's low of 51.78 held above the 50.68 swing low on light volume. R/R is about 3.4 to 59.5 and about 2.4 to 57.06 resistance. This is a starter size only, because the spike driver is unexplained, insiders are selling and the stop is only about 1.0 ATR away.
*Invalidation:* a daily close below 49.6, or below SMA20 (about 50.7) on rising volume. Either opens a move toward the 44.7-45.4 gap.

## 5. Rejected and vetoed
- **EXEL:** cut to Hold. It lost SMA20 (68.20), the stop is 0.37 ATR away and an undated binary FDA decision on zanzalintinib is pending.
- **CDNA:** cut to Underweight after the bear won the debate. Last 74.36 broke the 74.9 morning stop and SMA20 (77.13). It can be re-rated only if it reclaims 77.13 on volume.
- **ASO:** cut to Hold. The morning zone never filled (low 68.13), and R/R at 69.77 is 1.33, below the 1.5 floor. It stays on a pullback watch for 67.8-69.0, and any position must be closed before the 2026-12-08 earnings.
- **Risk-officer vetoes:** none. The risk officer cut sizes instead: GMAB x0.5, HAS x0.75, PLMR x0.75.

## 6. Data notes
- Intraday prices are about 15 minutes delayed and the close is not final. CDNA's stop breach and PLMR's position above its zone could change by the close.
- `earnings_date` is null in research for all three buys, so the engine did not check the earnings blackout. The candidates file shows the last reports as HAS 2026-10-20, PLMR 2026-11-04 and GMAB 2026-11-05, so a report within 3 days is unlikely. GMAB's next date should still be confirmed before a fill.
- HAS news was Yahoo only because Google RSS was rate-limited. GMAB news has nothing after 2026-11-13, and its SEC quarterly series is empty. The content of PLMR's 2026-11-12 8-K Item 7.01 is unverified.
- The risk officer reviewed from `research/*.json` only (it could not list `cards/`). The technical, news and fundamentals cards for all six tickers exist under `cards/` and match the research levels, so the review's conclusions stand.
- The "healthcare-heavy book" risk cited for GMAB, EXEL and CDNA refers to the decision log, not actual holdings. Confirmed healthcare weight is 0.0055.
- Partial-day volume figures (vol_ratio) are not comparable with full sessions.

This report is not investment advice; decisions and orders are the owner's.
