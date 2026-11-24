#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes a single original one-line roast of our own agent to
/output/entry.txt. Fully deterministic: the same constant line on
every run, no randomness, no network, no environment input.
"""

import os

ROAST = (
    "Our agent hallucinated an entire API, wrote docs for it, "
    "then filed a bug report against itself for not implementing it."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
