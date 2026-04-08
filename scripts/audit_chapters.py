"""Comprehensive audit of all corebook chapters for remaining PDF artifacts."""
import re
from pathlib import Path

COREBOOK = Path(".")
issues = []

for f in sorted(COREBOOK.glob("*.md")):
    text = f.read_text(encoding="utf-8")
    lines = text.split("\n")
    fname = f.name
    
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # 1. Spaced-out characters (3+ single chars separated by spaces)
        # Pattern: sequence of "X Y Z" where X,Y,Z are single letters
        if re.search(r'(?<!\w)[A-Za-z] [A-Za-z] [A-Za-z] [A-Za-z]', line) and not line.startswith('|'):
            # Filter out known OK patterns
            if not re.match(r'^>', line):
                issues.append((fname, i, "SPACED_CHARS", stripped[:100]))
        
        # 2. Broken words: lowercase-space-lowercase mid-word patterns
        # e.g. "teach-\n" or "h orse" - specifically letter+space+letters that form a word
        # Look for patterns like "xY zW" that suggest merged columns
        
        # 3. Missing blank line before heading
        if stripped.startswith("###") and i > 1 and lines[i-2].strip() != "" and not lines[i-2].strip().startswith("#"):
            issues.append((fname, i, "NO_BLANK_BEFORE_HEADING", stripped[:80]))
        
        # 4. Missing blank line after heading  
        if stripped.startswith("###") and i < len(lines) and lines[i].strip() != "" and not lines[i].strip().startswith("#"):
            issues.append((fname, i, "NO_BLANK_AFTER_HEADING", stripped[:80]))
        
        # 5. Hyphenated word at end of line (word split across lines)
        if re.search(r'\w-$', stripped) and not stripped.startswith('#') and not stripped.startswith('|') and not stripped.startswith('>'):
            issues.append((fname, i, "HYPHEN_AT_EOL", stripped[:100]))
        
        # 6. Line starting with lowercase (paragraph continuation not joined)
        if re.match(r'^[a-z]', stripped) and i > 1 and lines[i-2].strip() == "" and not stripped.startswith('|'):
            prev_line = lines[i-2-1].strip() if i > 2 else ""
            # Only flag if previous non-blank line doesn't end with terminal punct
            if prev_line and not re.search(r'[.!?:;"\u201D\u2019)\]]$', prev_line) and not prev_line.startswith('#') and not prev_line.startswith('|') and not prev_line.startswith('>') and not prev_line.startswith('-'):
                issues.append((fname, i, "LOWERCASE_AFTER_BLANK", f"prev: {prev_line[:60]} | cur: {stripped[:60]}"))
        
        # 7. Very short orphan lines (< 30 chars, not heading/list/table/blockquote/blank)
        if 1 < len(stripped) < 30 and not any(stripped.startswith(p) for p in ['#', '|', '>', '-', '*', '`', '!', '(']) and not stripped == '---':
            # Check if it's between two blank lines (orphaned)
            prev_blank = (i > 1 and lines[i-2].strip() == "")
            next_blank = (i < len(lines) and lines[i].strip() == "")
            if prev_blank and next_blank:
                issues.append((fname, i, "SHORT_ORPHAN", stripped))
        
        # 8. Double spaces within text (not in tables)
        if "  " in stripped and not stripped.startswith('|') and not stripped.startswith('#') and not stripped.startswith('>') and not stripped.startswith('*Abilities') and not stripped.startswith('*Attributes'):
            # Ignore indented continuation lines
            if not line.startswith("  "):
                issues.append((fname, i, "DOUBLE_SPACE", stripped[:100]))
        
        # 9. Garbled text patterns (letter-space-letter-space sequences in body)
        if re.search(r'[A-Za-z] [A-Za-z] [A-Za-z] [A-Za-z] [A-Za-z]', stripped):
            if not stripped.startswith('#') and not stripped.startswith('|') and not stripped.startswith('>'):
                # Check it's not just normal words
                match = re.search(r'([A-Za-z] ){4,}[A-Za-z]', stripped)
                if match:
                    span = match.group()
                    # If all tokens are single chars, it's garbled
                    tokens = span.split()
                    if all(len(t) == 1 for t in tokens):
                        issues.append((fname, i, "GARBLED_TEXT", stripped[:100]))

# Print results grouped by category
categories = {}
for fname, line, cat, text in issues:
    if cat not in categories:
        categories[cat] = []
    categories[cat].append((fname, line, text))

for cat in sorted(categories.keys()):
    items = categories[cat]
    print(f"\n{'='*60}")
    print(f"{cat} ({len(items)} issues)")
    print(f"{'='*60}")
    for fname, line, text in items[:30]:  # Limit output
        print(f"  {fname}:{line}: {text}")
    if len(items) > 30:
        print(f"  ... and {len(items)-30} more")
