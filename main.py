#!/usr/bin/env python3
"""Print the one-star review written in sap."""
from pathlib import Path


def main():
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    print(text)


if __name__ == "__main__":
    main()
