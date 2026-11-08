---
name: weekly-review
description: Weekly performance review. Scores the decision log and updates lessons with the performance-reviewer. Runs from the Saturday schedule or "/weekly-review".
---
# Weekly review

```bash
python -c "import yfinance" 2>/dev/null || pip install -q -r requirements.txt
python -m scanner.decisions score
```
Then call the `performance-reviewer` agent: it reads `state/scorecard.csv`, `state/decisions.jsonl`
and `state/lessons.md`, and writes `state/lessons.md` and `reports/weekly/<today>.md` (English).

```bash
git add state reports && git commit -m "weekly review $(date +%F)" && git push -u origin HEAD
```
Final message: number of scored decisions, mean 5- and 20-day excess return, hit rate and the top 3 lessons.
