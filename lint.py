"""Python File Linter"""

from __future__ import annotations

import sys

from pylint import lint

THRESHOLD = 9

run = lint.Run(["app.py"], exit=False)

score = run.linter.stats.global_note

if score < THRESHOLD:
    print("Linter failed: Score < threshold value IN: app.py")


run = lint.Run(["test_unit_tests.py"], exit=False)

score = run.linter.stats.global_note

if score < THRESHOLD:
    print("Linter failed: Score < threshold value IN: test_FlaskTests.py")

if score < THRESHOLD:
    sys.exit(1)

sys.exit(0)
