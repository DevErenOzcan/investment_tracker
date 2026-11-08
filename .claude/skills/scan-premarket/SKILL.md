---
name: scan-premarket
description: Full NASDAQ pre-market scan. Screens the universe, analyses finalists with the agent team, runs them through the risk engine and produces target portfolio weights and an English report. Runs from the morning schedule or "/scan-premarket"; the "force" argument skips the clock check.
---
# Pre-market scan

Follow every step in order. For agent steps, call the matching subagent with the Task/Agent tool and
state the `run-dir` path and ticker explicitly in every call. Send independent agent calls **in
parallel in the same message**. Never place orders, connect to a broker or edit `config/`.
All output (cards, report, final message) is in English. Amounts are notional units, never currency.

> **Calling agents:** if the project agents are not available as subagent types (this happens
> when the session started before the repo was cloned), call the `general-purpose` agent, pass the
> content of `.claude/agents/<name>.md` as its instructions and use the `model` from that file.
> Start at most 16 agents at once (the concurrency limit is 20). If an agent cannot write its
> output file, write the text it returns yourself.

## 0. Setup
```bash
python -c "import yfinance, exchange_calendars" 2>/dev/null || pip install -q -r requirements.txt
python -m scanner.clock --session premarket $( [ "$ARGUMENTS" = "force" ] && echo --force )
```
If the exit code is 3 (holiday / outside the window), write **nothing**, say "No run today: <reason>" and stop.

## 1-3. Screening funnel (code)
```bash
python -m scanner.screen --session premarket
```
Note the `run_dir` in the output (`$RUN` below). On error retry once; if it fails again write the
error to `$RUN/ERROR.md`, commit and stop. If `candidates` is 0, write the report as "no candidates".

## 4. Regime and triage (agents)
1. `macro-regime` → `$RUN/regime_view.json`
2. `triage-analyst` (number of finalists from `config/exchanges/nasdaq.yaml` → `screen.finalists`) → `$RUN/triage.json`

## 5. Data packets and deep analysis
```bash
python -m scanner.packets --run-dir $RUN --tickers <finalists,comma-separated> --positions
```
Then **in parallel** for every finalist: `technical-analyst`, `fundamentals-analyst`,
`news-catalyst-analyst` (plus `sentiment-analyst` from Phase 3). When all are done, run
`bull-researcher` and `bear-researcher` in parallel for every finalist (one round). Then
`research-manager` for every finalist → `$RUN/research/<T>.json`.
If a card is missing or invalid JSON, call that agent once more; if it still fails, continue to the
research-manager with a "data missing" note (it is expected to return REVIEW).

## 6. Sizing and risk
```bash
python -m scanner.sizing --run-dir $RUN
```
`risk-officer` → `$RUN/risk_review.json`, then rerun the engine with the vetoes applied:
```bash
python -m scanner.sizing --run-dir $RUN
```

## 7. Portfolio decision
`portfolio-manager` → `$RUN/allocation.json` and `$RUN/report.md`.
```bash
python -m scanner.validate $RUN/allocation.json
```
On errors, give them to the portfolio-manager to fix (at most 2 attempts).

## 8. Record and push
```bash
python -m scanner.decisions append --allocation $RUN/allocation.json
git add reports state && git commit -m "scan: premarket $(date +%F)" && git push -u origin HEAD
```
If the push fails on a network error, retry after 2, 4 and 8 seconds.

## 9. Final message
Return the "Summary" and "Actions" sections of `report.md` verbatim. This message shows in the notification.
