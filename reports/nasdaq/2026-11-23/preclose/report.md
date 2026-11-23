# NASDAQ preclose report: 2026-11-23

## 1. Summary
- **Regime:** risk-off (confidence 0.95). QQQ is below its 50- and 200-day averages (21-day -13.63%), VIX is 31.34 (1-year percentile 0.991), and only XLP, XLV and XLU hold above their 50-day. Engine regime multiplier is 0.4.
- **Funnel:** morning 2,977 universe → 25 candidates → 8 finalists → 4 recommendations; preclose re-check of those 4 → 1 kept (CRVL), 3 cancelled (SIBN, AMPH, GMAB).
- **Book:** 0.54% invested (5.4 units of 1,000) if the CRVL limit fills, and 99.46% cash. No holdings today.

## 2. Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| CRVL | buy-confirm (limit ≤ 87.25, skip if not filled) | 0.54% | 5.4 | 86.50 - 87.25 | 81.60 | 95.90 | Overweight | 0.45 |
| SIBN | cancel | 0.00% | 0 | re-entry 23.85 - 24.25 | 22.55 | 25.92 | Hold | 0.50 |
| AMPH | cancel | 0.00% | 0 | re-entry 28.30 - 28.75 | 27.55 | 31.00 | Hold | 0.42 |
| GMAB | cancel | 0.00% | 0 | re-entry 51.60 - 52.60 | 49.90 | 57.30 | Hold | 0.37 |
| Cash | | 99.46% | 994.6 | | | | | |

CRVL weight equals the engine weight (0.0054); no PM adjustment. The engine gave 0 to the three cancelled names, so the PM cannot add weight to them. Re-entry zones are the analysts' levels for a future session, not orders for today.

## 3. Current holdings
No holdings (`state/portfolio.json` has 1,000 cash units and no positions). No stop or target alerts, and the risk officer raised no held alerts. None of the morning orders filled: CRVL's intraday low (87.69) did not reach the 87.25 limit, and SIBN, AMPH and GMAB traded above their zones.

## 4. Theses
**CRVL (buy-confirm, limit only)**
- Tight 87-90 consolidation under the 90.71 52-week high, above SMA20 85.04, SMA50 79.95 and SMA200 64.19, with rs_63 +0.34 while QQQ fell 13.63% over 21 days.
- Revenue +11.47% YoY and net income +22.15% YoY; no catalyst before the 2027-02-02 earnings.
- Small size because of the risk-off regime, P/E 37.01 and officer Form 144 sales near the high; R/R is 1.53 at 87.25 and about 1.20 at the 88.09 last, so do not chase.
- *Invalidation:* daily close below the 81.84 swing low (stop 81.6); a close back below SMA20 (about 85.0) on rising volume is the early warning.

**SIBN (cancel)**
- Post-Q3 re-rating (revenue +14.5% YoY, net cash) in an uptrend, in one of only three sectors above the 50-day.
- Price ran to 24.59 (+3.6% on the day), R/R about 0.65 at the last price.
- Even the 24.05 midpoint of the re-entry zone gives about 1.25 R/R against the 22.55 stop and 25.92 target; by PM check only an entry at about 23.89 or lower clears the 1.5 floor, unless price breaks above 25.92 on volume.
- *Invalidation:* daily close below 22.55 (under the 22.72 swing low of 11/18).

**AMPH (cancel)**
- Uptrend intact (above SMA20 28.19, SMA50 26.62, SMA200 22.38; rs_63 +0.42); forward P/E 8.4.
- Ran +3.5% to 29.23 on light partial-day volume with no catalyst; R/R about 1.05 at the last price.
- Becomes actionable again in 28.30-28.75 (about 2.5 R/R at the 28.525 midpoint); stop raised to 27.55.
- *Invalidation:* daily close below 27.55 (under the 27.79 swing low of 11/19-11/20).

**GMAB (cancel)**
- Held the 50.24 10-day low and bounced to 53.12 (+5%); trend up (SMA20 53.19 > SMA50 43.39 > SMA200 32.12).
- About 3.5% above the morning zone top; R/R about 1.3 at the last price. The bounce came on light volume (vol_ratio 0.65) and the structure since the 10/28 gap is still lower highs.
- Re-entry only on a dip into 51.60-52.60 (about 2.4 R/R at the 52.1 midpoint); stop raised to 49.9.
- *Invalidation:* daily close below 49.9, which opens a gap-fill toward the 43.98 20-day low.

## 5. Rejected and vetoed
- **SIBN:** rejected by the engine, rating Hold (entry ran away, R/R below 1.5).
- **AMPH:** rejected by the engine, rating Hold (entry ran away, R/R about 1.05).
- **GMAB:** rejected by the engine, rating Hold (entry ran away, R/R about 1.3).
- **Risk-officer vetoes:** none. No reductions.

## 6. Data notes
- CRVL sector label: the packet profile says Financial Services / Insurance Brokers, while the cards use Healthcare (kept for consistency with the morning and lesson 8). No limit changes at this size.
- The CRVL technical card JSON was malformed (unterminated notes string) and was repaired; its values were checked against the packet.
- The news feed was titles-only Google RSS for some names. Offering risk was covered by the SEC filing check (no S-3/424B5 in 10 days).
- SIBN correction: the morning card cited a CEO sale. The packet shows only tax-withholding sales by the legal chief and one other officer on 11/18.
- GMAB: the SEC quarterly series was empty, and the October catalysts are sourced only from an IBD recap.
- Intraday prices are about 15 minutes delayed; volume figures are partial-day, so volume ratios understate the full session.

This report is not investment advice; decisions and orders are the owner's.
