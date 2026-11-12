# NASDAQ pre-close review, 2026-11-12

## 1. Summary
- **Regime:** neutral (confidence 0.65). QQQ ret_21 is -7.15%, close to the -8% risk-off trigger. Leadership has rotated into XLV, XLP and XLF, while XLK and SMH lag. The 10-year yield is 5.048.
- **Morning call vs pre-close call:** VTRS Overweight buy, now **buy-confirm** (weight 1.81% -> 1.72%, engine recompute). CERT Overweight buy, now **buy-confirm** (1.30%, unchanged). GMAB Overweight conditional buy, now **cancel** (downgraded to Hold, engine weight 0). APPN Overweight minimal buy, now **cancel** (risk-officer veto).
- **Invested weight:** 3.02% (30.2 units), all of it pullback-only limit entries that have not filled. **Cash:** 96.98% (min 10%).

## 2. Actions

| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| VTRS | buy-confirm (limit, pullback only) | 1.72% | 17.2 | 20.40-20.80 | 19.20 | 23.40 | Overweight | 0.47 |
| CERT | buy-confirm (limit, pullback only) | 1.30% | 13.0 | 11.30-11.80 | 10.40 | 13.55 | Overweight | 0.47 |
| GMAB | cancel | 0 | 0 | - | - | - | Hold | 0.28 |
| APPN | cancel (vetoed) | 0 | 0 | - | - | - | Overweight (vetoed) | 0.42 |

Engine weights are used unchanged; the PM made no adjustments. Pre-close levels vs morning: VTRS zone top 20.85 -> 20.80, stop 19.25 -> 19.20, target 23.5 -> 23.4. CERT zone top 11.75 -> 11.80, stop and target unchanged.

## 3. Current holdings and names near their stop
- **Holdings:** none. `state/portfolio.json` is empty, so there are no stop or target alerts.
- **Recommendations near their stop:**
  - VTRS last 20.915 is 8.2% above its 19.20 stop (about 3 ATR). Not close.
  - CERT last 11.855 is 12.3% above its 10.40 stop. Not close. The intraday low of 11.29 was still 8.6% above the stop.
  - GMAB (cancelled) is the closest: last 51.93 against the pre-close card stop of 50.70 is only 2.4% (about 0.5 ATR). This is one reason not to revive it intraday.
- **Fills:** both live names trade above their zones. Any limit order the owner chooses to place must sit inside the zone; filling at the current price breaks the R/R math.

## 4. Theses

**VTRS (Overweight, 0.47)**
- The post-earnings beat-and-raise uptrend holds: last 20.915 > SMA20 19.18 > SMA50 18.04 > SMA200 16.06, and healthcare is still the leading sector.
- Today's light-volume dip from the 21.20 52-week high is consolidation with no news driver. RSI 72.9 is still overbought, so wait for the pullback.
- R/R is 2.0 from the zone mid (20.60) and about 1.45 at the current price. Risks are Pacira closing near 2026-11-17 (financing or issuance) and price already at the mean analyst target.
- *Invalidation:* a daily close below 19.20 or back under SMA20 (~19.18). No entry if price never retraces into 20.40-20.80, and do not chase above 21.20.

**CERT (Overweight, 0.47)**
- The uptrend holds (11.855 > SMA20 10.96 > SMA50 9.63 > SMA200 7.35) after the Q3 beat, with no event risk before about Feb 2027.
- Today it tested the zone bottom (11.29) and bounced. Volume was light, so the 11/11 bearish reversal is not resolved.
- R/R is 1.74 from mid and about 1.17 at the current price. First resistance at 12.61 and 26.2% short interest mean gap risk in both directions.
- *Invalidation:* a daily close below 10.46 (10-day swing low). The 10.40 stop is hard.

Concentration note: both names are healthcare-rotation and post-earnings-drift bets (CERT sells software to pharma), so a rotation reversal would hit both. Combined exposure is 3.02%, well under the 30% sector cap.

## 5. Rejected and vetoed
- **GMAB:** downgraded to Hold (0.28). It failed to hold the 52.0-53.4 zone and faded from 53.03 to 51.93, a fourth straight lower close, with no news to explain it. Re-assess only after a daily reclaim above 53.03.
- **APPN:** risk-officer veto. The card zone gives R/R 1.35, below the 1.5 minimum, and the narrowed 52.28-52.7 zone sits far below the 54.93 last price (about 0.9 R/R there). It is also a lagging-tech, high-volatility name (ATR 5.6%, 11.7% short interest).

## 6. Data notes
- Pre-close prices are intraday last, about 15 minutes delayed (packet as_of 19:53 UTC). The engine `price` fields for VTRS (20.60) and CERT (11.55) are zone midpoints, not last prices. This report uses last.
- The Pacira closing date (on or near 2026-11-17) is inferred from an index-change notice, not confirmed by the company.
- The GMAB decline has no news or SEC filing in the packet dated after 2026-11-08. Its litigation risk was flagged on the Q3 call, but the details are not in the packet.
- There is no candidates.json for this session, because no universe screen runs pre-close. The review covers only the morning's four recommendations.

This report is not investment advice; decisions and orders are the owner's.
