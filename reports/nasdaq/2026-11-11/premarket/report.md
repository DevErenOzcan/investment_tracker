# NASDAQ premarket report: 2026-11-11

## 1. Summary
- **Regime: risk-off** (confidence 0.85). QQQ is below its 50- and 200-day averages and down 9.55% over 21 days. Semis and tech lead the decline. Healthcare, staples and financials hold near 1-year highs.
- **Funnel:** 2,984 universe → 2,868 with history → 1,001 liquid → 60 info pool → 25 candidates → 8 finalists → **3 recommendations** (5 Hold, 0 vetoed).
- **Invested 1.65% (16.5 units) and cash 98.35% (983.5 units)** of the 1,000-unit notional portfolio. All three are small, pullback-only entries. **The news feed was unavailable today, so no headline or event-risk check was done for any name.**

## 2. Actions

| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| PLMR | buy (new) | 0.85% | 8.5 | 155.70-159.00 | 150.90 | 174.00 | Overweight | 0.45 |
| SIBN | buy (new) | 0.48% | 4.8 | 24.00-24.90 | 23.30 | 28.40 | Overweight | 0.35 |
| COLM | buy (new) | 0.32% | 3.2 | 69.80-71.12 | 66.90 | 77.60 | Overweight | 0.42 |
| Cash | - | 98.35% | 983.5 | - | - | - | - | - |

All weights equal the engine's final weights after the risk-officer reductions (PLMR x0.6, SIBN x0.5, COLM x0.5). No PM adjustment was made. The last closes are above every entry zone: PLMR 161.08, SIBN 25.10 and COLM 72.26. Only fill inside the zone. Do not chase at the open. If price does not trade into the zone, skip the entry.

## 3. Current holdings
None. The notional portfolio is all cash (1,000 units), so there are no stop or target alerts. The risk review reported no held alerts.

## 4. Theses

**PLMR (Financial Services)**
- Q3 was strong: revenue +58% YoY, net income +27%, ROE 23.3% and forward P/E 13.9. The stock has low beta (0.24) and sits in a leading sector (XLF).
- From the 157.35 zone midpoint, reward/risk is about 2.6 to 174.0. At the 161.08 close it is about 1.3, which is why this is a pullback-only entry.
- Risks: RSI 75, 12.4% above SMA20, price at the mean analyst target, unscheduled catastrophe-loss gap risk, and possible offering risk after a 20% run.
- *Invalidation:* a daily close below 150.9. A close below 144.04 fully reverses the earnings breakout.

**SIBN (Healthcare)**
- Strong uptrend above SMA20/50/200. Q3 revenue rose 14.5% YoY with a narrowing loss and net cash, and the stock is in the leading sector (XLV).
- From the 24.45 midpoint, reward/risk is about 3.4, but the target needs a break above the 25.92 52-week high. The chance of hitting the target first is low.
- Risks: the stop is only about 0.9 ATR away, short interest is 11.7%, and a loss-making company near its highs could raise equity.
- *Invalidation:* a daily close below 23.3, or a close back inside the Nov 3 gap below about 23.77.

**COLM (Consumer Cyclical)**
- A margin-driven Q3 beat (net income +63%) produced a high-volume breakout to a 52-week high, with relative strength holding while selling is concentrated in tech.
- From the 70.65 midpoint, reward/risk is about 1.85, the weakest of the three, so it gets the smallest weight.
- Risks: revenue grew only 2%, short interest is about 19% of float (squeeze-driven gains can reverse), and it is a consumer cyclical with ^TNX near 5.0%.
- *Invalidation:* a daily close below 66.9, or a close back under SMA20 at 64.66.

**Portfolio note:** the sector labels differ, but all three are the same trade: extended post-earnings breakouts bought on a pullback. A single momentum unwind in a risk-off tape could hit all three together. The combined size stays small for that reason.

## 5. Rejected and vetoed
- **Risk-officer vetoes:** none. All three were reduced instead (see above).
- **APPN:** Hold. Reward/risk is about 1.04, below the 1.5 minimum, and tech lags in this regime.
- **CDNA:** Hold. The stop is about 0.7 ATR away on a beta-2.5 stock, and the cause of the gap is unverified.
- **EXEL:** Hold. There are signs of distribution near the highs, reward/risk at the close is about 1.3, and price is above the mean analyst target.
- **GMAB:** Hold. The cause of the +28% gap is unknown, and the weak pre-market indication (52.77) is unexplained.
- **GO:** Hold. It is indicated about 7% lower pre-market after earnings, a restatement is possible, and price is below the entry zone.
- **Dropped at triage:** HTFL, KOD and SLN (earnings on 2026-11-12, inside the blackout). BRZE, CYRX, VERX, ARHS, XERS, SGRY, VIR, SDGR, BSY and GDYN were over-extended (RSI or ext_20). AMPH was too thin. CERT, ASO and FLYW ranked below the picks.

## 6. Data notes
- **The news feed was unavailable today (network block), so no headline or event-risk check was done for any name.** Offerings, catastrophe losses, guidance changes, litigation and analyst actions are all unchecked. This is the main reason for the risk-officer reductions and the high cash level.
- At triage time, regime_view.json was not yet written, so triage used regime.json. The final regime_view.json agrees: risk-off.
- GMAB and CDNA have null sector/industry in the candidate data, so they were treated as Healthcare. The sub-industry cap could not be verified. Neither is recommended.
- The risk officer could not read the cards in cards/. Its review rests on research/, proposals.json and regime_view.json.
- The SEC-filing series was empty for some names (GMAB, CDNA). The GO restatement flag is unverified.
- The portfolio file has `as_of: null`. It is treated as all cash at the 1,000-unit base.

This report is not investment advice; decisions and orders are the owner's.
