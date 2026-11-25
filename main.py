#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — entry program.

DRAFT -> REVISED: the draft line was

    "Error: unbalanced load. I shook myself apart trying to wash one
    hoodie and a single sock, so I stopped."

Three real improvements in the revision below:

1. "Error:" became "ERROR:" — a real machine error shouts in caps,
   so the line now opens in the appliance's own voice instead of a
   polite lowercase label.
2. "I shook myself apart trying to wash" became "I am shaking myself
   apart over" — present tense puts the fault happening right now,
   and "over one hoodie and a single sock" names the exact absurd
   cause of a genuine unbalanced-load error instead of narrating it
   from after the fact.
3. "so I stopped" became "Spin cycle refused." — the punchline is
   now the machine's own flat refusal, naming the real consequence
   (no spin) instead of a vague stop, so the joke closes on the
   appliance going on strike.

The final line is 104 characters, one line, no trailing newline.
"""

import os

ENTRY = "ERROR: Unbalanced load. I am shaking myself apart over one hoodie and a single sock. Spin cycle refused."

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must have no leading/trailing whitespace"
assert ENTRY.strip(), "entry must not be only whitespace"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
