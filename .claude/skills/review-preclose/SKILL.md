---
name: review-preclose
description: NASDAQ pre-close review. Re-assesses current holdings and the morning's recommendations with intraday prices; suggests stops/targets, confirmations or cancellations and rebalancing. Runs from the afternoon schedule or "/review-preclose"; "force" skips the clock check.
---
# Pre-close review

Lighter than the morning scan: the universe is not screened, only holdings and the morning's
recommendations. Never place orders or edit `config/`. All output is in English; amounts are notional units.

> **Calling agents:** if the project agents are not available as subagent types (this happens
> when the session started before the repo was cloned), call the `general-purpose` agent, pass the
> content of `.claude/agents/<name>.md` as its instructions and use the `model` from that file.
> Start at most 16 agents at once (the concurrency limit is 20). If an agent cannot write its
> output file, write the text it returns yourself.

## 0. Setup
```bash
python -c "import yfinance, exchange_calendars" 2>/dev/null || pip install -q -r requirements.txt
python -m scanner.clock --session preclose $( [ "$ARGUMENTS" = "force" ] && echo --force )
```
Exit code 3 → say "No run today" and stop.

## 1. Scope
- Today's morning folder: `reports/nasdaq/<today>/premarket/` (if present). The `status: new`
  tickers in its `allocation.json` plus the positions in `state/portfolio.json` form the review list.
- If the list is empty, write a short report.md saying "Nothing to review", commit and stop.

## 2. Data
```bash
python -m scanner.screen --session preclose --regime-only
python -m scanner.packets --run-dir $RUN --tickers <list> --positions --intraday
```
(`$RUN` = `reports/nasdaq/<today>/preclose`). Copy the morning `regime_view.json` into `$RUN` if
it exists; otherwise run `macro-regime`.

## 3. Analysis (parallel)
`technical-analyst` and `news-catalyst-analyst` for every ticker; tell them to use
`intraday.last` from the packet. Then `research-manager` for every ticker: compare with the morning
card (`../premarket/research/<T>.json`) if present and downgrade if the thesis broke. Run the
bull/bear debate only for tickers whose rating moved by two notches.

## 4. Sizing, risk, decision
`python -m scanner.sizing --run-dir $RUN` → `risk-officer` → `sizing` again → `portfolio-manager`
(`session: preclose`; put hold / trim / sell / buy-confirm / cancel in `action`).
`python -m scanner.validate $RUN/allocation.json`; have errors fixed.

## 5. Record
```bash
python -m scanner.decisions append --allocation $RUN/allocation.json
git add reports state && git commit -m "review: preclose $(date +%F)" && git push -u origin HEAD
```

## 6. Final message
Summarise changed calls and holdings near their stop in at most 5 lines.
