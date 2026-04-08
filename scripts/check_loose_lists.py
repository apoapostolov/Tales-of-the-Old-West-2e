"""Check for loose bullet lists (blank lines between - items) in all .md files."""
import re
from pathlib import Path

for f in sorted(Path(".").glob("*.md")):
    text = f.read_text(encoding="utf-8")
    lines = text.split("\n")
    loose_count = 0
    examples = []
    for i in range(len(lines) - 2):
        if (
            lines[i].startswith("- ")
            and lines[i + 1].strip() == ""
            and i + 2 < len(lines)
            and lines[i + 2].startswith("- ")
        ):
            loose_count += 1
            if len(examples) < 3:
                examples.append(f"  L{i+1}: {lines[i][:60]}")
    if loose_count > 0:
        print(f"{f.name}: {loose_count} loose bullet gaps")
        for ex in examples:
            print(ex)
