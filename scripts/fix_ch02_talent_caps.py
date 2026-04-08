"""Convert talent names in ch02 from bold-lowercase to bold-ALL CAPS."""

import re

# Ordered longest-first to avoid partial matches
# Maps what appears in ch02 → ALL CAPS form
TALENT_MAP = [
    ('born in the saddle', 'BORN IN THE SADDLE'),
    ('judge of character', 'JUDGE OF CHARACTER'),
    ('shotgun master', 'SHOTGUN MASTER'),
    ('calming manner', 'CALMING MANNER'),
    ('business minded', 'BUSINESS MINDED'),
    ('cold blooded', 'COLD BLOODED'),
    ('healing touch', 'HEALING TOUCH'),
    ('horse warrior', 'HORSE WARRIOR'),
    ('knife fighter', 'KNIFE FIGHTER'),
    ('lightning fast', 'LIGHTNING FAST'),
    ('rabble rouser', 'RABBLE ROUSER'),
    ('high society', 'HIGH SOCIETY'),
    ('bronc buster', 'BRONC BUSTER'),
    ('lockpicker', 'LOCKPICKER'),
    ('manhunter', 'MANHUNTER'),
    ('miner 49er', 'MINER 49ER'),
    ('mountainfolk', 'MOUNTAIN FOLK'),  # ch02 typo → two words
    ('quick draw', 'QUICK DRAW'),
    ('quickdraw', 'QUICK DRAW'),       # ch02 variant
    ('light-footed', 'LIGHT-FOOTED'),
    ('bow master', 'BOW MASTER'),
    ('two gun', 'TWO GUN'),
    ('the voice', 'THE VOICE'),
    ('guard dog', 'GUARD DOG'),
    ('authority', 'AUTHORITY'),
    ('charming', 'CHARMING'),
    ('companion', 'COMPANION'),
    ('engineer', 'ENGINEER'),
    ('gambler', 'GAMBLER'),
    ('herbalist', 'HERBALIST'),
    ('survivor', 'SURVIVOR'),
    ('swindler', 'SWINDLER'),
    ('pugilist', 'PUGILIST'),
    ('tracker', 'TRACKER'),
    ('brawler', 'BRAWLER'),
    ('lawyer', 'LAWYER'),
    ('roper', 'ROPER'),
    ('lucky', 'LUCKY'),
    ('smith', 'SMITH'),
    ('shill', 'SHILL'),
    ('sneak', 'SNEAK'),
]

fp = 'corebook/02-your-player-character.md'
with open(fp, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace **talent name** and **talent name.** patterns
modified = 0
for lc, caps in TALENT_MAP:
    # Match **talent** and **talent.** with optional trailing period inside bold
    for pattern, repl in [
        (f'**{lc}.**', f'**{caps}**'),  # period inside bold → move period out handled by next
        (f'**{lc}**', f'**{caps}**'),
    ]:
        if pattern in text:
            text = text.replace(pattern, repl)
            print(f'  OK: {pattern!r} → {repl!r}')
            modified += 1

with open(fp, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'\n{fp}: {modified} replacements made')
