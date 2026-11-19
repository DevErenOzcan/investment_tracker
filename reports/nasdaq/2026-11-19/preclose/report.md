# NASDAQ pre-close review, 2026-11-19

## 1. Summary
- Regime: **risk-off** (confidence 0.85). QQQ 21-day return is -8.1% and it trades below its 50- and 200-day averages. VIX is at the 0.858 percentile. Staples, health care and utilities are leading.
- Funnel: 2,973 universe → 25 morning candidates → 3 morning recommendations re-assessed → **2 confirmed** (PGNY, TGTX). 1 is cancelled (VTRS).
- Invested **1.32%** (13.2 units of 1,000). Cash **98.68%** (986.8 units).

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| PGNY | buy-confirm | 0.88% | 8.8 | 34.90-35.80 | 33.20 | 40.00 | Overweight | 0.44 |
| TGTX | buy-confirm | 0.44% | 4.4 | 63.80-65.40 | 61.20 | 72.60 | Overweight | 0.40 |
| VTRS | cancel | 0.00% | 0 | - | (19.70 breached) | - | Hold | 0.38 |

The weights are the engine weights, with no PM adjustment. They differ from the morning sizes:
- PGNY rises from 0.47% to 0.88% because the pullback raised R/R from 1.67 to 1.91 and the Kelly constraint binds.
- TGTX rises from 0.35% to 0.44% after the engine recomputed its size, including the risk officer's x0.75 cut.

The entry zones are re-based so that R/R stays at 1.5 or better at the top of the zone: PGNY 1.62, TGTX 1.71.

## 3. Current holdings
- `state/portfolio.json` records no positions, so there are no stop or target alerts. The risk officer raised no held alerts.
- Alert: if the owner filled the morning VTRS order (the open at 20.25 traded inside the zone), treat that position as **stopped out**, because the low of 19.68 went through the 19.70 stop. Do not carry it on a lower stop.

## 4. Theses
**PGNY (Overweight, 0.44)**
- The post-earnings breakout is holding. Today's -1.7% pullback came on light volume (0.77x), and the low of 34.95 stayed well above the 33.34 post-earnings low.
- The trend is up: price is above SMA20, SMA50 and SMA200, and rs_63 is +0.48. Health care is a leading group in the risk-off tape.
- R/R is 1.91 at 35.54. The size is not raised because of the CEO, chairman and CPO sales (not confirmed as plan-based), a sequential revenue dip and the thin margin.
- *Invalidation:* a daily close below 33.30. A close below 32.03 (back inside the gap) means the breakout has failed.

**TGTX (Overweight, 0.40)**
- Q3 revenue rose 60.7% YoY, guidance was raised, and the uptrend is intact above all three moving averages (RS63 +0.29).
- The light-volume pullback traded into the zone (low 64.81). R/R is about 1.98 at 65.02.
- It is the smallest line because of the rejection at 67.19, beta 1.81, 27.7% short float, debt above cash (raise risk) and a stop only about 1.2 ATR away.
- *Invalidation:* a daily close below 61.20, or a failed push above 68.03 that closes back below 63.40 on above-average volume.

**Correlation note:** both names are same-day healthcare post-earnings pullbacks. Treat them as one correlated bet (lessons item 6). A broad de-risking flush could gap both through their stops together. Their combined size is small.

## 5. Rejected and vetoed
- **VTRS:** cancelled. It was downgraded to Hold (the engine rejected it as no new buy) and the risk officer vetoed it. The morning stop of 19.70 was breached (low 19.68), down days show distribution volume, and the 2026-11-17 Item 2.01 8-K has not been reviewed.

## 6. Data notes
- The VTRS 8-K of 2026-11-17 (Item 2.01, completed acquisition or disposition) is still unreviewed.
- PGNY: the packet does not say whether the insider sales were plan-based, and no article covers the earnings details.
- TGTX: the next earnings date is not in the packet (the last report was 2026-11-09).
- The preclose volume ratios use a partial day.
- The preclose run has no `candidates.json`. The funnel counts come from the morning run.
- Count the same-day premarket and preclose rows as one observation (lessons item 3).

This report is not investment advice; decisions and orders are the owner's.
