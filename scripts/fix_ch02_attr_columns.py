"""Move attribute values from name column to value column in ch02 profession table headers."""

import re

fp = 'corebook/02-your-player-character.md'
with open(fp, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Match header lines like: | Grit 2    |     | Quick 2         |     | Cunning 3        |     | Docity 2      |     |
header_pattern = re.compile(
    r'^\| Grit (\d)\s+\|\s+\| Quick (\d)\s+\|\s+\| Cunning (\d)\s+\|\s+\| Docity (\d)\s+\|\s+\|'
)

modified = 0
for i, line in enumerate(lines):
    m = header_pattern.match(line)
    if m:
        grit, quick, cunning, docity = m.group(1), m.group(2), m.group(3), m.group(4)
        new_header = (
            f'| Grit       | {grit}   | Quick          | {quick}   '
            f'| Cunning         | {cunning}   | Docity       | {docity}   |\n'
        )
        lines[i] = new_header
        modified += 1
        print(f'  Line {i+1}: Grit {grit}, Quick {quick}, Cunning {cunning}, Docity {docity}')

with open(fp, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f'\n{fp}: {modified} header lines updated')
