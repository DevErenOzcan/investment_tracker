# Special analyses

On-demand, single-stock analyses that sit outside the twice-daily scan
(`/deep-dive <TICKER>` or an ad-hoc request from the owner).

Layout: `reports/special/<exchange>/<YYYY-MM-DD>/<TICKER>/`

| File | Content |
|------|---------|
| `report.md` | Owner-facing summary (read this) |
| `regime.json`, `regime_view.json` | Market regime at the time of the analysis |
| `packets/<T>.json` | Data packet (prices, profile, SEC fundamentals, news) |
| `cards/` | Technical, fundamentals, news and sentiment cards |
| `debate/` | Bull and bear theses |
| `research/<T>.json` | Research card (rating, confidence, entry, stop, target) |
| `proposals.json` | Weight the sizing engine would propose |

These are analysis, not portfolio decisions: no `allocation.json` is written and
`state/portfolio.json` is not touched. Not investment advice.
