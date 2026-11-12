# investment_tracker

A market-scanning and portfolio-allocation agent team that runs twice a day on NASDAQ.
Adapted from the TradingAgents architecture (TauricResearch, Apache-2.0). It uses no external LLM
API: every agent is a Claude Code subagent.

## Core rule
**LLMs produce judgement, code produces numbers.** Scores, volatility, position sizes and limit
checks are computed by the Python modules in `scanner/`. Agents only use numbers from the data
packets and never invent them. The portfolio-manager may move an engine weight by at most +/-25%.

## Sizing base
All sizing is against a **notional portfolio of 1,000 units** (`config/portfolio.yaml`). Reports
show weights and notional units only. Never write a currency amount or a real account size into
the repo, reports or messages.

## Flow
- `/scan-premarket` (08:41 ET): universe → filters → factor score → triage → analysts → bull/bear →
  research-manager → sizing → risk-officer → sizing → portfolio-manager → validate → commit.
- `/review-preclose` (14:52 ET): holdings and the morning's recommendations re-assessed with intraday prices.
- `/weekly-review` (Saturday): decisions scored against QQQ, `state/lessons.md` updated.
- `/deep-dive <TICKER>`: single-stock analysis (manual), written to `reports/special/`.

## Layout
- `config/` — exchange, risk and portfolio settings. **Agents must not edit `config/risk.yaml`.**
- `scanner/` — deterministic core (`python -m scanner.<module> --help`).
- `.claude/agents/` — 12 agents; `.claude/skills/` — workflows; `.claude/hooks/` — safety hooks.
- `state/portfolio.json` — notional holdings in units; **only the owner edits it.**
- `state/decisions.jsonl`, `state/scorecard.csv`, `state/lessons.md` — decision log and lessons.
- `reports/<exchange>/<date>/<session>/` — output of each run; the file to read is `report.md`.
- `reports/special/<exchange>/<date>/<TICKER>/` — on-demand single-stock analyses (`/deep-dive`).

## Safety
- The system **never places orders**; a PreToolUse hook blocks broker/order-like commands.
- A Stop hook validates the latest `allocation.json` against the risk limits.
- Reports are not investment advice.

## Development
```bash
pip install -r requirements.txt
python -m pytest -q
python -m scanner.clock --session premarket --at 2026-11-09T13:50:00Z
```
Language: everything in the repo and in analysis output is in English.
