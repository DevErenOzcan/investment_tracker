# NASDAQ pre-close review — 2026-11-10

## Summary
- **Regime: risk-off** (confidence 0.8, same label as the morning). QQQ is below its 50- and 200-day averages (21-day -9.57%), VIX is 20.85 (1-year percentile 0.833, +37.08% over 21 days), SMH is at -19.21% over 21 days, and defensives (XLV, XLP) lead.
- **Review list:** the 3 morning recommendations (morning funnel 2,986 → 1,000 liquid → 25 candidates → 3), and there are no holdings. **What changed:** all three stay Overweight and are confirmed at lower weights for EXEL and AMPH and a slightly higher one for LFST. EXEL has pulled back into its zone. LFST and AMPH trade above their zones and are limit-only.
- **Invested weight 0.0132 (13.2 units), cash 0.9868 (986.8 units)** of the 1,000-unit notional base, versus 0.0178 / 0.9822 this morning. Engine weights are kept unchanged.

## Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| EXEL | buy-confirm | 0.0061 | 6.1 | 69.50–71.00 | 67.70 | 76.00 | Overweight | 0.45 |
| LFST | buy-confirm (limit only) | 0.0040 | 4.0 | 14.00–14.40 | 12.95 | 17.00 | Overweight | 0.40 |
| AMPH | buy-confirm (limit only) | 0.0031 | 3.1 | 28.00–28.60 (fill ≤ 28.30) | 26.60 | 31.00 | Overweight | 0.45 |
| Cash | — | 0.9868 | 986.8 | — | — | — | — | — |

Current prices (about 15 min delayed) are EXEL 70.72, LFST 14.66 and AMPH 29.06. EXEL is inside its zone; do not fill above 71.00. LFST is 0.26 above its zone; reward/risk at 14.66 is about 1.37, so do not chase. AMPH is 0.46 above its zone; reward/risk only reaches 1.5 at or below about 28.36, so the limit belongs in the lower half of the zone.

Morning versus afternoon:
- EXEL: weight 0.0084 → 0.0061, stop 67.8 → 67.7, zone 69.6–71.3 → 69.5–71.0.
- AMPH: weight 0.0061 → 0.0031, zone 27.9–28.5 → 28.0–28.6, stop unchanged at 26.6.
- LFST: weight 0.0033 → 0.0040, stop 12.85 → 12.95, zone unchanged.

The EXEL and AMPH cuts come from the risk officer's x0.75 and x0.5 reductions. LFST's x0.5 cut was applied to a higher pre-cut engine weight than this morning's.

## Current holdings
`state/portfolio.json` records no holdings (1,000 cash units), so there are no stop or target alerts, and the risk review raised no held-position alerts.
- **Possible unrecorded fills:** today's prices traded through two of the morning limit zones:
  - EXEL: morning zone 69.6–71.3; today's low was 69.74 and the open 71.56.
  - LFST: morning zone 14.0–14.4; today's low was 14.28 and the open 14.39.

  If the owner placed those limits, they may have filled. Fills should be recorded in `state/portfolio.json`, and then those names count as held, not new. AMPH's morning zone (27.9–28.5) was missed by 0.01 (low 28.51).

## Thesis
**EXEL** (Healthcare, biotechnology)
- High-margin, cash-generative biotech (operating margin 0.41, FCF 759M vs debt 162M) in a strong uptrend: last 70.72 is above SMA20 66.79, SMA50 61.59 and SMA200 51.84, with a 63-day return of +40.4%.
- The pullback the morning card wanted has arrived. RSI cooled from 70.5 to 66.2 and the 68.01 swing low is intact. Reward/risk is 1.75 to 76.0 against a 67.70 stop.
- Held at Overweight: the causes of the 11-05 reversal and the 11-09 volume are unknown, the price is above the 61.57 mean analyst target, short interest is 15.3%, and there is supply at 73.69.
- *Invalidation:* a daily close below 67.70 (under the 68.01 swing low), or a failed heavy-volume break of 73.69 that closes back under 68.

**LFST** (Healthcare, medical care facilities)
- Real operating improvement: revenue +25.3% YoY, positive net income and FCF. It is holding the Nov 9 breakout (last 14.66, today's range 14.28–14.88) above all three averages.
- Reward/risk is 2.24 from the 14.20 zone midpoint, falling to about 1.37 at the current price, so it is a limit-only entry.
- Lowest confidence (0.40) and widest stop (8.8%). The Nov 9 move on 29.5M shares (about 6x average) has no verified cause, valuation is rich (trailing P/E 81.4), and there is overhead supply at 15.66.
- *Invalidation:* a daily close below 12.95 (under the 13.05 10-day swing low), or a heavy-volume close back under the 13.20 Nov 9 low.

**AMPH** (Healthcare, specialty and generic drugs)
- Post-earnings uptrend at low multiples (forward P/E 8.74, EV/EBITDA 8.64): revenue +8.2% and net income +118% YoY, and last 29.06 is above all three averages.
- Today's drift on light volume (247k) cooled RSI to 67.6 without breaking structure. Reward/risk is 1.59 from the 28.30 midpoint but about 0.8 at 29.06.
- Supply sits at the 31.0 target (the 11-06 rejection). Other risks: short interest 22.1%, net debt, weak FCF (9.2M), price above the 24.5 mean analyst target, and prior-quarter net income refiled on 11-05 without being assessed.
- *Invalidation:* a daily close below 26.60, or a close below the 11-06 low of 27.80 that does not quickly recover.

**Theme risk (risk officer):** all three are the same trade, long post-earnings health care momentum that depends on the XLV rotation continuing. A reversal of that rotation would hit all three together.

## Rejected and vetoed
- **Rejected by the engine:** none this session.
- **Vetoed by the risk officer:** none. Reductions: EXEL x0.75 (news and filings unavailable, causes of the reversal and volume unknown), LFST x0.5 (unexplained 6x volume, lowest confidence, widest stop), AMPH x0.5 (unassessed net income refile, reward/risk below 1.5 outside the limit).
- The universe was not re-screened, so no other morning candidates were reconsidered.

## Data notes
- **News feed blocked:** the network proxy still blocked the news feed, so `news_7d` is empty for every ticker. That means the data is missing, not that nothing happened. It drove all three risk-officer reductions.
- **SEC filing content not reviewed:** EXEL has no filings in the last 10 days. The LFST 10-Q and 8-K (items 2.02, 7.01, 9.01, filed 11-05) and the AMPH 10-Q and 8-K (filed 11-05) are unread. AMPH's prior-quarter net income values were all refiled on 11-05 and have not been checked for a restatement.
- **No bull/bear debate ran** this session because no rating moved two notches. The ratings rest on the afternoon cards and the morning debate.
- **Engine `price` field:** LFST and AMPH were sized at their zone midpoints (14.20, 28.30), not at their current prices. `allocation.json` shows the current intraday prices. The AMPH research text gives reward/risk of "about 0.9" at 29.06, but its own levels (31.00 target, 26.60 stop) give about 0.8.
- Intraday prices are about 15 minutes delayed.
- `candidates.json` in this folder is a copy of the morning funnel. The morning finalist count is not recorded in this folder.

This report is not investment advice; decisions and orders are the owner's.
