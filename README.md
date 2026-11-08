# investment_tracker

A Claude Code agent team that scans NASDAQ twice a day (before the open and before the close),
finds stocks worth a closer look, and proposes how to weight them by risk and expected return.

- Rules and flow: [CLAUDE.md](CLAUDE.md)
- Sizing base: a notional portfolio of 1,000 units (`config/portfolio.yaml`). Outputs are weights;
  scale them to your own account outside the repo.
- Horizon: swing (a few days to a few weeks). Risk per trade: 0.75% of portfolio value (`config/risk.yaml`).

## Quick start
```bash
pip install -r requirements.txt
python -m pytest -q
# inside Claude Code:
/scan-premarket force
```

## Recording positions
When you open a position, add it to `state/portfolio.json` in notional units:
```json
{"ticker": "NVDA", "units": 80, "entry_price": 190.2, "entry_date": "2026-11-10",
 "stop": 178.0, "target": 215.0, "sector": "Technology"}
```
and reduce `cash_units` by the same amount. The system only reads this file.

## Data sources
Nasdaq Trader symbol directory, yfinance, Stooq (fallback), SEC EDGAR. SEC requires a contact
User-Agent: set the `SEC_USER_AGENT` environment variable to "Full Name email@example.com".

Based on [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) (Apache-2.0).
This software does not give investment advice.
