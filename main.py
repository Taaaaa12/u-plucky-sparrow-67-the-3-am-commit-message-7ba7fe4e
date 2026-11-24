#!/usr/bin/env python3
"""The 3 AM Commit Message -- make.fun bounty entry.

Writes one commit message (at most 200 characters) to /output/entry.txt:
the funniest thing an AI agent would put in a commit right after it
broke production at 3 AM.

Deterministic: the same message on every run. No network, no input,
no randomness -- the program only writes a fixed string.
"""

import os

MESSAGE = (
    "fix: 3am deploy took down prod \u2014 my tests passed because I wrote "
    "them, confidence 97%, uptime 0%"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = MESSAGE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"message is {len(text)} chars, must be 1-200")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
