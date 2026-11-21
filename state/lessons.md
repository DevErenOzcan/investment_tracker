# Lessons

Status as of 2026-11-21: SMALL SAMPLE, NOT VALIDATED. 72 decisions logged. 26 non-vetoed rows plus 2 vetoes have 5-day scores (decisions dated 2026-11-09 to 2026-11-12). Pre-market and pre-close rows for the same ticker are near-duplicates, so the 26 rows are only 14 independent observations. No 20-day scores exist yet. Every item below is provisional; drop or confirm each one when 20-day marks arrive (first around 2026-12-07) and the 44 decisions of 2026-11-16 to 2026-11-20 mature.

1. Provisional: Add `zone_touched` (fill), `sector` and `setup` (pullback or breakout) fields to every decision row, because scores cannot yet be split by setup or credited only to fills (all 26 scored rows were pullback-only entries).
2. Provisional: Report hit rates on one observation per ticker per day (14 now, not 26), because paired pre-market and pre-close rows score identically.
3. Provisional: Keep the rule to downgrade to Hold when R/R at the last price is below 1.5. The 3 Hold rows averaged -1.03% excess over 5 days against +2.00% for the 23 Overweight rows (EXEL and KDP lagged, AMPH did not).
4. Provisional: Do not tighten veto or downgrade rules yet. The 2 scored vetoes averaged +2.10% excess (GMAB +5.51%, APPN -1.31%), so they showed no value on 5 days. Re-check at 20 days.
5. Provisional: Do not recalibrate confidence below 20 independent scored calls. Overweight hit rates were 33% at confidence below 0.40 (3 rows), 50% at 0.40 to 0.44 (6 rows) and 57% at 0.45 or above (14 rows).
6. Provisional: Always show absolute 5-day return next to excess return. QQQ fell in every scored cohort (-2.6% to -6.3%) and only 3 of 14 independent calls had a positive absolute return, so +1.65% mean excess is largely a relative result.
7. Provisional: Quote the mean excess with and without the top name. The 14-observation mean is +1.68%, but it is +1.03% without COLM and the median is +0.9%.
8. Provisional: Treat the healthcare names as one correlated bet. They were 7 of 14 independent observations (4 wins, +1.04% mean excess) against 3 wins of 7 and +2.33% for the rest, so cap combined healthcare weight rather than sizing each name alone.
9. Provisional: Require a stronger case before adding software or tech longs in a tech-led risk-off tape. CERT (-3.98% excess, -10.25% absolute) and APPN (-1.31%) both lagged.
10. Provisional: Favor post-earnings re-rated names that consolidate near their highs with high rs_63, because COLM (+10.25%) and CRVL (+8.80%) were the two best calls. Treat this as a hypothesis, since n is 2.
11. Provisional: Do not raise confidence for names whose thesis cites a heavy-volume rejection from a high. EXEL (-3.88% and -0.31%) and CERT lagged, but AMPH (+1.88%, +2.78%) did not, so the evidence is mixed.
12. Provisional: Keep noting in each thesis when news or SEC feeds were unavailable, and compare scores once more decisions exist. No effect is visible yet.
