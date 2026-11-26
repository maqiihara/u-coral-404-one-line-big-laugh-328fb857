#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
"""

import os

ENTRY = "My smoke detector only beeps at 3 a.m. I'm convinced it's unionized."


def validate(text):
    """Mirror the sealed scorer's gate: UTF-8 text of 1 to 200 characters,
    not only white space."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return True


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
