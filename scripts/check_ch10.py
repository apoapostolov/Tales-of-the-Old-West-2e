#!/usr/bin/env python3
"""Quick scan of ch10 for remaining formatting issues."""
import re

with open('corebook/10-patience-is-a-virtue.md', 'r', encoding='utf-8') as f:
    text = f.read()

sq = '\u2019'

# Abilities as they should appear (CAPS)
ABILITIES_CAPS = [
    f"FIGHTIN{sq}", f"SHOOTIN{sq}", f"ANIMAL HANDLIN{sq}", "HAWKEYE",
    "PRESENCE", f"PERFORMIN{sq}", "INSIGHT", f"DOCTORIN{sq}", "RESILIENCE",
    "LABOR", "LIGHT-FINGERED", "MOVE", "OPERATE", "NATURE",
    f"BOOKLEARNIN{sq}", f"MAKIN{sq}"
]
# lowercase versions for detection
ABILITIES_LOWER = [a.lower() for a in ABILITIES_CAPS]

# Check: ability name in a game-mechanics context but lowercase
# Pattern: "make a/an X roll/test", "using X", "test X", "your X"
issues = []
for lower, caps in zip(ABILITIES_LOWER, ABILITIES_CAPS):
    base = lower.rstrip(sq.lower()).rstrip("'")
    # Find any occurrence of lowercase version after make/test/using/roll/a/an
    pat = re.compile(r'(?:make a|make an|test|using|roll|a |an )(' + re.escape(lower) + r')', re.IGNORECASE)
    for m in pat.finditer(text):
        found = m.group(1)
        if found != caps and found.upper() != caps.upper().replace(sq, sq):
            ctx = text[max(0,m.start()-30):m.end()+30]
            issues.append(f"Lowercase ability '{found}' in: ...{ctx}...")

# Talent names: check Talents: lines for any lowercase first letters
for m in re.finditer(r'\*\*Talents:\*\*([^\n]+)', text):
    line = m.group(1)
    for t in re.finditer(r'([a-z][a-zA-Z\u2019 -]+?)\s*\(', line):
        name = t.group(1).strip()
        if name and name[0].islower():
            issues.append(f"Lowercase talent name '{name}' in: {m.group()[:80]}")

print(f"Total issues: {len(issues)}")
for i in issues:
    print(" ", i[:120])
