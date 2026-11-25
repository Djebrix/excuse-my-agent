#!/usr/bin/env python3
"""Write the entry line to /output/entry.txt (stdlib only, deterministic)."""
import os

LINE = "I'm sorry \u2014 I hit my token limit mid-sentence, forgot the deadline entirely, and confidently hallucinated a calendar where it was still next Tuesday, and I believed it."

OUT = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
