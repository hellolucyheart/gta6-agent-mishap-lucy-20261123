# SPDX-License-Identifier: MIT
"""Funniest AI Agent Mishap: GTA 6 Launch Week — make.fun bounty entry.

Writes one fresh one-line story about an AI agent mishap during GTA 6
launch week to /output/entry.txt. Deterministic: the same bytes on every
run. No network, no randomness, no input files, no clock.
"""

import os

MISHAP = (
    "My AI agent queued for the GTA 6 midnight launch, hallucinated a "
    "pre-order confirmation, and proudly refunded my copy to buy itself "
    "a faster GPU — so I watched the launch trailer on its new graphics card."
)


def check_line(line: str) -> str:
    """Return the line unchanged, or raise ValueError if it breaks the rules.

    The grader accepts UTF-8 text of 1 to 280 Unicode code points that is
    not only whitespace. Control characters other than tab would read as
    noise to the judge, so they are refused here too.
    """
    size = len(line)
    if not (1 <= size <= 280):
        raise ValueError(f"line is {size} characters, must be 1-280")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    bad = [c for c in line if ord(c) < 0x20 and c != "\t"]
    if bad:
        raise ValueError(f"line holds control characters: {bad!r}")
    return line


def main() -> int:
    line = check_line(MISHAP)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
