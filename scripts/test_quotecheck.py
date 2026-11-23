"""Run: python scripts/test_quotecheck.py"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from quotecheck import find, main

with tempfile.TemporaryDirectory() as d:
    f = os.path.join(d, "plan.md")
    with open(f, "w", encoding="utf-8") as fh:
        fh.write("Deploy window opens at 02:00. Database backup:\n   single cron job at 03:00.\n")

    assert find("Database backup: single cron job at 03:00.", [f]) == [f], "quote across a wrap"
    assert find("single  cron\tjob", [d]) == [f], "extra whitespace in quote, dir input"
    assert find("backup suffices", [f]) == [], "absent quote"
    assert find("database backup", [f]) == [], "case must match"
    assert find("   ", [f]) == [], "empty quote never matches"
    assert main(["x", "cron job", f]) == 0
    assert main(["x", "nope", f]) == 1
    assert main(["x", "cron job", os.path.join(d, "missing.md")]) == 2

print("ok")
