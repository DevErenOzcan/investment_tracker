# NVDA special analysis — 2026-11-12 (pre-market, v2 with news)

> Analysis only, not a portfolio decision and not investment advice. No `allocation.json` written;
> `state/portfolio.json` untouched. Sizing base: notional 1,000 units.
>
> **v2** replaces the morning version, which ran without news (feed blocked). News access was
> enabled and the news, sentiment, debate and research steps were re-run.

## Verdict
**Rating: Hold (watchlist) · confidence 0.30 · debate winner: bear (dealbreaker) · engine-proposed weight: 0%**
(`scanner.sizing`: 0 positions, cash weight 1.0 — Hold ratings do not open positions.)

The selloff is governance-driven, not fundamental. Reports (unconfirmed by the company) say NVIDIA's
board is weighing removing CEO Jensen Huang over alleged ties to a suspected Chinese spy and a second
reported affair. That is a binary event, and earnings on 2026-11-17 land in the same window. The
bear's dealbreaker caps the rating at Hold. Fundamentals remain strong.

## What drove the selloff (news card, score -2, binary_event = true)
| Date | Event | Status |
|---|---|---|
| Nov 5 | -9.3% on 306M shares (vs ~131M avg) | **Trigger not identified** in the packet (title-only items) |
| Nov 8 | Board investigating Huang's links to an alleged spy (Barron's) | Reported |
| Nov 9-10 | Gap down (open 173.07 vs 186.64), "the Jensen Huang affair"; low 165.89 on 429M shares | Reported |
| Nov 11 (late) | Board reportedly preparing to oust Huang; second reported affair | Reported, unconfirmed |
| Nov 12 | Futures fall; analysts cut ratings / "back away"; Beijing warns US on tech curbs; 10-year yield touches 5% | Headlines |

No company statement and no 8-K (Item 5.02) in the SEC filings for the last 10 days. Most items are
headline-only (Google News RSS), so analyst names and new targets are not available. The profile's
consensus (mean 1.39, target 309.72) is probably stale.

## Data used
| Source | Status |
|---|---|
| Prices, indicators (yfinance, close 2026-11-11) | OK — pre-market quote ~160.4 |
| Profile / valuation (yfinance) | OK |
| SEC EDGAR quarterly revenue / net income | OK, series has gaps (Jan-2025, Jan-2026 quarters missing) |
| SEC filings, last 10 days | none |
| News, last 7 days | **OK** — Yahoo Finance (Nov 12) + Google News RSS (Nov 5-12, titles only) |
| Social sentiment | not collected |

## Market regime — neutral (0.65)
QQQ below its 50-day, above its 200-day; 21-day -7.15%. VIX 18.33 (0.61 percentile).
Semis weak: SMH below 50- and 200-day, 21-day -13.8%; XLK 21-day -11.2%. 10-year yield 4.998.

## Analyst cards
| Card | Score | Summary |
|---|---|---|
| Technical | -1 | Downtrend, setup none. Close 173.73 < SMA20/50/200. 21-day -24%, RSI14 28.7, volume 2.6x. |
| Fundamentals | +1 | Revenue YoY +105.9%, net income YoY +125.9%, operating margin 65.2%, forward P/E 10.91, cash > debt. |
| News | **-2** | CEO-ouster reports (unconfirmed) + earnings 2026-11-17 = binary event. |
| Sentiment | -1 | Bearish, not crowded (short interest 1.2%); medium contrarian risk — sharp rebound possible if the CEO question resolves. |

## Conditional levels (only if price reclaims 165.89)
The technical card's original levels (entry 170-174, stop 163.4) are void: the pre-market quote is
below the stop, the 165.89 swing low and the 52-week low (~163.9). The research manager reset them:

| | Level | Derivation |
|---|---|---|
| Entry zone | 165.89 – 170.0 (ref. 167.95) | reclaim of the swing low |
| Stop | 156.03 | pre-market 160.38 − 0.5 × ATR (8.70) |
| Target | 194.9 | Nov 6 high / gap fill |
| Reward/risk | ~2.3 | expected return -7.1% / +16.0% |

## Debate
**Strongest bull points**
1. The business is not the problem: +106% revenue growth, 65% operating margin, forward P/E 10.9, low dilution risk.
2. The trigger is reported, not confirmed (no 8-K, no company statement); a denial or quick resolution could reverse a headline-driven, oversold move (RSI 28.7, 2.6x volume).

**Strongest bear points (won)**
1. A pending, binary governance outcome (ouster or not) plus earnings in the same window — with beta 2.25 any entry is a gap bet.
2. The chart is broken: price below all averages and below the swing low, 52-week low and stop; semis and tech lag; analysts are cutting.

The bull conceded there is no entry today; its case needs a reclaim of 165.89 **and** a confirmed resolution of the CEO question.

## What would change the call
1. A company statement / 8-K resolving Huang's status (either way removes the binary risk).
2. The 2026-11-17 earnings print.
3. A close back above 165.89.
Then re-run `/deep-dive NVDA` with fresh prices.

## Data discrepancies noted
- Pre-market quote varied during the morning (160.70 → 160.38); the packet's last value was used.
- 52-week low: 163.90 (price history) vs 164.27 (profile).
- Profile `regularMarketPreviousClose` 168.796 does not match the 2026-11-11 close of 173.73.

## Files
`regime_view.json`, `packets/NVDA.json`, `cards/`, `debate/`, `research/NVDA.json`, `proposals.json`.
