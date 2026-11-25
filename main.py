#!/usr/bin/env python3
"""Print the one-star review in entry.txt, byte for byte.

The review is a thirsty houseplant's complaint, kept in entry.txt
so the text lives in one place. This script only locates that file
next to itself and writes its contents to stdout unchanged.
No stripping, no reformatting: what is in the file is what is printed.
"""

import sys
from pathlib import Path


def main() -> int:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    sys.stdout.write(entry_path.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
