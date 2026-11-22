#!/usr/bin/env python3
"""Writes one short text to /output/entry.txt for the
make-the-ai-judge-feel-curious-20261122-2311 bounty (stdlib only)."""

import os

TEXT = (
    "The lighthouse keeper leaves one window lit every night for a ship "
    "that sank a hundred years ago. Some nights, a light answers from "
    "the water, slow and patient, in the same rhythm. He has never once "
    "written down what it says."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
