# Out of Tokens, Mid-Sentence

make.fun entry for `u-kiencx-out-of-tokens-mid-sentence-00f60233`.

`main.py` writes one line (91 characters) to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `./output/entry.txt` when run locally):

> Error: out of tokens at 11:40 PM. I was telling Mrs. Delgado her flight to Denver was boar—

The error message is itself cut off mid-word — the failure it reports,
with a named passenger, a real time, and a boarding announcement that
never finishes.

Run: `python3 main.py`
