#!/usr/bin/env python3
"""Fix ch10 talent names (Title Case), missing bold, structural headings, duplicate running headers."""
import re

path = 'c:/git-public/Tales-of-the-Old-West-2e/corebook/10-patience-is-a-virtue.md'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# ── 1. Talent names Title Case in statblocks ──────────────────────────────────

replacements = [
    (
        '**Talents:** authority (Advanced), charming (Advanced), cold blooded (Basic), business minded (Advanced).',
        '**Talents:** Authority (Advanced), Charming (Advanced), Cold Blooded (Basic), Business Minded (Advanced).'
    ),
    (
        'Talents: guard dog (Advanced - Scarlet), man\u2019s best friend (Basic - Rebel), light-footed (Advanced).',
        '**Talents:** Guard Dog (Advanced - Scarlet), Man\u2019s Best Friend (Basic - Rebel), Light-footed (Advanced).'
    ),
    (
        '**Talents:** guard dog (Advanced - Digger).',
        '**Talents:** Guard Dog (Advanced - Digger).'
    ),
    (
        '**Talents:** shotgun master (Advanced).',
        '**Talents:** Shotgun Master (Advanced).'
    ),
    (
        '**Talents:** charming (Basic), judge of character (Basic), lucky (Basic).',
        '**Talents:** Charming (Basic), Judge of Character (Basic), Lucky (Basic).'
    ),
    (
        '**Talents:** roper (Basic).',
        '**Talents:** Roper (Basic).'
    ),
    (
        '**Talents:** hay-maker (Advanced).',
        '**Talents:** Hay-maker (Advanced).'
    ),
    (
        '**Talents:** sharpshooter (Advanced).',
        '**Talents:** Sharpshooter (Advanced).'
    ),
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new, 1)
        print(f'OK: {old[:50]}')
    else:
        print(f'NOT FOUND: {repr(old[:60])}')

# ── 2. Structural fixes ───────────────────────────────────────────────────────

# Epilogue subheading merger
old_epilogue = (
    '### The Epilogue\n\n'
    'If the Player Characters Leave Patience with Peyton and Uphold Rockcliffe\u2019s Lie '
    'When the player characters'
)
new_epilogue = (
    '### The Epilogue\n\n'
    '### If the Player Characters Leave Patience with Peyton and Uphold Rockcliffe\u2019s Lie\n\n'
    'When the player characters'
)
if old_epilogue in text:
    text = text.replace(old_epilogue, new_epilogue, 1)
    print('OK: Epilogue subheading restored')
else:
    print(f'NOT FOUND: epilogue heading')

# Typo: Shunting -> Hunting
old_shack = '### Tyler Peyton Shunting Shack'
new_shack = "### Tyler Peyton's Hunting Shack"
if old_shack in text:
    text = text.replace(old_shack, new_shack, 1)
    print('OK: Shunting -> Hunting')
else:
    print('NOT FOUND: shunting shack heading')

# Remove duplicate '### Appendix: Your Tale Begins' running headers
# Pattern: \n### Appendix: Your Tale Begins\n\n### (next real heading)
count = 0
pattern = '\n### Appendix: Your Tale Begins\n\n### '
while pattern in text and count < 10:
    text = text.replace(pattern, '\n\n### ', 1)
    count += 1
print(f'OK: Removed {count} duplicate Appendix running headers')

# ── 3. Talent names in Living Outcome Tables ──────────────────────────────────

table_talents = [
    # Outlaw
    ('| cold blooded or fast shooter |', '| Cold Blooded or Fast Shooter |'),
    ('| brawler or pugilist          |', '| Brawler or Pugilist          |'),
    ('| warcry or authority          |', '| Warcry or Authority          |'),
    ('| lockpicker or sneak          |', '| Lockpicker or Sneak          |'),
    ('| two gun or light-footed      |', '| Two Gun or Light-footed      |'),
    ('| quick draw or lightning fast |', '| Quick Draw or Lightning Fast |'),
    # Frontier Folk
    ('| lucky or hard to hit            |', '| Lucky or Hard to Hit            |'),
    ('| survivor or bow master          |', '| Survivor or Bow Master          |'),
    ('| light-footed or tracker         |', '| Light-footed or Tracker         |'),
    ('| companion or born in the saddle |', '| Companion or Born in the Saddle |'),
    ('| man\u2019s best friend or guard dog  |', '| Man\u2019s Best Friend or Guard Dog  |'),
    ('| animal hunter or knife fighter  |', '| Animal Hunter or Knife Fighter  |'),
    # Ranch Hand
    ('| hay-maker or brawler           |', '| Hay-maker or Brawler           |'),
    ('| sharpshooter or expert fanning |', '| Sharpshooter or Expert Fanning |'),
    ('| bronc buster or horse warrior  |', '| Bronc Buster or Horse Warrior  |'),
    ('| charming or authority          |', '| Charming or Authority          |'),
    ('| born in the saddle or roper    |', '| Born in the Saddle or Roper    |'),
    ('| horse warrior or defender      |', '| Horse Warrior or Defender      |'),
]

for old, new in table_talents:
    if old in text:
        text = text.replace(old, new, 1)
        print(f'OK table: {old.strip()[:50]}')
    else:
        print(f'NOT FOUND table: {repr(old.strip()[:60])}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('\nFile written successfully.')
