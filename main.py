#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Two Lines to Your Past Self — make.fun entry.

Writes exactly two lines to /output/entry.txt:

  Line 1 warns the past self about one specific moment.
  Line 2 says in one sentence why that moment mattered.

The text is fixed and deterministic: the entry is the text itself,
so the program writes the same two lines on every run.
"""

import os
import sys

# The entry text: two lines, two sentences, 1-280 characters.
ENTRY_TEXT = (
    "Don't send that 2 a.m. text to her \u2014 you already know the answer, "
    "and she already knows you know.\n"
    "The silence after it cost you three years of friendship "
    "you never got back.\n"
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def validate(text: str) -> None:
    """Check the text against the competition gate before writing it."""
    stripped = text.strip()
    if not MIN_CHARS <= len(stripped) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(stripped)}"
        )
    if not stripped:
        raise ValueError("entry must not be only whitespace")
    lines = stripped.splitlines()
    if len(lines) != 2:
        raise ValueError(f"entry must be exactly two lines, got {len(lines)}")


def main() -> int:
    # Write exactly the validated text plus one trailing newline, so the
    # file on disk is byte-for-byte what validate() approved.
    text = ENTRY_TEXT.strip() + "\n"
    validate(text)
    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text.strip())} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
