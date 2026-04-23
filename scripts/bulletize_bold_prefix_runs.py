"""Convert runs of paragraphs that begin with `**Bold prefix.** ...` into
markdown bullet lists. Operates on .md files under 1870s-the-old-west/.

A "run" is two or more consecutive paragraphs (separated by single blank
lines) where each paragraph begins with `**...**` followed by content on
the same line. The run is converted: each paragraph becomes one `- ...`
bullet, with no blank lines between bullets.

Skips runs inside fenced code blocks and blockquotes (lines starting with `>`).
"""
from __future__ import annotations

import pathlib
import re
import sys

BOLD_PREFIX = re.compile(r"^\*\*[A-Z][^*\n]+?\.?\*\*[\s\u2014\-]")

ROOT = pathlib.Path(__file__).resolve().parent.parent / "1870s-the-old-west"


def process(text: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    in_fence = False
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            in_fence = not in_fence
            out.append(line)
            i += 1
            continue
        if in_fence or line.startswith(">"):
            out.append(line)
            i += 1
            continue
        if BOLD_PREFIX.match(line):
            # Look ahead: collect a run
            run = [line]
            j = i + 1
            # Each paragraph is one logical line; separated by exactly one blank line.
            while j + 1 < len(lines) and lines[j] == "" and BOLD_PREFIX.match(lines[j + 1]):
                run.append(lines[j + 1])
                j += 2
            if len(run) >= 2:
                # Convert to bullets, no blank lines between
                for entry in run:
                    out.append(f"- {entry}")
                i = j + 1 if j < len(lines) else j
                # Need to preserve trailing blank line that separated run from next content
                # j currently points to the position AFTER last entry.
                # If lines[j] is blank, keep it as separator.
                # Above we set i = j + 1 only if we moved past — actually j is already
                # the index after the last consumed entry line, so set i = j.
                i = j
                continue
            else:
                out.append(line)
                i += 1
                continue
        out.append(line)
        i += 1
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
