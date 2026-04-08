"""Compact loose bullet lists in markdown files.

Removes blank lines between consecutive bullet list items (- prefix)
while preserving blank lines around the list boundaries (before first
item and after last item). Also handles nested lists and continuation
lines (indented text under a bullet).

Usage:
    python fix_loose_lists.py          # fix all *.md in corebook/
    python fix_loose_lists.py --check  # dry-run, report counts only
"""
import re
import sys
from pathlib import Path

COREBOOK = Path(__file__).parent.parent / "corebook"


def is_bullet(line: str) -> bool:
    """Return True if line is a bullet item (- prefix)."""
    return line.startswith("- ")


def is_continuation(line: str) -> bool:
    """Return True if line is an indented continuation of a bullet."""
    return line.startswith("  ") and not line.startswith("  -")


def is_bullet_or_continuation(line: str) -> bool:
    return is_bullet(line) or is_continuation(line)


def compact_loose_lists(text: str) -> tuple[str, int]:
    """Remove blank lines between consecutive bullet items.

    Returns (fixed_text, count_of_removed_blanks).
    """
    lines = text.split("\n")
    result = []
    removed = 0
    i = 0
    while i < len(lines):
        # Check if current line is a bullet or continuation
        if is_bullet_or_continuation(lines[i]):
            # Look ahead: if next line is blank and the line after
            # is another bullet or continuation, skip the blank
            if (
                i + 2 < len(lines)
                and lines[i + 1].strip() == ""
                and is_bullet_or_continuation(lines[i + 2])
            ):
                result.append(lines[i])
                # Skip the blank line
                i += 2
                removed += 1
                continue
        result.append(lines[i])
        i += 1
    return "\n".join(result), removed


def main():
    check_only = "--check" in sys.argv
    total = 0
    for f in sorted(COREBOOK.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        fixed, count = compact_loose_lists(text)
        if count > 0:
            total += count
            print(f"{f.name}: {count} blank lines removed")
            if not check_only:
                f.write_text(fixed, encoding="utf-8")
    if check_only:
        print(f"\nDry run: {total} blank lines would be removed")
    else:
        print(f"\nTotal: {total} blank lines removed")


if __name__ == "__main__":
    main()
