#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes exactly one funny line to /output/entry.txt."""
import os

JOKE = "My therapist prescribed closure, so I ghosted her mid-sentence."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
