#!/usr/bin/env python3
"""Write one office joke to /output/entry.txt.

Chosen joke: the boss "respects" a Do Not Disturb status by naming the
meeting "Sorry to Disturb". The setup is a universal office truth (DND
gets ignored), the turn is the surprise — the polite meeting title itself —
and the punchline lands last, in one tight line.
"""

import os
import sys

JOKE = "My boss respected my “Do Not Disturb” status by naming the meeting “Sorry to Disturb.”"


def main() -> int:
    if not JOKE or not JOKE.strip():
        return 2
    if len(JOKE) > 200 or "\r" in JOKE or "\n" in JOKE:
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
