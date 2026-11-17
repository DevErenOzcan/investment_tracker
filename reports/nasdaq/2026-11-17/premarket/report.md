# NASDAQ premarket report: 2026-11-17

## 1. Summary
- **Regime:** risk-off (confidence 0.8). QQQ is below its 50- and 200-day averages (ret_21 -6.77%), VIX is at the 0.877 1-year percentile and ^TNX is at 5.141. Defensives (XLP, XLV) and financials lead.
- **Funnel:** 2984 universe → 2872 with history → 997 liquid → 60 info pool → 25 candidates → 8 finalists → 4 recommendations (all Overweight, all small).
- **Book:** 3.52% invested (35.2 of 1000 units) and 96.48% cash. Engine weights are used unchanged. Consumer Cyclical is 2.67% and Healthcare is 0.85%, both well below the 30% sector cap.

## 2. Actions
All four are new, pullback-only limit entries. Do not chase above the zone. HAS, CROX and GCT were quoted above their zones before the open, so some may not fill today.

| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| HAS | buy | 1.42% | 14.2 | 119.0-121.0 | 116.7 | 132.1 | Overweight | 0.40 |
| CROX | buy | 0.87% | 8.7 | 155.5-159.0 | 148.8 | 178.9 | Overweight | 0.42 |
| GMAB | buy | 0.85% | 8.5 | 50.7-51.6 | 49.5 | 59.0 | Overweight | 0.33 |
| GCT | buy | 0.38% | 3.8 | 62.0-63.0 | 57.7 | 72.0 | Overweight | 0.45 |
| Cash | - | 96.48% | 964.8 | - | - | - | - | - |

## 3. Current holdings
No positions are held (`state/portfolio.json`: 1000 cash units, no positions), so there are no stop or target alerts. The risk review raised no held alerts.

## 4. Theses and invalidation
**HAS** (Overweight, 0.40)
- Post-earnings trend continuation backed by fundamentals: Q3 revenue +15.0% YoY, net income +69.2%, outlook raised.
- Price is consolidating the 10/20 gap in a 117.1-124.6 range above SMA20 (118.90) on fading volume. R/R from the zone to the 132.1 measured move is about 3.7.
- The target needs a break of 124.62, and price is close to the 123.31 mean analyst target. Leverage is high (D/E about 410) while yields are rising.
- *Invalidation:* a daily close below 116.7, which is under the 117.13 swing low.

**CROX** (Overweight, 0.42)
- The 10/29 earnings re-rating has held for about three weeks above SMA20/50/200. Forward P/E is 10.0, ROE 49.1% and Q3 net income +48.65% YoY.
- R/R from the zone is about 2.6, but only about 1.8 at the 159.5 pre-market quote, so the entry is pullback-only.
- Beta 1.5, the twice-rejected 164.24 high and the 164.67 mean analyst target cap near-term upside. The risk officer cut the size by x0.75.
- *Invalidation:* a daily close below 148.8, or a failed break of 164.24 that closes back under 160 on rising volume.

**GMAB** (Overweight, 0.33)
- Profitable healthcare name (operating margin 30.6%, FCF 855M) pulling back on fading volume to SMA20 (50.65) and the 50.68 swing low, in a sector that leads this tape.
- R/R is about 4.8 to 59.0, but the stop is only about 0.75 ATR away, so the R/R overstates the edge. The risk officer cut the size by x0.75.
- The driver of the 10/28 +28% gap is unknown, insiders are selling, and warrant dilution is minor. The pre-market price is 50.83, and the entry is valid only while 50.68 holds.
- *Invalidation:* a daily close below 49.5, or an open that holds below 50.68 (entry is then off).

**GCT** (Overweight, 0.45)
- GigaCloud (not GCT Semiconductor) is holding its 11/5 earnings gap after a Q3 beat (revenue +27%, net income +36%) at a forward P/E of 10.2.
- R/R is only 1.70 at 63.0 and about 1.2 at the 64.15 last close, the 11/16 high was rejected, beta is 1.6 and short interest is 11.5% of float. The risk officer cut the size by x0.5 to a starter position.
- It forms one consumer-discretionary momentum theme with HAS and CROX, so expect the three to stop out together on a risk-off leg.
- *Invalidation:* a daily close below 57.7 (a full gap fill), or a close below SMA20 (about 60.4) on rising volume before entry.

## 5. Rejected and vetoed
- **APPN:** Hold. Extended 8.4% above SMA20 in a lagging tech sector, with R/R about 1.34 at the last close (lesson 1). Revisit if price fills 53.0-54.8.
- **AMPL:** Hold. Heavy supply at 18.85 leaves only about 0.7R to first resistance, and the stock has GAAP losses and a forward P/E of 106 while ^TNX is at 5.14.
- **AMPH:** Hold. R/R is about 1.15 at mid-entry because of 31.0 resistance, and the price is above the mean analyst target.
- **ASO:** Hold. R/R is about 1.16 at the last price, and earnings on 12/08 come with about 19.9% short interest.
- **Dropped at triage:** ACHC, XMTR, SEZL (over-extended), SLN (pinned to a pending acquisition), VERX, COLM, STGW (stretched), LFST (secondary offering), XNCR, VRDN, KOD (binary biotech risk), CERT, ARHS, CDNA, ADMA, CYRX, CHA (weaker or broken setups, thin liquidity).
- **Risk-officer vetoes:** none. Reductions: GCT x0.5, GMAB x0.75, CROX x0.75.

## 6. Data notes
- **No sentiment card this run.** All theses rest on technical, fundamentals and news cards only (lesson 9).
- **Yahoo 401/429 errors:** some packet fundamentals fields are missing. The APPN profile is null, so its valuation, cash, debt and short interest are unknown. APPN was rated Hold anyway.
- **Earnings dates:** `earnings_date` is null in every research packet. The last reports (HAS 10/20, CROX 10/29, GMAB and GCT about 11/5) make the next ones very likely outside the 10-day horizon, but this is unconfirmed.
- **Sector labels:** these were filled in by the research-manager. The screener lists GCT as Technology / Software - Infrastructure, but research and risk label it Consumer Cyclical (GigaCloud, B2B e-commerce goods), and that label is used here. Even under the screener label, both sectors stay far below the cap.
- **Ticker collision:** GCT headlines mix GigaCloud with GCT Semiconductor, so the news read for GCT is noisy.
- **Triage ran without `regime_view.json`**, so triage did not apply a preference for leading sectors. The regime multiplier (0.4) was applied in sizing.
- **Risk review ran twice:** the first pass could not locate the analyst cards and cut every name; the second pass read the cards and replaced it (HAS cut withdrawn, GMAB cut eased to x0.75).
- **GMAB:** the cause of the 10/28 gap is unexplained in the packets.
- **Lessons are unvalidated** (no scored decisions yet). GMAB and APPN appear in lesson 5 as earlier vetoes to track. GMAB is included today at a reduced size.

This report is not investment advice; decisions and orders are the owner's.
