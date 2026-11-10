# NASDAQ premarket report: 2026-11-10

## 1. Summary
- **Regime:** risk-off (confidence 0.8). QQQ is below its 50- and 200-day averages with a 21-day return of -9.57%. SMH (-19.21%) and XLK (-14.04%) lead the decline. Money is rotating into health care (XLV 21-day +10.26%), staples and consumer discretionary.
- **Funnel:** universe 2986 → with history 2866 → liquid 1000 → candidates 25 → finalists 8 → recommendations 3 (all Overweight, all Healthcare).
- **Allocation:** 0.0178 invested (17.8 of 1000 notional units) and 0.9822 cash (982.2 units). All engine weights are kept unchanged, with no PM adjustment.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| EXEL | buy (limit, new) | 0.0084 | 8.4 | 69.60-71.30 | 67.80 | 76.00 | Overweight | 0.45 |
| AMPH | buy (limit, new) | 0.0061 | 6.1 | 27.90-28.50 | 26.60 | 31.00 | Overweight | 0.45 |
| LFST | buy (limit, new) | 0.0033 | 3.3 | 14.00-14.40 | 12.85 | 17.00 | Overweight | 0.40 |
| Cash | - | 0.9822 | 982.2 | - | - | - | - | - |

All three are limit entries in the pullback zone only. The last closes (EXEL 71.74, AMPH 29.38, LFST 14.60) are above their zones. If price does not trade into a zone, take no position. Weights reflect the engine's risk-off multiplier (0.4), the Overweight conviction multiplier (0.6) and the risk-officer reductions (EXEL x0.75, AMPH x0.75, LFST x0.5).

## 3. Current holdings
- No positions are held (`state/portfolio.json` is empty, 1000 cash units). There are no stop or target alerts and no held-position alerts from the risk review.

## 4. Theses
**EXEL** (Overweight, 0.45)
- Cash-generative biotech (operating margin 0.41, FCF 759M vs debt 162M) in a strong uptrend (63-day +39.8%, RS +0.45) in the leading health care group.
- The stock is extended (RSI 70.5, 8.3% above SMA20) and was rejected at 73.69 on 11-05. It trades above the 61.57 mean analyst target and short interest is 15.3%.
- The trade is a dip entry for a 2.09 reward/risk to 76.0.
- *Invalidation:* a daily close below 67.80, or a failed break above 73.69 on heavy volume followed by a close back under 68.

**AMPH** (Overweight, 0.45)
- Post-earnings uptrend (revenue +8.2% YoY, net income +118% YoY) at low multiples (forward P/E 8.835, EV/EBITDA 8.643).
- Reward/risk is a modest 1.75. The target sits at the 31.0 rejection wick, price is above the 24.5 mean analyst target, short interest is 22.08%, and liquidity is thin.
- The health care rotation is the tailwind. Do not chase.
- *Invalidation:* a daily close below 26.60, or a close back below the 11-06 low of 27.80 that fails to recover.

**LFST** (Overweight, 0.40)
- Uptrend backed by operating improvement: revenue +25.3% YoY with three sequential increases, and positive net income and FCF.
- The 11-09 move (+6% on about 6x average volume) has no verified driver. Overhead supply sits at 15.66, valuation is rich (trailing P/E 81.1) and the stop is the widest of the three (9.51%).
- Reward/risk is 2.07 to 17.0. The target needs a breakout above 15.66.
- *Invalidation:* a daily close below 12.94, or a heavy-volume close under the 13.20 11-09 low. The 12.94 level sits above the 12.85 engine stop, and the risk officer recommends that the tighter level governs exits.

**Portfolio note:** all three are the same trade, extended health care momentum riding a defensive rotation. A reversal of that rotation would hit all of them together. Combined exposure is 0.0178, far below the 0.30 sector cap.

## 5. Rejected and vetoed
- **Risk-officer vetoes:** none. Reductions were applied as listed in section 2.
- **CDNA**, Hold (0.38): a beta-2.49 growth name in a risk-off tape. The target needs a breakout above the 90.87 high, and offering risk cannot be checked.
- **APPN**, Hold (0.40): the post-earnings gap is fading after the 56.38 rejection. Reward/risk is thin (1.77 at mid-entry) and valuation is rich.
- **AMPL**, Hold (0.40): the target is a failed-breakout level (18.85), reward/risk is 1.59 at mid-entry, and it is a loss-making growth name in a weak tech tape.
- **FLYW**, Hold (0.42): extended (RSI 71.4), reward/risk is about 1.3 at the top of the zone, and an 8-K item 5.02 management-change flag is unresolved.
- **VERX**, Hold (0.40): an unexplained Q3 net loss of -46.6M, a wide stop (about 11% loss), leverage, and extended (RSI 72.3).
- **Dropped at triage** (17 names): HTFL, KOD, SLN and GO were inside the earnings blackout. The other 13 (XERS, SIBN, CYRX, SGRY, ASO, ARHS, REPL, GDYN, VIR, SDGR, XNCR, CRCT, BSY) were over-extended on RSI or ext_20.

## 6. Data notes
- **The news feed was unavailable this run.** All headline lists were empty, and the SEC filing list was also empty for EXEL and CDNA. Event risk was therefore not checked: offerings, secondary sales, analyst actions, M&A and litigation. This drove the risk-officer reductions on all three names, and it is why entries are limit-only.
- **Sector label normalised:** EXEL's sector label was normalised from "Health Care" to "Healthcare" to match AMPH and LFST, so the engine's sector aggregation groups all three together. Combined exposure (0.0178) is far below max_sector 0.30 either way.
- CDNA had no sector or industry in the candidate data and its research lists the sector as "Unknown". This did not affect the call because CDNA was rated Hold.
- The VIX percentile is 0.833, just under the 0.85 stress threshold. A cross above 0.85 would confirm stress and argues for re-checking the zones before any fill.

This report is not investment advice; decisions and orders are the owner's.
