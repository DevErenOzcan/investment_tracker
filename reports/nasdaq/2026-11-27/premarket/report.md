# NASDAQ pre-market report: 2026-11-27 (half day, early close 13:00 ET)

## 1. Summary
- **Regime:** risk-off (confidence 0.9). QQQ is below its 50- and 200-day averages, 21-day -12.11%, VIX 25.44 (1y percentile 0.90). Staples, health care and real estate lead; tech and semis lag. The engine applied a regime multiplier of 0.4.
- **Funnel:** universe 2,968 → with history 2,858 → liquid 996 → info pool 60 → candidates 25 → finalists 8 (IDXX, PGNY, GMAB, IPAR, PLMR, CROX, AZTA, AMPH) → recommendations 2 (PGNY, AMPH).
- **Exposure:** 1.36% invested (13.6 of 1,000 units), 98.64% cash. Both names are healthcare, so this is one small defensive bet.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| PGNY | buy (dip-only limit) | 0.95% | 9.5 | 35.50-36.30 | 34.80 | 39.40 | Overweight | 0.40 |
| AMPH | buy (limit at or below 28.80) | 0.41% | 4.1 | 28.50-28.80 | 27.55 | 31.00 | Overweight | 0.45 |
| Cash | - | 98.64% | 986.4 | - | - | - | - | - |

Both weights are the engine's own figures after the risk-officer reductions. I made no PM adjustment, because the regime does not justify adding size. Neither entry should be chased. Because of the 13:00 ET early close, any unfilled limit lapses with the session.

## 3. Current holdings
- No positions are held (`state/portfolio.json`: 1,000 cash units, peak 1,000, drawdown 0.0%). There are no stop or target alerts.
- **Timing alert:** the 14:52 ET pre-close review runs after today's 13:00 ET close. It cannot re-assess fills or intraday prices for this session. The "re-assess at pre-close if price pulls back" conditions on the Hold names (IDXX, IPAR, PLMR, CROX) therefore move to the next premarket run.

## 4. Theses
**PGNY (Overweight, 0.40)**
- Profitable and cash-generative, with YoY revenue growth accelerating (1.4% → 5.3% → 8.9%). FCF is 195.1M against 25.9M of debt.
- It has held its 11-05 earnings gap in a 3-week 34.94-37.21 base (rs_63 0.52), in health care, which leads the risk-off tape.
- It is extended (RSI 68.7, +31% in 21 days, near the 37.75 mean analyst target), so it is a dip entry only. R/R is about 3.2 at 35.9 and about 2.1 at 36.3. Consider partial profits at 37.21.
- *Invalidation:* a daily close below 34.80, or a failed push through 37.21 that closes back below 36.0 on above-average volume.

**AMPH (Overweight, 0.45)**
- A post-earnings re-rated uptrend above SMA20/50/200 (63-day +33%), consolidating in a 28-30 range.
- Q3 revenue was +8.2% YoY and net income +117.7%, in a health-care name while XLV leads.
- R/R is about 1.20 at the 29.12 last close, but 1.76 at 28.80 and about 2.4 near 28.55. Hence limit-only and half size. Risks: 21.5% short interest, leverage, price above the 24.5 mean analyst target.
- *Invalidation:* a daily close below 27.55 (under the 27.79 10-day swing low).

## 5. Rejected and vetoed
- Risk-officer vetoes: none. Reductions: PGNY x0.75, AMPH x0.5.
- IDXX: Hold. R/R about 1.22 at the last close; it only works on a pullback to about 696-705.
- GMAB: Hold. The target needs a breakout above 59.97 on a 0.77 volume ratio; R/R about 1.19 at the last close.
- IPAR: Hold. R/R 1.15 at the last close, RSI 73.5, price above the mean target, Goldman downgrade on 11-23.
- PLMR: Hold. The last price of 167.74 is above the 162.5-165.0 zone (R/R about 1.17), RSI 74.1.
- CROX: Hold. Pre-market 161.44 is above the zone (R/R 1.41), beta 1.5 in a risk-off tape.
- AZTA: Hold. First resistance gives about 1.3 R/R, ATR 6.2%, high beta, gap-reversal history.

## 6. Data notes
- **Sector label mismatch:** the engine labelled PGNY "Healthcare" and AMPH "Health Care". In allocation.json both are normalized to "Healthcare". Combined they are 1.36%, far below the 30% sector cap, so this did not bind, but the engine's sector map should be normalized.
- Many candidates came in with `sector: null` (for example UPBD, NTSK, GDYN, CRCT, COLM, VCEL, ASO). PGNY's sector was assigned from its business description.
- Triage first ran before `regime_view.json` existed and was rerun with it. The finalists above come from the rerun.
- The causes of the earnings gaps for PGNY and IDXX are inferred, not sourced. GMAB's SEC quarterly series was empty. AZTA's 10-K (filed 2026-11-19) has not been reviewed.
- Half-day session: thin liquidity makes fills and stops less reliable, and the pre-close review cannot act today (see section 3).
- `state/portfolio.json` has `as_of: null`. No holdings are recorded.

This report is not investment advice; decisions and orders are the owner's.
