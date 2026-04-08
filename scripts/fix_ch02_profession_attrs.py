"""Merge Attributes line values into table header row for each profession in ch02."""

import re

fp = 'corebook/02-your-player-character.md'
with open(fp, 'r', encoding='utf-8') as f:
    lines = f.readlines()

modified = 0
i = 0
while i < len(lines):
    line = lines[i]
    # Match: **Attributes:** Grit N, Quick N, Cunning N, Docity N
    m = re.match(r'\*\*Attributes:\*\* Grit (\d), Quick (\d), Cunning (\d), Docity (\d)', line.strip())
    if m:
        grit, quick, cunning, docity = m.group(1), m.group(2), m.group(3), m.group(4)

        # Find the next table header line (within 3 lines)
        for j in range(i+1, min(len(lines), i+4)):
            if lines[j].strip().startswith('| Grit'):
                # Replace the header: inject values after attribute names
                new_header = (
                    f'| Grit {grit}    |     | Quick {quick}         |     '
                    f'| Cunning {cunning}        |     | Docity {docity}      |     |\n'
                )
                lines[j] = new_header
                # Remove the **Attributes:** line (mark as empty)
                lines[i] = ''
                modified += 2
                print(f'  Line {i+1}: removed Attributes line (Grit {grit}, Quick {quick}, Cunning {cunning}, Docity {docity})')
                print(f'  Line {j+1}: updated header → {new_header.rstrip()}')
                break
    i += 1

with open(fp, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f'\n{fp}: {modified} lines modified ({modified//2} professions updated)')
