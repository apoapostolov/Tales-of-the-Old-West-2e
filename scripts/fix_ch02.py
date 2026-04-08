"""Fix chapter 02 structural issues: stat blocks, Faith split, age table."""
import re

data = open('02-your-player-character.md', 'r', encoding='utf-8').read()

# Fix 1: Age table header
data = data.replace(
    '**P lay er C h a r ac t e r  age  t a bl e  -** C h o o se  yo ur age :',
    '**Player Character Age Table** - Choose your age:'
)
print('Fix 1: age table header')

# Fix 2: Stat blocks
def parse_stat_block(text):
    t = ' '.join(text.split())

    attrs = {}
    for garbled, clean in [('G ri t', 'Grit'), ('Q uick', 'Quick'), ('c unnin G', 'Cunning'), ('D oci t y', 'Docity')]:
        m = re.search(re.escape(garbled) + r'\s+(\d)', t)
        if m:
            attrs[clean] = int(m.group(1))
        else:
            attrs[clean] = 2

    ability_patterns = [
        ('Labor', r'Labor'),
        ('Move', r'Move'),
        ('Hawkeye', r'Hawke?\s*ye'),
        ("Performin'", r"Per\s*f\s*ormin['\u2019]?"),
        ('Presence', r'Presence'),
        ('Operate', r'Operate'),
        ('Nature', r'Nature'),
        ("Makin'", r"Makin['\u2019]?"),
        ("Fightin'", r"Fightin['\u2019]?"),
        ("Shootin'", r"Shootin['\u2019]?"),
        ('Insight', r'Insight'),
        ("Doctorin'", r"Doctorin['\u2019]?"),
        ('Resilience', r'Resilience'),
        ('Light-Fingered', r'Light-Fingered'),
        ("Animal Handlin'", r"Animal\s*Handlin['\u2019]?"),
        ("Booklearnin'", r"Booklearnin['\u2019]?"),
    ]

    abilities = {}
    for clean, pattern in ability_patterns:
        m = re.search(pattern + r'\s+(\d)', t)
        if m:
            abilities[clean] = int(m.group(1))
        else:
            abilities[clean] = 0

    attr_line = ', '.join(f'{k} {v}' for k, v in attrs.items())

    grit_abs = ["Fightin'", 'Labor', 'Presence', 'Resilience']
    quick_abs = ['Light-Fingered', 'Move', 'Operate', "Shootin'"]
    cunning_abs = ["Animal Handlin'", 'Hawkeye', 'Insight', 'Nature']
    docity_abs = ["Booklearnin'", "Doctorin'", "Makin'", "Performin'"]

    rows = []
    for g, q, c, d in zip(grit_abs, quick_abs, cunning_abs, docity_abs):
        gv = str(abilities.get(g, 0)) if abilities.get(g, 0) > 0 else '\u2014'
        qv = str(abilities.get(q, 0)) if abilities.get(q, 0) > 0 else '\u2014'
        cv = str(abilities.get(c, 0)) if abilities.get(c, 0) > 0 else '\u2014'
        dv = str(abilities.get(d, 0)) if abilities.get(d, 0) > 0 else '\u2014'
        rows.append(f'| {g} | {gv} | {q} | {qv} | {c} | {cv} | {d} | {dv} |')

    table = f'**Attributes:** {attr_line}\n\n'
    table += '| Grit | | Quick | | Cunning | | Docity | |\n'
    table += '|---|---|---|---|---|---|---|---|\n'
    table += '\n'.join(rows)

    return table

stat_pattern = re.compile(
    r'^G\s*ri\s*t\s+\d\s+Q\s*uick\s+\d.*?Booklearnin.*?\d?\s*$',
    re.MULTILINE
)

count = 0
for m in reversed(list(stat_pattern.finditer(data))):
    old = m.group(0)
    new = parse_stat_block(old)
    data = data[:m.start()] + new + data[m.end():]
    count += 1

print(f'Fix 2: replaced {count} stat blocks')

# Fix 3: Faith section - rejoin split paragraph
# The Faith text is split: ends with "an affinity with" then continues as orphaned text
# in the abilities list as "nature, or just the simple belief..."
faith_fragment = 'nature, or just the simple belief in yourself as the only one you can truly trust.'
if faith_fragment in data:
    # Find the orphaned block (it's between PRESENCE and RESILIENCE in the abilities list)
    frag_idx = data.index(faith_fragment)

    # Find the full orphaned text block (from fragment to next ability list item)
    # It includes the Faith description paragraph
    resilience_marker = '- RESILIENCE (Grit)'
    if resilience_marker not in data:
        resilience_marker = '- RESILIENCE'

    orphan_end = data.index(resilience_marker, frag_idx)
    orphan_text = data[frag_idx:orphan_end].strip()

    # Remove it from the abilities list
    # Find start - it's after "- PRESENCE (Grit)\n\n"
    presence_marker = '- PRESENCE (Grit)'
    if presence_marker not in data:
        presence_marker = '- PRESENCE'

    pres_idx = data.index(presence_marker)
    pres_end = pres_idx + len(presence_marker)

    # The orphan starts after PRESENCE line
    data = data[:pres_end] + '\n\n' + data[orphan_end:]

    # Now rejoin the Faith paragraph
    faith_cut = 'an affinity with'
    if faith_cut in data:
        cut_idx = data.index(faith_cut)
        # The paragraph after "an affinity with" should continue with the orphan text
        # Remove the current line break after "an affinity with"
        after_cut = data[cut_idx + len(faith_cut):]
        # Strip leading whitespace/newlines
        after_cut = after_cut.lstrip('\n')
        data = data[:cut_idx] + faith_cut + ' ' + orphan_text + '\n\n' + after_cut
        print('Fix 3: Faith section rejoined')

# Fix 4: Fix the split 'teach-' / 'ing' in Presence section (ch03 already fixed heading)
# And fix 'anoth-\n\ner' split in Spending XP
if 'costs anoth-\n\ner 6 XP' in data:
    data = data.replace('costs anoth-\n\ner 6 XP', 'costs another 6 XP')
    print('Fix 4a: anoth-er rejoined')
elif 'costs anoth-' in data:
    # Try variations
    idx = data.index('costs anoth-')
    after = data[idx+12:idx+30]
    print(f'Fix 4a debug: after "costs anoth-" = {repr(after)}')

# Normalize multiple blank lines
while '\n\n\n' in data:
    data = data.replace('\n\n\n', '\n\n')

open('02-your-player-character.md', 'w', encoding='utf-8').write(data)
print(f'Done. {len(data.splitlines())} lines.')
