"""Fix talent name Title Case across all corebook chapters."""

changes = {
    'corebook/06-life-in-the-old-west.md': [
        ('**Talents:** calming manner, charming, shill.',
         '**Talents:** Calming Manner, Charming, Shill.'),
        ('Talents:  cold blooded ,  fast shooter ,  manhunter .',
         '**Talents:** Cold Blooded, Fast Shooter, Manhunter.'),
        ('**Talents:** gambler, forger, swindler.',
         '**Talents:** Gambler, Forger, Swindler.'),
        ('**Talents:** authority, business minded, high society.',
         '**Talents:** Authority, Business Minded, High Society.'),
        ('**Talents:** bow master, horse warrior, tomahawk fighter.',
         '**Talents:** Bow Master, Horse Warrior, Tomahawk Fighter.'),
        ('**Talents:** authority, healing touch, herbalist.',
         '**Talents:** Authority, Healing Touch, Herbalist.'),
        ('Talents:  engineer ,  miner 49er ,  smith .',
         '**Talents:** Engineer, Miner 49er, Smith.'),
        ('**Talents:** brawler, companion, shotgun master.',
         '**Talents:** Brawler, Companion, Shotgun Master.'),
        ('**Talents:** authority, judge of character, lawyer.',
         '**Talents:** Authority, Judge of Character, Lawyer.'),
        ('**Talents:** dead eye, hay-maker, two gun.',
         '**Talents:** Dead Eye, Haymaker, Two Gun.'),
        ('Talents:  charming ,  lawyer ,  rabble rouser .',
         '**Talents:** Charming, Lawyer, Rabble Rouser.'),
        ('Talents:  born in the saddle ,  lightning fast ,  lucky .',
         '**Talents:** Born in the Saddle, Lightning Fast, Lucky.'),
        ('Talents:  high society ,  rabble rouser ,  the voice .',
         '**Talents:** High Society, Rabble Rouser, The Voice.'),
        ('**Talents:** bronc buster, companion, roper.',
         '**Talents:** Bronc Buster, Companion, Roper.'),
        ('**Talents:** business minded, charming, guard dog.',
         '**Talents:** Business Minded, Charming, Guard Dog.'),
        ('**Talents:** authority, pistoleer, warcry.',
         '**Talents:** Authority, Pistoleer, War Cry.'),
        ('Talents:  pugilist ,  shotgun master ,  survivor .',
         '**Talents:** Pugilist, Shotgun Master, Survivor.'),
        # smart apostrophe variant for man's best friend
        ('**Talents:** man\u2019s best friend, mountain folk, sharp shooter.',
         '**Talents:** Man\u2019s Best Friend, Mountain Folk, Sharpshooter.'),
        ('**Talents:** business minded, gunsmith, shill.',
         '**Talents:** Business Minded, Gunsmith, Shill.'),
    ],
    'corebook/09-the-new-mexico-campaign.md': [
        ('Talents:  authority  (Advanced),  charming  (Advanced),  cold blooded  (Advanced),  business minded (Advanced),  high society  (Advanced).',
         '**Talents:** Authority (Advanced), Charming (Advanced), Cold Blooded (Advanced), Business Minded (Advanced), High Society (Advanced).'),
        ('**Talents:** authority (Basic), brawler (Advanced), hay-maker (Advanced), high society (Basic), knife fighter (Advanced), rabble rouser (Advanced).',
         '**Talents:** Authority (Basic), Brawler (Advanced), Haymaker (Advanced), High Society (Basic), Knife Fighter (Advanced), Rabble Rouser (Advanced).'),
    ],
    'corebook/10-patience-is-a-virtue.md': [
        ('Light-footed (Advanced).', 'Light-Footed (Advanced).'),
        ('Hay-maker (Advanced).', 'Haymaker (Advanced).'),
        ('Two Gun or Light-footed', 'Two Gun or Light-Footed'),
        ('Light-footed or Tracker', 'Light-Footed or Tracker'),
        ('Hay-maker or Brawler', 'Haymaker or Brawler'),
    ],
}

total_applied = 0
total_missed = 0

for fp, replacements in changes.items():
    with open(fp, 'r', encoding='utf-8') as f:
        text = f.read()

    applied = 0
    missed = 0
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
            print(f'  OK: {old[:70]}')
            applied += 1
        else:
            print(f'  MISS: {old[:70]}')
            missed += 1

    with open(fp, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f'{fp}: {applied}/{len(replacements)} applied, {missed} missed')
    print()
    total_applied += applied
    total_missed += missed

print(f'Total: {total_applied} applied, {total_missed} missed')
