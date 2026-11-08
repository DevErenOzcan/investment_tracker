#!/usr/bin/env python3
"""Stop hook: if an allocation.json was written in the last 4 hours, validate it against the
schema and risk limits. If invalid, block the session from ending and return the errors."""
import json
import os
import subprocess
import sys

root = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))
try:
    payload = json.load(sys.stdin)
except Exception:  # noqa: BLE001
    payload = {}

r = subprocess.run([sys.executable, "-m", "scanner.validate", "--latest", "--max-age-min", "240"],
                   cwd=root, capture_output=True, text=True)
if r.returncode == 2:
    if payload.get("stop_hook_active"):
        # Still invalid on the second attempt: do not loop, leave a warning.
        print("WARNING: allocation.json is still invalid:\n" + r.stderr, file=sys.stderr)
        sys.exit(0)
    print("allocation.json failed risk validation. Fix it with the portfolio-manager and "
          "run `python -m scanner.validate`:\n" + r.stderr, file=sys.stderr)
    sys.exit(2)
sys.exit(0)
