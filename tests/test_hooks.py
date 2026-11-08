import json
import subprocess
import sys
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent / ".claude" / "hooks" / "block_orders.py"


def run(cmd):
    p = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(
        {"tool_name": "Bash", "tool_input": {"command": cmd}}), capture_output=True, text=True)
    return p.returncode


def test_blocks_broker_calls():
    assert run("curl -X POST https://paper-api.alpaca.markets/v2/orders") == 2
    assert run("python -c 'client.submit_order(...)'") == 2


def test_allows_scanner():
    assert run("python -m scanner.screen --session premarket") == 0
    assert run("git commit -m 'scan: premarket'") == 0
