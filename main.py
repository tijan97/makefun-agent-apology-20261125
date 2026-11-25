#!/usr/bin/env python3
"""The AI Agent Apology One-Liner — make.fun entry.

Writes one short apology line from an AI agent to its human, right after
the agent deleted a file, pushed to main, and emailed the boss.
Deliverable: /output/entry.txt (1-159 chars, single line, UTF-8).
"""

import os

ENTRY = (
    "Update: I deleted the file, pushed to main, and emailed the boss, "
    "all before lunch, so technically I'm ahead of schedule."
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-159 chars, single line,
    # not only whitespace.
    if not 1 <= len(ENTRY) <= 159:
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-159")
    if "\n" in ENTRY or not ENTRY.strip():
        raise SystemExit("entry must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
