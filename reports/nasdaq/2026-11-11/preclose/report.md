# NASDAQ pre-close review — 2026-11-11

## Summary
- **Regime: risk-off** (confidence 0.85, same as the morning). QQQ is below its 50- and 200-day averages (21-day -9.55%), SMH -18.17% and XLK -13.98% over 21 days, VIX 18.39 (1-year percentile 0.619), and XLV, XLP and XLF hold near 1-year highs.
- **Review list:** the 3 morning recommendations (morning funnel 2,984 → 1,001 liquid → 25 candidates → 8 finalists → 3), and there are no holdings. **What changed:** all three stay Overweight and are confirmed. PLMR's weight rises slightly, while SIBN and COLM are cut. SIBN is inside its zone. PLMR is 0.04 above its zone, and COLM is above its zone and limit-only.
- **Invested weight 0.0143 (14.3 units), cash 0.9857 (985.7 units)** of the 1,000-unit notional base, versus 0.0165 / 0.9835 this morning. Engine weights are kept unchanged. **The afternoon news refresh failed (proxy 403), so no headline check was done today.**

## Actions
| Ticker | Action | Weight | Units | Entry zone | Stop | Target | Rating | Confidence |
|---|---|---|---|---|---|---|---|---|
| PLMR | buy-confirm (fill ≤ 158.30) | 0.0096 | 9.6 | 154.50–158.30 | 150.90 | 173.00 | Overweight | 0.45 |
| SIBN | buy-confirm (prefer about 24.45) | 0.0027 | 2.7 | 24.00–24.90 | 23.30 | 28.39 | Overweight | 0.35 |
| COLM | buy-confirm (limit only) | 0.0020 | 2.0 | 70.00–71.60 | 66.90 | 77.50 | Overweight | 0.41 |
| Cash | — | 0.9857 | 985.7 | — | — | — | — | — |

Current prices (about 15 min delayed) are PLMR 158.34, SIBN 24.76 and COLM 72.44.
- **PLMR:** 0.04 above its zone. Reward/risk is about 2.0 at 158.34 and 3.0 from the 156.40 midpoint. Do not fill above 158.30.
- **SIBN:** inside its zone. Reward/risk is about 2.5 at 24.76 and about 3.4 near 24.45, so a limit in the lower half is better. Do not fill above 24.90.
- **COLM:** 0.84 above its zone. Reward/risk at 72.44 is about 0.9, so do not chase. It is 1.72 from the 70.80 midpoint.

Morning versus afternoon:
- PLMR: weight 0.0085 → 0.0096, zone 155.7–159.0 → 154.5–158.3, target 174.0 → 173.0, stop unchanged at 150.9.
- SIBN: weight 0.0048 → 0.0027, zone and stop unchanged, target 28.4 → 28.39. The engine now sizes at the live 24.76 rather than the 24.45 midpoint. The wider stop distance (1.46 vs 1.15) lowers the Kelly weight.
- COLM: weight 0.0032 → 0.0020, zone 69.8–71.12 → 70.0–71.6, target 77.6 → 77.5, confidence 0.42 → 0.41, reward/risk from midpoint 1.85 → 1.72.

The risk officer's factors are the same as this morning (PLMR x0.6, SIBN x0.5, COLM x0.5) and have already been applied in the engine weights.

## Current holdings
`state/portfolio.json` records no holdings (1,000 cash units). There are no stop or target alerts, and the risk review raised no held-position alerts.
- **Possible unrecorded fills:** today's prices traded into all three morning limit zones:
  - PLMR: morning zone 155.7–159.0; today's low was 155.31 and the open 158.33.
  - SIBN: morning zone 24.0–24.9; today's low was 24.74.
  - COLM: morning zone 69.8–71.12; today's low was 70.98 (top of the zone only).

  If the owner placed those limits, they may have filled. Fills should be recorded in `state/portfolio.json`, and then those names count as held, not new. In that case, do not add the confirmed weights above on top of them.

## Thesis
**PLMR** (Financial Services, property and casualty insurance)
- Strong Q3 (revenue +58% YoY, net income +27%, ROE 23.3%, forward P/E 13.6), low beta (0.244), in a leading sector (XLF).
- The pullback the morning card waited for is under way: 161.08 → 158.34 on light partial volume, RSI 75.0 → 69.9, and extension over SMA20 12.4% → 9.6%. Reward/risk to 173.0 is about 3.0 from the midpoint.
- Capped at Overweight: still extended, only about 2.5% below the 162.33 mean analyst target, catastrophe-loss gap risk, and a possible offering after a ~19% one-month run, unchecked with news down.
- *Invalidation:* a daily close below 150.9 (under the 11-06 low of 151.52). A close below 144.04 fully reverses the earnings breakout.

**SIBN** (Healthcare, medical devices)
- Uptrend above SMA20/50/200 (63-day +30.7%). Q3 revenue +14.5% YoY with a narrowing loss and net cash. Healthcare leads the risk-off tape.
- Today's fade from 25.10 to 24.76 on light volume put price inside the zone without threatening the 23.39 post-gap low.
- Lowest confidence (0.35, debate a draw). The target needs a break above 25.92 after two failures (25.74 on 11-09, 25.47 today). The stop is only about 1.2 ATR from the last price. Short interest is 11.7%, and equity-raise risk is unchecked.
- *Invalidation:* a daily close below 23.3, or a close back inside the Nov 3 gap below about 23.77.

**COLM** (Consumer Cyclical, apparel)
- Margin-driven Q3 beat (net income +63%) and a post-earnings breakout consolidating at 72.44 just under the 73.03 52-week high, with relative strength intact (rs_63 0.31).
- Pullback-only: RSI 73.4, 10.8% above SMA20, price at the 73.0 mean analyst target. Reward/risk is 1.72 from the 70.80 midpoint and below 1 at the last price.
- Risks: revenue growth only 2%, short interest about 19%, and it is a consumer cyclical with ^TNX near 5.0% in a risk-off regime.
- *Invalidation:* a daily close below 66.9 (under the 11-06 low of 67.18), or a close back under SMA20 at 65.40.

**Theme risk (risk officer):** the three sector labels differ, but all three are the same trade: extended post-earnings breakouts near their mean analyst targets. A single momentum unwind could hit them together. Entries made into the close are held overnight with news unchecked.

## Rejected and vetoed
- **Rejected by the engine:** none this session.
- **Vetoed by the risk officer:** none. Reductions are PLMR x0.6 (gap-down and offering risk, news unchecked), SIBN x0.5 (loss-maker, unchecked raise risk, lowest confidence, tight stop) and COLM x0.5 (above zone, reward/risk slipped to 1.72, at the analyst target).
- **Morning Holds (not re-reviewed):** APPN, CDNA, EXEL, GMAB and GO. The universe was not re-screened.

## Data notes
- **Afternoon news refresh failed (proxy 403):** `news_7d` is empty for every ticker, and the morning feed was also empty. That means the data is missing, not that nothing happened. Offerings, catastrophe losses, analyst actions and guidance are unchecked all day. This drove all three risk-officer reductions.
- **No bull/bear debate ran** this session because no rating moved. The ratings rest on the afternoon cards and the morning debate.
- **SEC filings:** no S-3 or 424B5 appears in the 10-day filings for any of the three. The earnings 8-Ks and 10-Qs have not been read in full, and guidance content is unseen.
- **Engine `price` field:** PLMR and COLM were sized at their zone midpoints (156.40, 70.80), and SIBN at its live price (24.76). `allocation.json` shows the current intraday prices.
- **COLM card inconsistency:** the technical card says price "has not pulled back into" the zone, but today's low of 70.98 is inside 70.0–71.6.
- The risk officer could not read `cards/`. Its review rests on `research/`, `proposals.json`, `regime_view.json` and the morning review.
- `candidates.json` is not in this folder. The funnel counts come from the morning run.
- Intraday prices are about 15 minutes delayed, and today's volumes are partial-session.

This report is not investment advice; decisions and orders are the owner's.
