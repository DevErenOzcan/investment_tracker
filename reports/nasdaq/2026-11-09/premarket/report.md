# NASDAQ premarket report — 2026-11-09

## Summary
- **Regime: risk-off** (confidence 0.9): QQQ is below its 50- and 200-day averages (21-day -12.24%), the VIX 1-year percentile is 0.876, tech and semis lead the decline (XLK -16.71%, SMH -23.6% over 21 days), and defensives lead (XLV, XLP, XLRE).
- **Funnel:** 2,986 universe → 2,864 with history → 1,000 liquid → 25 candidates → 8 finalists → 4 recommendations (all Overweight, conditional pullback entries).
- **Invested weight 0.0247 (24.7 units), cash 0.9753 (975.3 units)** of the 1,000-unit notional base; engine weights are kept unchanged after the risk-off multiplier (0.4) and the risk officer's reductions.

## Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| CRVL | buy (new) | 0.0100 | 10.0 | 81.50–83.20 | 78.90 | 89.76 | Overweight | 0.47 |
| EXEL | buy (new, pullback only) | 0.0065 | 6.5 | 67.00–69.60 | 64.10 | 77.10 | Overweight | 0.47 |
| AMPH | buy (new, pullback only) | 0.0049 | 4.9 | 27.50–28.40 | 26.60 | 31.00 | Overweight | 0.42 |
| KDP | buy (new, pullback only) | 0.0033 | 3.3 | 35.60–36.10 | 34.00 | 39.49 | Overweight | 0.45 |
| Cash | — | 0.9753 | 975.3 | — | — | — | — | — |

Buy only inside the entry zone. Pre-market prices for EXEL (71.0) and KDP (36.5) are above their zones, and AMPH's last close (28.49) is above its zone, so these need a pullback to fill. Do not chase.

## Current holdings
No holdings are recorded in `state/portfolio.json` (1,000 cash units), so there are no stop or target alerts. The risk review raised no held-position alerts.

## Theses
**CRVL** (Financial Services, insurance services)
- Uptrend (close 83.16 above SMA20 82.11, SMA50 76.13, SMA200 62.85) pulling back to SMA20 after a net-positive earnings reaction (11-04 gap up, close 87.38).
- High-quality, accelerating fundamentals; not a tech name in a tech-led sell-off. R/R 2.15 from the 82.35 midpoint, and no earnings until 2027-02-02.
- Capped at Overweight: rich multiple (trailing P/E 34.9), a failed push at 89.76, up 34.8% in 63 days, and thin liquidity.
- *Invalidation:* daily close below 78.9; a close below SMA50 (76.13) breaks the uptrend.

**EXEL** (Healthcare, biotech)
- Clean uptrend (close 69.57 above SMA20 65.63, SMA50 60.92, SMA200 51.57; rs_63 +0.40) in the leading Healthcare sector (XLV 21-day +9.9%).
- Profitable growth (latest quarter revenue +10.2% YoY), and earnings are past (2026-10-29). R/R about 2.1 from the 68.3 midpoint.
- The 11/05 reversal from 73.69 on 4.4M shares is a distribution warning, with resistance between entry and target; biotech event risk is unchecked.
- *Invalidation:* daily close below 64.1, or a close below SMA20 (65.63) on rising volume.

**AMPH** (Healthcare, specialty pharma)
- Clean uptrend (close 28.49 above SMA20 26.55, SMA50 25.35, SMA200 22.29) with accelerating revenue growth (0.4% → 5.4% → 8.2% YoY) and a forward P/E of 8.57.
- R/R 2.26 from the 27.95 midpoint, but the target is the 31.0 post-earnings spike that was just rejected.
- 22.08% short interest, a mean analyst target of 22.5 below price, leverage and thin FCF limit conviction.
- *Invalidation:* daily close below 26.6 (under the 2 Nov low of 26.69).

**KDP** (Consumer Defensive)
- Trend-4 uptrend (close 36.63 above SMA20 34.93, SMA50 32.78, SMA200 29.87) with rs_63 0.35 in the leading XLP group; earnings are past (2026-11-03).
- R/R 1.61 at 36.1 only; it needs a pullback entry and a breakout through the 37.89 52-week high to reach 39.49.
- Fundamentals are unverified: an unexplained revenue step from 3,976M to 7,309M suggests a corporate action whose terms are not visible.
- *Invalidation:* daily close below 34.0, or a close back below SMA20 (about 34.93) after a failed attempt at 37.89.

**Portfolio note:** all four names are bets that the defensive rotation continues (Healthcare 0.0114 combined, plus Consumer Defensive and insurance services). A risk-on reversal or a rebound in XLK/SMH would likely hit them together.

## Rejected and vetoed
**Vetoed by the risk officer:** none.

**Rejected after research (rating Hold, no new buy):**
- **ASO:** R/R about 1.15, below 1.5; stretched (RSI 74, 11.8% above SMA20) in a non-leading cyclical sector.
- **CDNA:** R/R about 1.42, below 1.5; beta 2.49, ATR 6.85%, pre-market 81.0 above the zone.
- **MANH:** R/R about 1.21; Technology lags in risk-off and the forward P/E is 40.9.
- **SIBN:** R/R about 1.4; extended 13% above SMA20 after the gap, and the gap reason is unknown.

**Dropped at triage:**
- **Overbought (RSI above 78):** BRZE (RSI 81.4), BSY (RSI 80.1).
- **Over-extended (ext_20 above 15%):** CERT (15.2%), GMAB (16.8%, 5-day -6.0%), VERX (15.7%), ARHS (24.2%, RSI 76.4), XERS (40.2%, RSI 82.4), REPL (46.1%, RSI 79.9).
- **Earnings blackout:** KOD and HTFL (earnings 2026-11-12, within 3 business days), SLN (earnings today, RSI 78.06, ext_20 15.6%).
- **Weaker setup or sector preference:** APPN (software slot went to the more liquid MANH), FLYW and AMPL (lagging tech; AMPL forward P/E 98.6), SDGR (ext_20 14.4%, ATR 7.4%, weak volume), CBLL (trend score 3, RSI 51.9), SEZL (ATR 7.6%, 23.6% below the high).

## Data notes
- **News feed blocked:** the yfinance news feed was blocked by the network proxy for every ticker, so `news_7d` is empty everywhere. This is missing data, not proof that there were no events. Event, litigation and offering risk could not be checked, and that drove most of the risk officer's reductions.
- **Quote/profile endpoint returned 401:** the yfinance quote/profile endpoint returned 401 during the screen, so sector and industry fields are null in `candidates.json`. Sector labels in this report come from the research cards, and valuation context is thin for some names (for example, EXEL's profile fields are null).
- **SEC filings partial:** SEC filings were only partly available. The content of recent 8-K/10-Q filings (CRVL, AMPH, KDP) was not reviewed, and some quarterly series have gaps.
- KDP's revenue series shows an unexplained step (3,976M → 7,309M), so its fundamentals are treated as unverified.
- Pre-market prices (EXEL 71.0, KDP 36.5, CDNA 81.0) are above the research entry zones. Fills depend on pullbacks.

This report is not investment advice; decisions and orders are the owner's.
