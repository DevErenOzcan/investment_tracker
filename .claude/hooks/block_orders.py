#!/usr/bin/env python3
"""PreToolUse hook: blocks any command that looks like order placement or broker access.

The system is a decision-support tool; the owner places orders themselves.
"""
import json
import re
import sys

PATTERNS = [
    r"\balpaca\b", r"\bib_insync\b", r"\bibapi\b", r"\bib-?gateway\b", r"\brobin_?stocks\b",
    r"\btradier\b", r"\bwebull\b", r"\bdegiro\b",
    r"place_?order", r"submit_?order", r"create_?order", r"/v2/orders", r"/orders\b",
    r"\bccxt\b",
]
RX = re.compile("|".join(PATTERNS), re.IGNORECASE)


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001
        return 0
    ti = data.get("tool_input", {}) or {}
    text = " ".join(str(ti.get(k, "")) for k in ("command", "url", "content", "file_path"))
    m = RX.search(text)
    if m:
        print(f"Blocked: '{m.group(0)}' looks like order placement or broker access. This system "
              "never places orders; write the recommendation to the report and let the owner decide.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
