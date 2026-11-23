#!/usr/bin/env python3
"""Dad Joke Showdown — write one dad joke to /output/entry.txt.

The joke is a fixed, original line chosen after scoring six candidates
against the kit's judge brief (see CANDIDATES.md). This program validates
it against the competition gate — UTF-8 text, 1 to 200 characters, not
only white space — and writes it to /output/entry.txt.
"""

import os
import sys

JOKE = (
    "I told my son the money in our savings account is growing. "
    "He asked when we can pick it. "
    "I said, 'Son, interest takes time.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = JOKE.strip()
    if not text:
        print("error: joke is blank", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"error: joke is {len(text)} characters, over the 200 limit",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the write: read it back and confirm it is exactly the joke,
    # a single line, and still inside the gate.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("error: written file differs from the joke", file=sys.stderr)
        return 1
    if "\n" in written:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
