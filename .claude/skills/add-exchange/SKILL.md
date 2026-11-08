---
name: add-exchange
description: Guide for adding a new exchange (e.g. Borsa Istanbul, NYSE). Prepares the exchange config, the universe source and the schedules.
---
# Adding an exchange

1. Copy `config/exchanges/nasdaq.yaml` to `config/exchanges/<code>.yaml` and edit:
   - `calendar`: exchange_calendars code (Borsa Istanbul = `XIST`, NYSE = `XNYS`).
   - `timezone`, `currency`, `symbol_suffix` (Borsa Istanbul: `.IS`), `benchmark` (Borsa Istanbul: `XU100.IS`).
   - `universe`: for exchanges other than Nasdaq Trader use `source: csv` and
     `path: config/universe/<code>.csv` (columns: symbol,name,market_category). Build the list with the owner.
   - `filters`: price, traded value and market cap thresholds in local currency.
   - `regime_symbols`: local index and sector indices.
2. SEC EDGAR covers US companies only; `sec_fundamentals` stays empty elsewhere.
3. Add the new data hosts to the environment's network access (needs the owner's approval).
4. Call everything with `--exchange <code>`, e.g. `python -m scanner.clock --session premarket --exchange <code>`.
5. Create two schedules in the exchange's time zone (about 50 min before the open and 70 min before the close).
6. Run `pytest` and do one manual run with `force`.
