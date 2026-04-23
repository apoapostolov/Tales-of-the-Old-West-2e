"""Second pass: convert single-paragraph runs that contain multiple
`**Bold prefix.** ...` segments into bullet lists.

Pattern: a single non-blank line that begins with `**X.** ` and contains
2+ occurrences of ` **Y.** ` (mid-line boundaries). Split on those
boundaries; each segment becomes a bullet.

Skips fenced code blocks and blockquotes.
"""
from __future__ import annotations

import pathlib
import re
import sys

LEADING = re.compile(r"^\*\*[A-Z][^*\n]+?\.?\*\*[\s\u2014\-]")
INLINE_BOUNDARY = re.compile(r"\s\*\*[A-Z][^*\n]+?\.?\*\*[\s\u2014\-]")

ROOT = pathlib.Path(__file__).resolve().parent.parent / "1870s-the-old-west"


def split_inline(line: str) -> list[str] | None:
    if not LEADING.match(line):
        return None
    # Find inline boundaries (mid-line)
    boundaries = list(INLINE_BOUNDARY.finditer(line))
    if len(boundaries) < 1:
        return None
    # Split: produce segments where each starts with **X.** ...
    parts: list[str] = []
    start = 0
    for m in boundaries:
        # End previous segment at m.start() (the leading space)
        parts.append(line[start:m.start()].rstrip())
        # Next segment begins at m.start()+1 (skipping the leading space)
        start = m.start() + 1
    parts.append(line[start:].rstrip())
    return parts


def process(text: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    in_fence = False
    for line in lines:
        if line.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            continue
        if in_fence or line.startswith(">") or line.startswith("- "):
            out.append(line)
            continue
        parts = split_inline(line)
        if parts and len(parts) >= 2:
            for p in parts:
                out.append(f"- {p}")
        else:
            out.append(line)
    return "\n".join(out)


def main() -> int:
    files = sorted(ROOT.glob("*.md"))
    changed = 0
    for f in files:
        original = f.read_text(encoding="utf-8")
        new = process(original)
        if new != original:
            f.write_text(new, encoding="utf-8")
            changed += 1
            print(f"updated: {f.name}")
    print(f"\n{changed} file(s) changed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
