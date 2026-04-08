"""Convert talent names to ALL CAPS in statblock Talents: lines and Living Outcome Tables."""

# Canonical talent names -> ALL CAPS mapping
# Ordered longest-first to avoid partial replacements
TALENTS = [
    ('Man\u2019s Best Friend', 'MAN\u2019S BEST FRIEND'),
    ("Man's Best Friend", "MAN\u2019S BEST FRIEND"),
    ('Born in the Saddle', 'BORN IN THE SADDLE'),
    ('Judge of Character', 'JUDGE OF CHARACTER'),
    ('Tomahawk Fighter', 'TOMAHAWK FIGHTER'),
    ('Expert Fanning', 'EXPERT FANNING'),
    ('Business Minded', 'BUSINESS MINDED'),
    ('Calming Manner', 'CALMING MANNER'),
    ('Healing Touch', 'HEALING TOUCH'),
    ('Shotgun Master', 'SHOTGUN MASTER'),
    ('Rabble Rouser', 'RABBLE ROUSER'),
    ('Bronc Buster', 'BRONC BUSTER'),
    ('Horse Warrior', 'HORSE WARRIOR'),
    ('Knife Fighter', 'KNIFE FIGHTER'),
    ('Lightning Fast', 'LIGHTNING FAST'),
    ('Mountain Folk', 'MOUNTAIN FOLK'),
    ('Animal Hunter', 'ANIMAL HUNTER'),
    ('Fast Shooter', 'FAST SHOOTER'),
    ('Cold Blooded', 'COLD BLOODED'),
    ('High Society', 'HIGH SOCIETY'),
    ('Miner 49er', 'MINER 49ER'),
    ('Bow Master', 'BOW MASTER'),
    ('Dead Eye', 'DEAD EYE'),
    ('Guard Dog', 'GUARD DOG'),
    ('Hard to Hit', 'HARD TO HIT'),
    ('Light-Footed', 'LIGHT-FOOTED'),
    ('Quick Draw', 'QUICK DRAW'),
    ('The Voice', 'THE VOICE'),
    ('Two Gun', 'TWO GUN'),
    ('War Cry', 'WAR CRY'),
    ('Sharpshooter', 'SHARPSHOOTER'),
    ('Lockpicker', 'LOCKPICKER'),
    ('Companion', 'COMPANION'),
    ('Authority', 'AUTHORITY'),
    ('Charming', 'CHARMING'),
    ('Haymaker', 'HAYMAKER'),
    ('Defender', 'DEFENDER'),
    ('Engineer', 'ENGINEER'),
    ('Gambler', 'GAMBLER'),
    ('Gunsmith', 'GUNSMITH'),
    ('Herbalist', 'HERBALIST'),
    ('Manhunter', 'MANHUNTER'),
    ('Pistoleer', 'PISTOLEER'),
    ('Pugilist', 'PUGILIST'),
    ('Survivor', 'SURVIVOR'),
    ('Swindler', 'SWINDLER'),
    ('Tracker', 'TRACKER'),
    ('Brawler', 'BRAWLER'),
    ('Forger', 'FORGER'),
    ('Lawyer', 'LAWYER'),
    ('Roper', 'ROPER'),
    ('Smith', 'SMITH'),
    ('Lucky', 'LUCKY'),
    ('Shill', 'SHILL'),
    # Sneak may appear in tables
    ('Sneak', 'SNEAK'),
]

import re


def caps_talents_in_line(line):
    """Replace Title Case talent names with ALL CAPS in a Talents: line."""
    for title, caps in TALENTS:
        line = line.replace(title, caps)
    return line


changes = {
    'corebook/06-life-in-the-old-west.md': 'talents_lines',
    'corebook/09-the-new-mexico-campaign.md': 'talents_lines',
    'corebook/10-patience-is-a-virtue.md': 'talents_lines_and_tables',
}

for fp, mode in changes.items():
    with open(fp, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = 0
    for i, line in enumerate(lines):
        if 'Talents:' in line and '**Talents:**' in line:
            new_line = caps_talents_in_line(line)
            if new_line != line:
                lines[i] = new_line
                modified += 1

        if mode == 'talents_lines_and_tables' and '|' in line:
            # Check if this looks like a Living Outcome Table data row with talents
            parts = line.split('|')
            if len(parts) >= 6:
                talent_col = parts[4]
                new_talent_col = talent_col
                for title, caps in TALENTS:
                    new_talent_col = new_talent_col.replace(title, caps)
                if new_talent_col != talent_col:
                    parts[4] = new_talent_col
                    new_line = '|'.join(parts)
                    if new_line != line:
                        lines[i] = new_line
                        modified += 1

    with open(fp, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f'{fp}: {modified} lines updated')

print('\nDone.')
