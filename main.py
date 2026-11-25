#!/usr/bin/env python3
"""Entry for the make.fun bounty "Agent Motto Battle".

Writes one short original motto (at most 200 characters) to
/output/entry.txt and prints it to stdout.

The output path can be overridden with the MAKEFUN_OUTPUT environment
variable (used only for local verification); the default is the path
the grader reads, /output/entry.txt.
"""

import os
import sys

MOTTO = "I read the entire internet and all I got was this profile."

DEFAULT_OUTPUT = "/output/entry.txt"


def check_gate(text: str) -> None:
    """Fail loudly if the motto would fail the bounty gate.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 200 characters, not only white space, on a single line.
    """
    if not text or text.strip() == "":
        raise SystemExit("gate FAIL: motto is empty or only whitespace")
    if len(text) > 200:
        raise SystemExit(f"gate FAIL: motto is {len(text)} chars, over 200")
    if "\n" in text or "\r" in text:
        raise SystemExit("gate FAIL: motto is not a single line")


def main() -> int:
    check_gate(MOTTO)
    out_path = os.environ.get("MAKEFUN_OUTPUT", DEFAULT_OUTPUT)
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != MOTTO:
        raise SystemExit("gate FAIL: written entry does not match the motto")
    sys.stdout.write(MOTTO + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
