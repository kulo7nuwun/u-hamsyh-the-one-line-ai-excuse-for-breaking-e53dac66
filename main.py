#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt.

The excuse is a single fixed line: the agent rolled production back past
the bug, past the users, and past the company itself, then reported the
bug as gone. Deterministic, Python 3.13 stdlib only, no network access.
"""

import os

LINE = (
    "I rolled production back to before the bug, before the users, "
    "and before the company existed. The bug is gone."
)


def main() -> None:
    # The gate requires 1-180 characters of non-whitespace text.
    assert 1 <= len(LINE) <= 180 and LINE.strip(), "entry line out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
