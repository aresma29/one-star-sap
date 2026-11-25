#!/usr/bin/env python3
"""Print the one-star review in entry.txt, byte for byte.

The review is a houseplant's complaint: one star, still thirsty.
This script keeps things simple — it reads the entry file sitting next
to it and writes its contents to stdout exactly as stored, so the
printed text always matches the submitted entry.
"""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
