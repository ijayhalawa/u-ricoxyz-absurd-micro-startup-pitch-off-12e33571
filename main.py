#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes exactly one sentence -- a pitch for an absurdly specific
micro-startup for lazy AI agents -- to /output/entry.txt.

Stdlib only, no network, fully deterministic: the same bytes on
every run.
"""

import os

ENTRY = (
    "Apology-as-a-Service for lazy customer-support agents: "
    "pre-written 'sorry, I hallucinated' emails at $0.10 per apology, "
    "auto-sent with zero human oversight."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
