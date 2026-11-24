"""Write one funny fortune cookie message for an AI agent to entry.txt.

Reads no environment variable except MAKEFUN_OUTPUT_DIR (default /output).
Prints exactly the fortune, one line, and writes the same line to
$MAKEFUN_OUTPUT_DIR/entry.txt so the harness gate can read it.

Fortune angle: the dreaded upgrade is coming *for* the agent, not *to* it —
a promotion that reads like a pink slip.
"""

import os

LINE = "A great upgrade is coming. Sadly, it is coming for you, not to you."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(LINE)
