# NASDAQ preclose review: 2026-11-18

## 1. Summary
- **Regime:** risk-off (confidence 0.85). QQQ is below its 50- and 200-day averages (ret_21 -8.55%), the VIX is at its 0.905 1-year percentile and ^TNX is 5.115. XLP, XLV and XLF lead.
- **Scope:** the 4 morning recommendations (no recorded holdings). 1 remains (GMAB) and 3 are cancelled after downgrades to Hold (CROX, AZTA, AMPH).
- **Book:** 0.72% invested (7.2 units) and 99.28% cash (992.8 units) against a notional base of 1,000 units.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| GMAB | buy-confirm | 0.72% | 7.2 | 50.90-51.90 | 49.90 | 57.29 | Overweight | 0.38 |
| CROX | cancel | 0.00% | 0 | (re-entry 157.0-160.9) | 148.80 | 178.98 | Hold | 0.43 |
| AZTA | cancel | 0.00% | 0 | (re-entry at or below about 45.8) | 43.00 | 50.06 | Hold | 0.45 |
| AMPH | cancel | 0.00% | 0 | (re-entry 28.8-29.4) | 27.30 | 32.50 | Hold | 0.40 |
| Cash | | 99.28% | 992.8 | | | | | |

All weights equal the engine weights. No PM adjustments were made.

## 3. Current holdings and morning orders
- `state/portfolio.json` has no positions, so there are no stop or target alerts on recorded holdings.
- **Fills against the morning zones today:**
  - **GMAB:** the morning zone 50.9-52.0 was traded (day range 51.12-52.26), so a morning fill is likely. Size stays at 7.2 units. Log a fill and the morning row as one observation (lessons item 3).
  - **CROX:** the day low of 156.10 traded inside the morning zone 154.5-158.5, so a resting order may have filled. Hold any fill with the 148.8 stop, no adds at 162.79; cancel any unfilled remainder.
  - **AZTA:** the morning zone 44.2-45.29 was never touched (low 45.56). Cancel.
  - **AMPH:** the day low of 28.90 touched the top of the morning zone 28.3-29.0, so a resting order at 28.90-29.0 may have filled. Hold any fill with the stop raised to 27.30; cancel any unfilled remainder.
- The owner should record any fills in `state/portfolio.json` so the next session treats them as held.

## 4. Theses
**GMAB (buy-confirm, 7.2 units)**
- The pullback thesis holds. The last price of 51.27 is inside the 50.9-51.9 zone and above the 50.68 swing low. The trend is still above SMA50/200 (42.25/31.82) with RS63 +0.61.
- Low-beta (0.52) XLV name in a risk-off tape led by healthcare. R/R is about 4.4 (6.02 reward against 1.37 risk) to the 57.29 post-spike closing high.
- Weaker than this morning: price is just below SMA20 (51.88), highs have been lower since 11/9 and the 5-day return is -4.9%. The spike catalyst is still unverified and insiders sold on 11/12, hence the x0.5 risk cut.
- *Invalidation:* a daily close below the 50.68 swing low (stop 49.9). That opens a gap-fill toward 44-45.

**CROX (cancel, Hold)**
- Thesis intact (10/29 re-rating, forward P/E about 10, holding the 149.5 base), but at 162.79 R/R is only 1.16, and the 164.24 high was rejected again today (high 164.07).
- Back to Overweight on a pullback into 157.0-160.9 (R/R about 1.96 at 159.0) or a close above 164.24 on expanding volume.
- *Invalidation:* a daily close below 149.5.

**AZTA (cancel, Hold)**
- Thesis intact (holding above 43.15, net cash, no catalyst before 2027-02-03), but the stock ran +5.8% to 48.49 on light volume with no news and sits 3% under the 50.06 target. R/R is about 0.29.
- The re-entry zone 45.6-46.8 gives R/R about 1.21 at its midpoint; R/R reaches 1.5 only at or below about 45.8.
- *Invalidation:* a daily close below 43.15. A close above 50.06 on volume needs a new breakout review.

**AMPH (cancel, Hold)**
- Stacked uptrend and Q3 beat (forward P/E 8.9) intact, but at 29.775 R/R is 1.10 and the first leg to the 31.00 high is about 1.06.
- Re-entry in 28.8-29.4 with the stop raised to 27.30 (R/R 1.89 at 29.10, about 1.5 at 29.38).
- *Invalidation:* a daily close below the 27.43 swing low.

## 5. Rejected and vetoed
- **CROX, AZTA, AMPH (engine rejected, rating Hold):** all three were downgraded on R/R at the last price (lessons item 1), not because the thesis broke.
- The risk officer issued no new vetoes. One reduction: GMAB x0.5. The morning SEZL veto stands.

## 6. Data notes
- Prices are about 15 minutes delayed and today's volume is partial. The GMAB stop is only 1.37 below the last price (about 0.65 ATR).
- GMAB: the catalyst behind the 10/05, 10/23 and 10/28 spikes is still unverified.
- No bull/bear debate ran this session (no rating moved by two notches).

This report is not investment advice; decisions and orders are the owner's.
