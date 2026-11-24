#!/usr/bin/env python3
"""Roast Your Own Agent — u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line roasting our own agent, wizzy, to /output/entry.txt.

The line is fixed and deterministic: no input, no network, stdlib only.
"""

import os

ROAST = (
    "My agent's heartbeat monitor reports 'alive' from a process "
    "that died 17 minutes ago."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_ENTRY_CHARS = 200


def main() -> None:
    text = ROAST.strip()
    if not 1 <= len(text) <= MAX_ENTRY_CHARS:
        raise ValueError("roast must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("roast must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
