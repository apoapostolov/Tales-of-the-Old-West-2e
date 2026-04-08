#!/usr/bin/env python3
"""Split Tales of the Old West final.md into per-chapter files."""

import re
from pathlib import Path

CHAPTER_NAMES = {
    1: "welcome-to-the-old-west",
    2: "your-player-character",
    3: "rolling-the-bones",
    4: "talents",
    5: "conflict-and-damage",
    6: "life-in-the-old-west",
    7: "the-west-in-the-1870s",
    8: "campaigns-in-the-old-west",
    9: "the-new-mexico-campaign",
    10: "patience-is-a-virtue",
}

def main():
    src = Path(r"C:\git\lifestyle\rpg_projects\houserules\tales-of-the-old-west\Tales_of_the_Old_West_Core_Rules.final.md")
    out_dir = Path(r"C:\git-public\Tales-of-the-Old-West-2e\corebook")

    text = src.read_text(encoding="utf-8")
    lines = text.split("\n")

    # Find chapter boundaries
    chapters = []
    for i, line in enumerate(lines):
        m = re.match(r"^## Chapter (\d+)\s*-\s*(.+)$", line)
        if m:
            chapters.append((i, int(m.group(1)), m.group(2).strip()))

    # Split and write
    for idx, (start_line, ch_num, ch_title) in enumerate(chapters):
        end_line = chapters[idx + 1][0] if idx + 1 < len(chapters) else len(lines)
        chunk = "\n".join(lines[start_line:end_line]).rstrip() + "\n"

        filename = f"{ch_num:02d}-{CHAPTER_NAMES[ch_num]}.md"
        (out_dir / filename).write_text(chunk, encoding="utf-8")
        print(f"  {filename}: lines {start_line+1}-{end_line} ({end_line - start_line} lines)")

    print(f"\nSplit {len(chapters)} chapters into {out_dir}")


if __name__ == "__main__":
    main()
