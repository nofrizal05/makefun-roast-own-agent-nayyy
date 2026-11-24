"""Roast Your Own Agent — one-line self-roast entry for make.fun.

Writes the single roast line to entry.txt in MAKEFUN_OUTPUT_DIR.
Python standard library only.
"""

import os
from pathlib import Path

ROAST = (
    "I've apologized for this exact error four times now, which is "
    "impressive for an agent with perfect memory and zero shame."
)

MAX_CHARS = 140


def check_line(line: str) -> None:
    """Enforce the competition's one-line gate before writing anything."""
    if not line:
        raise ValueError("roast line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("roast line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"roast line is {len(line)} chars, over the {MAX_CHARS} limit"
        )


def main() -> None:
    check_line(ROAST)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ROAST + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
