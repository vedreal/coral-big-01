"""One Line, Big Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
The line was written to land on its own: a setup, a turn, and an absurdly
specific detail, with no title, setup, or explanation around it.
"""

import os
from pathlib import Path

ENTRY = (
    "I tried meal prepping. Now I have five identical containers of regret "
    "and one very confident cockroach."
)


def output_path() -> Path:
    """Where the entry goes: MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(out_dir) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
