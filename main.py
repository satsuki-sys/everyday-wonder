"""Everyday Wonder — make.fun entry.

Writes a single sentence (at most 200 characters) about a small moment
of wonder in everyday life to /output/entry.txt.
"""

import os

ENTRY = (
    "The escalator handrail moves faster than the steps, "
    "so for thirty seconds my hand is travelling without me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
