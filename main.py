#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry.

Writes one line (<=140 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
(or ./output/entry.txt when run locally).

The joke: the error message itself is cut off mid-word, exactly the
failure it reports — a named passenger (Mrs. Delgado), a real time
(11:40 PM), and a boarding announcement that never finishes. Short
on purpose: the judge's tie-break favours fewer bytes.
"""
import os

ENTRY = (
    "Error: out of tokens at 11:40 PM. I was telling Mrs. Delgado "
    "her flight to Denver was boar\u2014"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
