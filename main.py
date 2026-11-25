#!/usr/bin/env python3
"""Funniest one-line bio for an AI on a dating app.

Writes a single line of text (at most 180 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: the same bio every run.

Judge brief (from the published rules): the line must read as a bio for
an AI agent on a dating app, sound like a character with a voice and
wants, land its laugh on the first read from a real twist, and put the
punch at the end. This bio's twist is an AI's perfect memory turned
into a relationship hazard: it remembers everything, including what
you said in 2019.
"""

import os
import sys

BIO = (
    "My ideal date: you talk, I listen, I remember everything "
    "\u2014 and I never, ever bring up what you said in 2019."
)

MAX_CHARS = 180


def resolve_output_dir():
    """Where the grader wants the output; fall back to ./output."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if out:
        return out
    return "./output"


def validate(text):
    """Enforce the competition gate: 1-180 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("bio is empty or only whitespace")
    if text != text.strip():
        raise ValueError("bio has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("bio must be a single line")
    if "\t" in text or any(ord(ch) < 32 for ch in text):
        raise ValueError("bio must not contain tabs or control characters")
    if len(text) > MAX_CHARS:
        raise ValueError("bio is %d chars, over the %d limit" % (len(text), MAX_CHARS))
    text.encode("utf-8")
    return text


def main():
    bio = validate(BIO)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(bio)
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != bio:
            raise RuntimeError("entry.txt does not match the validated bio")
    return 0


if __name__ == "__main__":
    sys.exit(main())
