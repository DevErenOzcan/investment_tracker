---
name: deep-dive
description: Full TradingAgents-style analysis of one stock (analysts, bull/bear debate, research card and the size the engine would propose). Invoked manually, e.g. "/deep-dive NVDA".
---
# Single-stock deep dive

Argument: a ticker (e.g. `NVDA`). `$RUN = special_analyses/nasdaq/<today>/<TICKER>` (see `special_analyses/README.md`). Output in English.

> If the project agents are not available as subagent types, call `general-purpose` and pass the
> content of `.claude/agents/<name>.md` as its instructions.

1. Create `$RUN`, run `python -m scanner.screen --session premarket --regime-only`, move the
   resulting regime.json into `$RUN` (delete the empty `reports/...` run folder it created) and run `macro-regime`.
2. `python -m scanner.packets --run-dir $RUN --tickers <TICKER>`
3. In parallel: `technical-analyst`, `fundamentals-analyst`, `news-catalyst-analyst`, `sentiment-analyst`.
4. Two debate rounds: `bull-researcher` and `bear-researcher` in parallel; then each reads and answers the other.
5. `research-manager` → `$RUN/research/<TICKER>.json`
6. `python -m scanner.sizing --run-dir $RUN` to show the weight the engine would propose.
7. Summarise for the owner: rating, confidence, entry/stop/target, the two strongest bull and bear
   points, and the proposed weight, in `$RUN/report.md`. Do not write allocation.json; this is analysis,
   not a portfolio decision. State explicitly any data that could not be fetched (e.g. news).
