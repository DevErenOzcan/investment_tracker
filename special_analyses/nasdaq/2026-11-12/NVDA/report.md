# NVDA special analysis — 2026-11-12 (pre-market)

> Analysis only, not a portfolio decision and not investment advice. No `allocation.json` written;
> `state/portfolio.json` untouched. Sizing base: notional 1,000 units.

## Verdict
**Rating: Hold (watchlist) · confidence 0.20 · debate winner: bear · engine-proposed weight: 0%**
(`scanner.sizing`: 0 positions, cash weight 1.0 — Hold ratings do not open positions.)

NVIDIA's fundamentals are strong and cheap on the packet's ratios, but there is no technical setup,
the reference long levels are already broken in the pre-market, the selloff's cause is unknown, and
earnings land inside the holding window. Wait.

## Data used / not available
| Source | Status |
|---|---|
| Prices, indicators (yfinance, close 2026-11-11) | OK |
| Profile / valuation (yfinance) | OK — pre-market quote 160.70 |
| SEC EDGAR quarterly revenue / net income | OK, but series has gaps (Jan-2025, Jan-2026 quarters missing) |
| SEC filings, last 10 days | none in packet (coverage not independently confirmed) |
| **News, last 7 days** | **UNAVAILABLE — fetch failed (proxy 403).** The cause of the selloff could not be identified. |
| Social sentiment | not collected |

## Market regime — neutral (0.65)
QQQ below its 50-day but above its 200-day; 21-day return -7.15% (just short of the -8% risk-off line).
VIX 18.33 (1y percentile 0.61). **Semis are the weak spot:** SMH below 50- and 200-day, 21-day -13.8%;
XLK 21-day -11.2%. 10-year yield 4.998 (0.879 percentile). Leaders: XLV, XLP, XLY, XLF.

## Analyst cards
| Card | Score | Summary |
|---|---|---|
| Technical | -1 | Downtrend, setup **none**. Close 173.73 < SMA20 203.80 / SMA50 217.10 / SMA200 204.19. 21-day -24.0%, RSI14 28.7 (oversold), volume 2.6x average (463M and 429M shares on Nov 9-10). |
| Fundamentals | +1 | High quality, accelerating: last-quarter revenue YoY +105.9%, net income YoY +125.9%, operating margin 65.2%, FCF 41.8B vs cash 62.5B / debt 38.9B. Trailing P/E 21.96, forward P/E 10.91. Short interest 1.2%. |
| News | 0 | News unavailable. Only known catalyst: **earnings 2026-11-17** (3 business days) — binary event. |
| Sentiment | -1 | Price-driven bearish tape; analyst consensus still very bullish (mean 1.39, 56 analysts), so no analyst capitulation. |

## Reference levels (from the technical card — stale at today's open)
| | Level |
|---|---|
| Entry zone | 170.0 – 174.0 (ref. 172.0) |
| Stop | 163.4 (below 165.89 swing low; 52-week low ~163.90) |
| Target | 194.9 (Nov 6 high / gap fill) |
| Reward/risk | ~2.66 |
| Pre-market quote | **160.70 — about 7.5% below the close and already below the stop** |

## Debate
**Strongest bull points**
1. Quality at a low multiple: revenue +105.9% YoY, 65% operating margin, forward P/E 10.91, low dilution risk.
2. Capitulation-style volume with RSI 28.7: a reclaim of 165.89 would be a valid bounce trigger toward 194.9.

**Strongest bear points**
1. No setup, confirmed downtrend, and the pre-market quote has already broken the stop and swing low — the long levels are void at the open.
2. Earnings on 2026-11-17 (beta 2.25, ATR 5.0%) plus an unexplained ~24% drawdown in a weak semis tape: any entry now is a gap bet with missing information.

The bull conceded the timing (upside probability cut to 0.20); the bear dropped its dealbreaker and argued on timing only.

## What would change the call
A close back above **165.89** after the **2026-11-17** earnings print. At that point the levels should
be rebuilt from new prices (`/deep-dive NVDA` again) rather than reusing these. A successful news pull
explaining the selloff would also be needed.

## Files
`regime_view.json`, `packets/NVDA.json`, `cards/`, `debate/`, `research/NVDA.json`, `proposals.json`.
