#!/usr/bin/env python3
"""Comprehensive fix for all remaining garbled tables, stat blocks, and plain-text data."""
import re
import os

BASE = r'c:\git-public\Tales-of-the-Old-West-2e\corebook'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)

def safe_replace(content, old, new, label):
    if old in content:
        content = content.replace(old, new, 1)
        print(f"  FIXED: {label}")
        return content, 1
    else:
        print(f"  NOT FOUND: {label}")
        return content, 0

###############################################################################
# NPC STAT BLOCK PARSER
###############################################################################
SKILL_RE = re.compile(
    r"(ANIMAL HANDLIN'|BOOK LEARNIN'|BOOKLEARNIN'|LIGHT-FINGERED|"
    r"PERFORMIN'|SHOOTIN'|FIGHTIN'|DOCTORIN'|RESILIENCE|PRESENCE|"
    r"HAWKEYE|INSIGHT|NATURE|OPERATE|MAKIN'|LABOR|MOVE)\s+(\d)"
)

def parse_npc(text):
    """Parse a garbled NPC stat block into structured data."""
    m = re.match(r'(.+?)\s+GRIT\s+(\d)\s+QUICK\s+(\d)\s+CUNNING\s+(\d)\s+DOCITY\s+(\d)\s+', text)
    if not m:
        return None
    name = m.group(1).strip()
    attrs = f"GRIT {m.group(2)}, QUICK {m.group(3)}, CUNNING {m.group(4)}, DOCITY {m.group(5)}"
    rest = text[m.end():]
    skills = []
    last_end = 0
    for sm in SKILL_RE.finditer(rest):
        skills.append(f"{sm.group(1)} {sm.group(2)}")
        last_end = sm.end()
    desc = rest[last_end:].strip()
    skill_line = ", ".join(skills)
    return name, attrs, skill_line, desc

def format_npc(name, attrs, skill_line, desc):
    """Format an NPC stat block into clean markdown."""
    lines = [f"**{name}** \u2014 {attrs}"]
    lines.append(f"{skill_line}")
    lines.append(f"{desc}")
    return "\n".join(lines)

def format_talents(raw):
    """Clean up garbled Talents line."""
    # Remove extra spaces around talent names
    t = re.sub(r'\s{2,}', ' ', raw).strip()
    # Fix "Talents:  x ,  y" -> "**Talents:** x, y"
    t = re.sub(r'^Talents:\s*', '**Talents:** ', t)
    # Clean spaces before commas and periods
    t = re.sub(r'\s+,', ',', t)
    t = re.sub(r'\s+\.', '.', t)
    return t

def format_gear(raw):
    """Clean up Gear line."""
    g = re.sub(r'\s{2,}', ' ', raw).strip()
    g = re.sub(r'^Gear:\s*', '**Gear:** ', g)
    return g

WEAPON_HEADER = "| Weapon | Action | Draw Mod | Attack Mod | Damage | Critical | Range | Ammo |\n| --- | --- | --- | --- | --- | --- | --- | --- |"

def parse_weapon_text(text):
    """Parse garbled plain-text weapon data into table rows."""
    # Known weapon names (multi-word) that appear in the data
    weapons = [
        "Metropolitan Navy 1864", "Colt 45 Peacemaker", "Colt Walker",
        "Winchester 1873", "Spencer Carbine", "Hunting Blade", "Quality Blade",
        "Shotgun", "Cooper", "Kosh"
    ]
    rows = []
    remaining = text.strip()
    while remaining:
        remaining = remaining.strip()
        if not remaining:
            break
        found = False
        for wname in weapons:
            if remaining.startswith(wname):
                after = remaining[len(wname):].strip()
                parts = after.split(None, 6)
                if len(parts) >= 7:
                    rows.append(f"| {wname} | {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {parts[6]} |")
                    # Find where the next weapon starts
                    used = len(wname) + 1
                    for p in parts[:7]:
                        used = after.index(p, used - len(wname) - 1) + len(p) if used == len(wname) + 1 else used
                    remaining = after[sum(len(p) for p in parts[:7]) + 6:].strip()
                elif len(parts) >= 1:
                    rows.append(f"| {wname} | {' | '.join(parts)} |")
                    remaining = ""
                found = True
                break
        if not found:
            break
    return rows

###############################################################################
# CH08 FIX
###############################################################################
def fix_ch08():
    print("\n=== CH08 ===")
    path = os.path.join(BASE, '08-campaigns-in-the-old-west.md')
    content = read_file(path)
    content, c = safe_replace(content,
        '| | 45 | The Army is Coming',
        '| 45 | The Army is Coming',
        "Stray pipe on 'The Army is Coming'")
    if c:
        write_file(path, content)
    return c

###############################################################################
# CH07 FIX: Tribal Names Table
###############################################################################
def fix_ch07():
    print("\n=== CH07 ===")
    path = os.path.join(BASE, '07-the-west-in-the-1870s.md')
    content = read_file(path)
    changes = 0

    # The garbled tribal names run from the header "### Tribal Names" until
    # "### A Brief History of African Americans"
    # Find the garbled block: starts after "### Tribal Names" header
    tribal_start_marker = "### Tribal Names\n"
    african_marker = "### A Brief History of African Americans"

    ts = content.index(tribal_start_marker) + len(tribal_start_marker)
    te = content.index(african_marker)
    old_block = content[ts:te]

    new_table = """
| Common Name | Endonym | Comments |
| --- | --- | --- |
| Apache | Ind\u00e9, Ndeh | Closely related to the Navajo. |
| Arapaho | Hinono\u2019eiteen | Nomadic buffalo hunters, they were called different things by different tribes, often with a \u2018Sky\u2019 or \u2018Cloud\u2019 reference. Traditional allies of Cheyenne and Sioux, and enemies of Comanche and Kiowa. |
| Arikara | Arikara | The name means \u201chorns\u201d or possibly \u201celk people\u201d. They were semi-nomadic but did cultivate corn, beans and tobacco. Said to own many dogs. |
| Assinboine | Hohe Nakota | The commonly used name of Assinboine (meaning \u201cburned rock\u201d) was coined by the Chippewas tribe in 1812 when Chippewas captives were burned to death by their Assinboine enemies. |
| Blackfoot | Niitsitapi | Called Blackfoot by other tribes due to their black leather moccasins, the Native name means \u201cthe real people\u201d. |
| Cayuse | Liksiyu | The name Cayuse was coined by early French Canadian trappers. Renowned for breeding the Cayuse horse, a fast horse with great endurance. Semi-nomadic. They came into conflict with white settlers after the opening of the Oregon Trail, and as a result of the 1848 gold rush. |
| Cherokee | Anigiduwagi | The name Cherokee probably comes from other tribal names for them meaning \u201cpeople who live in the cave / mountain country\u201d. One of the so-called Five Civilized Tribes forcibly moved from their lands in the southeast to reservations in Indian Territory (modern Oklahoma). They were agrarian farmers and hunters. |
| Cheyenne | S\u00f3\u2019taeo\u2019o and Tsitsistas | These two tribes merged to form the Cheyenne in 1830, which itself might mean \u201cred talker,\u201d a name possibly given them by the Lakota. |
| Chickasaw | Chikashsha | The name means \u201crebel\u201d in the Choctaw language. One of the so-called Five Civilized Tribes. |
| Chinook | Tsin\u00fak | A Pacific Northwestern community, their name possibly means \u201cfish eaters\u201d or \u201cstrong fighters\u201d. |
| Choctaw | Chahta | The name possibly derived from a tribal leader, or from the Choctaw phrase for \u201criver people\u201d, Hacha hatak. One of the so-called Five Civilized Tribes. |
| Chumash | Chumash | The name means \u201cbead people\u201d or \u201cseashell people\u201d. |
| Comanche | Nermenuh | The name Comanche may have come from the Ute word \u201ckomantica\u201d meaning \u201cpeople who fight all the time\u201d, possibly a compliment as the Ute and Comanche tribes were allies at the time. |
| Creek | Mvskoke | One of the so-called Five Civilized Tribes. |
| Crow | Aps\u00e1alooke | Rivals of the Sioux and Cheyenne. Their name was possibly coined by the Hidatsa tribe, meaning \u201cchildren of the large-beaked bird\u201d and shortened to \u201ccrow\u201d or \u201craven\u201d by other tribes. |
| Hopi | Hopi | The name means \u201cone who is well-mannered\u201d. The Hopi are descended from ancestral Puebloans. |
| Hualapai | Hwalb\u00e1y | Pronounced \u201cwalapai\u201d, the name means \u201cpeople of the tall pines\u201d in the Native language. |
| Hupa | Natinixwe | The name means \u201cpeople of the place where the trails return\u201d. |
| Kiowa | K\u00fatj\u00e0u, Ka\u2019igwu | The name Kiowa is possibly derived from the way the Comanche would pronounce the tribe\u2019s name. |
| Lakota | Th\u00edthunwan | The Lakota name comes from the endonym, Lakota, meaning \u201cfeeling affection, friendly or unified\u201d\u2014there are dozens of variations used by different tribes. A part of the Great Sioux Nation. |
| Lenape | L\u00ebnapeyok | Called the Delaware by English colonists. |
| Mandan | Numakiki, Nuweta | Wiped out by smallpox brought to them by settlers, the Mandan tribe numbered only in the hundreds in the mid to late nineteenth century. |
| Miami | Mihtohseeniaki, Myaamiaki | The name means \u201cthe people\u201d. Forcibly moved to Indian Territory from their traditional homelands around the great lakes. |
| Mojave | \u2019Aha Makhav | Indigenous to the Colorado river and Mojave desert across Arizona, California, Nevada and Utah, they were forced onto reservations in 1865, although many refused. |
| Navajo | Din\u00e9 | Initially hunter-gatherers, the Navajo adopted agriculture from the Puebloan peoples, then sheep and goat herding from the Spanish. |
| Nez Perce | Nim\u00edipuu | The name means \u201cwe, the people\u201d. The name Nez Perce (literally \u201cpierced nose\u201d) was coined by French Canadian fur traders in the eighteenth century. Hunter gathering lifestyle. |
| Paiute | Numa, Nuwuvi | Consisting of three separate tribes living in the Great Basin area, the Northern and Southern Paiute, and the Mono. |
| Pawnee | Pawnee | Living in what became Kansas and Nebraska, the Pawnee were so badly ravaged by attacks from the Lakota that they were relocated to the Indian Territory in the 1870s. |
| Pima | Akimel O\u2019odham | Meaning \u201criver people\u201d, the tribe lived along the Gila and Salt rivers. |
| Pomo | Pomo | Meaning \u201cthose who live at the red earth hole\u201d. |
| Quapaw | Ugahxpa | Forcibly moved to Indian Territory under the 1830 Indian Removal Act. |
| Salish | S\u00e9li\u0161 u Qlisp\u00e9 | Includes the Sanpoils and the Kootenai tribe, also called the Flatheads by colonists due to their tradition of artificially flattening the foreheads of their children. |
| Seminole | Yat\u2019siminoli | The name means \u201cfree people\u201d. One of the so-called Five Civilized Tribes. |
| Seneca | On\u00f6dow\u00e1g\u00e1 | Part of the Six Nations, aka the Iroquois League, forcibly moved to Indian Territory in the 1830s. |
| Shawnee | Various possibilities | Forcibly moved to Indian Territory under the 1830 Indian Removal Act. |
| Shoshone | Newe | The Shoshone name derives from the Shoshone word sosoni, a grass they used to make their homes. Known as \u201cGrass House People\u201d by other tribes. |
| Washo | _Wa\u0161iw_ | Means \u201cthe people from here\u201d. |
| Yuma | _Yuma / Quechan_ | The name means \u201cthose who descended\u201d. |

"""
    content = content[:ts] + new_table + content[te:]
    changes = 1
    print(f"  FIXED: Tribal Names table ({len(new_table.strip().splitlines())-2} tribes)")
    write_file(path, content)
    return changes

###############################################################################
# CH06 FIXES
###############################################################################
def fix_ch06():
    print("\n=== CH06 ===")
    path = os.path.join(BASE, '06-life-in-the-old-west.md')
    content = read_file(path)
    changes = 0

    # ---- FIX 1: General Gear Table ----
    old_gen = (
        "| Item Cost Weight Basic Rations for 1 $2 2 week Bullets / shells $1/20 Tiny "
        "Clothes (standard) 50c\u2013$2 - Clothes (fancy) $5\u201350 - "
        "Coffin $7.5 6 Deck of cards $1\u20135 Tiny Gold, 1oz $100 Tiny "
        "Handcuffs $1\u20135 Tiny Lemonade (bottle) 5c \u00bd Lockpicks (set) $5 Tiny "
        "Matches (box) 50c Tiny Newspaper 10c Tiny Oil Lantern $1 \u00bd "
        "Pelt, Bear 70c\u2013$1 2 Pelt, Bison 30-40c 2 Pelt, Wolf 50\u201370c 1 "
        "Rope, 20\u2019 length $2 \u00bd Saddle & Gear $30\u2013100 2 "
        "Silver, 1oz $10 Tiny Tobacco goods $1\u20135 Tiny |  |\n"
        "| --- | --- |\n"
        "| Whiskey, sipping (bottle) | 50c \u00bd |\n"
        "| Whiskey, good (bottle) | $2 \u00bd |"
    )
    new_gen = (
        "| Item | Cost | Weight |\n"
        "| --- | --- | --- |\n"
        "| Basic Rations for 1 week | $2 | 2 |\n"
        "| Bullets / shells | $1/20 | Tiny |\n"
        "| Clothes (standard) | 50c\u2013$2 | - |\n"
        "| Clothes (fancy) | $5\u201350 | - |\n"
        "| Coffin | $7.5 | 6 |\n"
        "| Deck of cards | $1\u20135 | Tiny |\n"
        "| Gold, 1oz | $100 | Tiny |\n"
        "| Handcuffs | $1\u20135 | Tiny |\n"
        "| Lemonade (bottle) | 5c | \u00bd |\n"
        "| Lockpicks (set) | $5 | Tiny |\n"
        "| Matches (box) | 50c | Tiny |\n"
        "| Newspaper | 10c | Tiny |\n"
        "| Oil Lantern | $1 | \u00bd |\n"
        "| Pelt, Bear | 70c\u2013$1 | 2 |\n"
        "| Pelt, Bison | 30\u201340c | 2 |\n"
        "| Pelt, Wolf | 50\u201370c | 1 |\n"
        "| Rope, 20\u2019 length | $2 | \u00bd |\n"
        "| Saddle & Gear | $30\u2013100 | 2 |\n"
        "| Silver, 1oz | $10 | Tiny |\n"
        "| Tobacco goods | $1\u20135 | Tiny |\n"
        "| Whiskey, sipping (bottle) | 50c | \u00bd |\n"
        "| Whiskey, good (bottle) | $2 | \u00bd |"
    )
    content, c = safe_replace(content, old_gen, new_gen, "General Gear table (22 items)")
    changes += c

    # ---- FIX 2: Specialized Gear Table + Orphan Separator ----
    # Find from "### Specialized Gear" to the orphan separator
    spec_start = "### Specialized Gear\n"
    spec_end = "\n\n### A Note on Prices"
    if spec_start in content and spec_end in content:
        si = content.index(spec_start) + len(spec_start)
        ei = content.index(spec_end)
        new_spec = """
| Item | Cost | Weight | Notes |
| --- | --- | --- | --- |
| Boat\u2014canoe | $40 | 4 | A light canoe designed for two people and a small amount of baggage. |
| Boat\u2014rowboat | $35 | 8 | Basic but sturdy, the rowboat can take four people easily, six at a stretch, and some baggage. |
| Camping Gear | $10 | 2 | Basic camping gear with bedrolls, canvas for shelter, a tinderbox and a pan for cooking. Gives a +1 bonus to NATURE rolls when making camp for the night. |
| Cart | $30 | N/A | A basic four-wheeled cart with space for three people sitting up front and carrying capacity for a lot of cargo. |
| Doctoring Bag | $25 | 1 | Contains basic items and simple medicines and elixirs. Gives a +1 bonus to DOCTORIN\u2019 rolls. |
| Farming equipment | $250 | Varies | Covers a wide range of equipment needed to manage a Farming Outfit. Without this, the Turn of the Season Business roll for a Farming Outfit suffers a \u22122 penalty. |
| Holster\u2014basic | $2.50 | Tiny | Nothin\u2019 fancy, just holds your gun. |
| Holster\u2014Bridgeport Rig | $50 | Tiny | A belt holder with a special clip instead of an actual holster, making it quick to draw. Can also swivel, allowing you to take a shot without drawing. Gain a +1 bonus to the Draw during a duel if the weapon is drawn. Gain a +2 bonus to the Draw for the first shot if the weapon is not drawn (but the weapon needs to be drawn to shoot again). |
| Holster\u2014Law Dog | $40 | Tiny | Made for the quick draw, this holster gives a +1 bonus to the Draw roll during a duel. |
| Holster\u2014Open-toe Swivel | $25 | Tiny | A holster with an opening through which the barrel sticks out, which can swivel, allowing a fast shot in a duel with the weapon still in the holster. Gain a +1 bonus to the Draw for the first shot, but the weapon remains in its holster\u2014it needs to be drawn to shoot again. |
| Horses, Donkeys & Mules | Varies | N/A | There are many breeds of horse to choose from. See page 120. |
| Panning equipment | $10 | Varies | Covers the range of equipment needed to manage a Panning Claim. Without this, the Turn of the Season Business roll for a Panning Outfit suffers a \u22122 penalty. |
| Lasso | $5 | \u00bd | A length of stiffened rope with a loop at one end for wrangling cattle, horses, and wayward folk. |
| Mining equipment | $25 | Varies | A wide range of equipment needed to manage a Mining Outfit. Without this, the Turn of the Season roll for a Mining Outfit suffers a \u22122 penalty. |
"""
        content = content[:si] + new_spec + content[ei:]
        changes += 1
        print("  FIXED: Specialized Gear table (14 items) + removed orphan separator")

    # ---- FIX 3: Property Location Table ----
    prop_start = "### Property Location Table\n"
    prop_end = "\n### The Homestead Act 1862"
    if prop_start in content and prop_end in content:
        pi = content.index(prop_start) + len(prop_start)
        pe = content.index(prop_end)
        new_prop = """
| Type | Location | Availability | Cost / Value |
| --- | --- | --- | --- |
| 1 | In town, rough\u2014no one wants to live here. | Very good. | Nothing\u2014feel free to stake your claim. |
| 2 | In town, outskirts\u2014a decent plot away from the latrines and ne\u2019er-do-wells, but it\u2019s not going to have a good view or a gentle brook running out back. | Good. | 1 Capital\u2014see the town clerk, pay up, and stake your claim. |
| 3 | In town, center\u2014smelly and noisy, dusty in the summer and muddy in the winter. But you\u2019re in the thick of it. | Poor\u2014competition for these plots can be fierce and violent. | 2 Capital\u2014the town clerk sells these plots, persuaded by a hefty bribe. |
| 4 | In town, prize plot\u2014only the best get to live here. | Terrible\u2014the first in town, the richest, or those with a violent manner get these plots. | 3 Capital\u2014to get this land you\u2019d best be on good terms with the gentile-types who already live there. |
| 5 | Out of town, rough\u2014160 acres of rough land given to you thanks to the Homestead Act. | Very good\u2014the one thing the West has in abundance is land. | $14 to lodge a claim, and the land is worth nothing. |
| 6 | Out of town, decent\u2014160 acres of decent land you grabbed at a steal thanks to the Homestead Act. | Good\u2014but these plots get snapped up quickly. | $14 to lodge a claim, but the land is worth 1 Capital. |
| 7 | Out of town, good\u2014sought-after real estate. | Poor. | $14 if you can claim the land under the Homestead Act. Otherwise it costs 2 Capital and another hefty bribe. |
| 8 | Out of town, superb\u2014the best land within miles, and only the best, or those with a violent manner get these plots. | Terrible\u2014the first in town, the richest, or wealthiest, can hope to acquire it. | 3 Capital\u2014rare as a rattlesnake\u2019s smile, be ready to fight to get this land. |
"""
        content = content[:pi] + new_prop + content[pe:]
        changes += 1
        print("  FIXED: Property Location table (8 rows)")

    # ---- FIX 4: D66 Compadre Attribute/Ability Table ----
    old_d66 = "D66 Attribute Ability 1 1-1 2 FIGHTIN\u2019 1 3 -14 LABOR GRIT 1 5 -1 6 PRESENCE"
    if old_d66 in content:
        # Find the full garbled line
        idx = content.index(old_d66)
        line_end = content.index('\n', idx)
        old_full = content[idx:line_end]
        new_d66 = (
            "| D66 | Attribute | Ability |\n"
            "| --- | --- | --- |\n"
            "| 11\u201312 | GRIT | FIGHTIN\u2019 |\n"
            "| 13\u201314 | GRIT | LABOR |\n"
            "| 15\u201316 | GRIT | PRESENCE |\n"
            "| 21\u201322 | QUICK | RESILIENCE |\n"
            "| 23\u201324 | QUICK | LIGHT-FINGERED |\n"
            "| 25\u201326 | QUICK | MOVE |\n"
            "| 31\u201332 | CUNNING | OPERATE |\n"
            "| 33\u201334 | CUNNING | SHOOTIN\u2019 |\n"
            "| 35\u201336 | CUNNING | ANIMAL HANDLIN\u2019 |\n"
            "| 41\u201342 | CUNNING | HAWKEYE |\n"
            "| 43\u201344 | CUNNING | INSIGHT |\n"
            "| 45\u201346 | CUNNING | NATURE |\n"
            "| 51\u201352 | DOCITY | BOOK LEARNIN\u2019 |\n"
            "| 53\u201354 | DOCITY | DOCTORIN\u2019 |\n"
            "| 55\u201356 | DOCITY | MAKIN\u2019 |\n"
            "| 61\u201362 | CHOOSE | PERFORMIN\u2019 |\n"
            "| 63\u201366 | CHOOSE | CHOOSE |"
        )
        content = content[:idx] + new_d66 + content[line_end:]
        changes += 1
        print("  FIXED: D66 Compadre Attribute/Ability table")

    # ---- FIX 5: Random Horses Table ----
    old_rh = "Horse Roll Adult Stallion Old Knacker Breeding Mare"
    if old_rh in content:
        idx = content.index(old_rh)
        # Find end - next blank line or heading
        line_end = idx
        while line_end < len(content) and content[line_end] != '\n':
            line_end += 1
        # The entire table is one line
        old_full = content[idx:line_end]
        new_rh = (
            "| Horse | Roll | Adult Stallion (1\u20133) | Old Knacker (4\u20135) | Breeding Mare (6) |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| American Quarter | 11\u201314 | $75 | $40 | $100 |\n"
            "| American Saddlebred | 15\u201322 | $100 | $50 | $125 |\n"
            "| Appaloosa (rare) | 23\u201324 | $225 | $150 | $750 |\n"
            "| Arabian (rare) | 25\u201326 | $250 | $200 | $1000 |\n"
            "| Cayuse (rare) | 31\u201332 | $225 | $150 | $750 |\n"
            "| Criollo | 33\u201335 | $125 | $60 | $250 |\n"
            "| Missouri Fox Trotter | 36\u201342 | $75 | $40 | $100 |\n"
            "| Morgan | 43\u201345 | $100 | $50 | $150 |\n"
            "| Mustang | 46\u201352 | $50 | $30 | $75 |\n"
            "| Paint / Pinto | 53\u201356 | $100 | $50 | $100 |\n"
            "| Palomino | 61\u201363 | $150 | $100 | $250 |\n"
            "| Tennessee Walker | 64\u201366 | $50 | $30 | $100 |\n"
            "| Donkey / Mule | \u2014 | $25 | $15 | N/A |"
        )
        content = content[:idx] + new_rh + content[line_end:]
        changes += 1
        print("  FIXED: Random Horses table (13 breeds)")

    # ---- FIX 6: Horse Breed Stats Table ----
    old_hbs_marker = "| Horse ModifierRiding |"
    if old_hbs_marker in content:
        hbs_start = content.index(old_hbs_marker)
        # Find end - after the Donkey/Mule line
        hbs_search = content[hbs_start:]
        donkey_marker = "| Donkey / Mule"
        dm_idx = hbs_search.index(donkey_marker)
        hbs_end = hbs_start + dm_idx + hbs_search[dm_idx:].index('\n') + 1

        new_hbs = (
            "| Horse | Riding Mod | Grit | Quick | Cunning | FIGHTIN\u2019 | RESILIENCE | Qualities | Flaws |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
            "| American Quarter | 0 | 5 | 4 | 3 | 1 | 2 | FAST, +1 Random | +2 Random |\n"
            "| American Saddlebred | 0 | 6 | 2 | 3 | 1 | 2 | HARDY, +1 Random | +2 Random |\n"
            "| Appaloosa (rare) | \u22121 | 7 | 3 | 3 | 1 | 3 | STEADY, PAINTED COAT, +1 Random | HARD RIDING, +1 Random |\n"
            "| Arabian (rare) | 0 | 4 | 5 | 2 | 1 | 2 | FAST, GRACEFUL, +1 Random | TEMPERAMENTAL, +2 Random |\n"
            "| Cayuse (rare) | 0 | 5 | 4 | 3 | 3 | 2 | ORNERY, STRONG, +1 Random | UNRULY, +1 Random |\n"
            "| Criollo | 0 | 6 | 2 | 4 | 0 | 4 | STAMINA, +1 Random | +2 Random |\n"
            "| Missouri Fox Trotter | +1 | 6 | 3 | 4 | 1 | 3 | EASY TO RIDE, +1 Random | +2 Random |\n"
            "| Morgan | 0 | 4 | 5 | 3 | 1 | 2 | FAST, +1 Random | +2 Random |\n"
            "| Mustang | \u22121 | 5 | 4 | 4 | 1 | 0 | HOT HORSE, +1 Random | HARD RIDING, +1 Random |\n"
            "| Paint / Pinto | +1 | 5 | 4 | 3 | 1 | 2 | PAINTED COAT, SUREFOOTED, +1 Random | +2 Random |\n"
            "| Palomino | +1 | 4 | 3 | 4 | 0 | 0 | GRACEFUL, +1 Random | NO FIGHTIN\u2019 SPIRIT, +1 Random |\n"
            "| Tennessee Walker | 0 | 4 | 5 | 3 | 0 | 0 | SUREFOOTED, +1 Random | +2 Random |\n"
            "| Donkey / Mule | 0 | 6 | 2 | 2 | 0 | 1 | ORNERY | STUBBORN |\n"
        )
        content = content[:hbs_start] + new_hbs + content[hbs_end:]
        changes += 1
        print("  FIXED: Horse Breed Stats table (13 breeds)")

    # ---- FIX 7: Weapon Qualities - Ranged (plain text -> table) ----
    wqr_marker = "### Weapon Qualities - Ranged\n"
    wqr_end = "### Weapon Qualities - Melee\n"
    if wqr_marker in content and wqr_end in content:
        wqr_si = content.index(wqr_marker) + len(wqr_marker)
        wqr_ei = content.index(wqr_end)
        new_wqr = """
| Weapon | Quality | Impact |
| --- | --- | --- |
| Pistol | CALIBRATED | The weapon is so well calibrated its aim is true. Gain +1 bonus to the weapon\u2019s Attack modifier. |
| Pistol | CONCEALABLE | Small and compact, a pistol with this quality is easily concealed about your person. Those trying to spot it get a \u22121 penalty on their HAWKEYE test. |
| Pistol | FANNING | The gun is ideal for fanning. You gain a +1 bonus to your SHOOTIN\u2019 ability when fanning with this weapon. |
| Pistol | FAST DRAW | The weapon is designed for the quick draw. You gain a +1 bonus to the Draw. |
| Pistol | HEAVY | The pistol is heavy in your hand and kicks like a mule but delivers a powerful blast. It does +1 extra damage, but has a \u22121 penalty to Draw. |
| Pistol | HIDDEN | A palm-sized gun designed for concealment. Those trying to spot it suffer a \u22123 penalty on their HAWKEYE test. |
| Pistol | HOT LOADER | Loading is slow, so anything that makes it quicker can only be a good thing. This gun has a swappable revolver cylinder (2 actions for full reload). |
| Pistol | LIGHT | The weapon is very small and counts as a Tiny item, but it\u2019s not made for fast drawing so you suffer a \u22121 penalty on the Draw. |
| Pistol | LONG BARREL | A long barrel makes gunplay easier, but it\u2019s slower on the draw. Gain a +1 bonus to SHOOTIN\u2019, but a \u22121 penalty on the Draw. |
| Pistol | SHORT BARREL | A short barrel isn\u2019t great for accuracy, but it\u2019s quicker to get that iron from your holster. Gain a +1 bonus on Draw, but a \u22121 penalty on SHOOTIN\u2019. |
| Pistol | SIGHTS | Well-made sights make shooting at range easy. Range negatives are one die less for all ranges when using an Aim action before making a shot. |
| Any | BALANCED | The weapon feels good in your hand and you can\u2019t help but shoot straight with it. Grants a +1 bonus to SHOOTIN\u2019. |
| Any | MAINTAINED | Beautifully made with maintenance in mind, this weapon is easy to keep working. Once per scene you may reroll all Trouble dice showing a \u20181\u2019, but only before pushing. |
| Any | PIERCING | The weapon is renowned for being deadly in the hands of an expert. Gain +1 to the Units die on critical injury rolls. |
| Any | POWERFUL | The weapon packs a real punch. Grants +1 to the weapon\u2019s Damage. |
| Any | RELIABLE | Tough and sturdy, this weapon is reliable and just doesn\u2019t break. If Trouble is rolled while using this weapon, the amount of Trouble is reduced by 1, to a minimum of 1. |
| Shotgun | SAWN-OFF | A short-barreled shotgun is deadly in close quarters, but terrible further away. Grants a +1 bonus to SHOOTIN\u2019 but the maximum range is Short. |

**Wells Fargo Coachgun**

"""
        content = content[:wqr_si] + new_wqr + content[wqr_ei:]
        changes += 1
        print("  FIXED: Weapon Qualities - Ranged table")

    # ---- FIX 8: Weapon Qualities - Melee (plain text -> table) ----
    wqm_marker = "### Weapon Qualities - Melee\n"
    wqm_end = "### Weapon Conditions (Ranged)\n"
    if wqm_marker in content and wqm_end in content:
        wqm_si = content.index(wqm_marker) + len(wqm_marker)
        wqm_ei = content.index(wqm_end)
        new_wqm = """
| Weapon | Quality | Impact |
| --- | --- | --- |
| Any | BALANCED | The weapon sits well in your hand and helps you make the blow. Grants a +1 bonus to FIGHTIN\u2019. |
| Any | FORGIVING | The weapon is reliable and easy to use. You can ignore one die of Trouble on your first roll when using this weapon as if you had spent a point of Faith (but not after a pushed roll). |
| Any | MOUNTED | This weapon is especially deadly when used from horseback. After a pushed roll, when mounted, you can push again for free, although Trouble still applies. |
| Any | PIERCING | The weapon is renowned for being deadly in the hands of an expert. Grants +1 to the Units die on critical injury rolls. |
| Any | SHARPENED | The weapon is made to inflict as much damage as possible. Gain +1 to the weapon\u2019s Damage. |
| Any | SLEEK | It\u2019s designed to be drawn fast. You can draw this weapon as a free action. |
| Any | TOUGHENED | The weapon cannot be broken by the outcome of Trouble. |
| Any | WEIGHTED | The weapon is beautifully weighted to give you an advantage in the fight. Gain a +1 bonus to FIGHTIN\u2019. |

"""
        content = content[:wqm_si] + new_wqm + content[wqm_ei:]
        changes += 1
        print("  FIXED: Weapon Qualities - Melee table")

    # ---- FIX 9: Weapon Conditions - Ranged (plain text -> table) ----
    wcr_marker = "### Weapon Conditions (Ranged)\n"
    wcr_end = "### Weapon Conditions (Melee)\n"
    if wcr_marker in content and wcr_end in content:
        wcr_si = content.index(wcr_marker) + len(wcr_marker)
        wcr_ei = content.index(wcr_end)
        new_wcr = """
| D6 | Condition | Impact |
| --- | --- | --- |
| 1 | DIRTY | When you attack with this weapon your final total of successes is reduced by 1, to a minimum of 0. |
| 2 | DAMAGED BORE | The weapon is low powered. The damage rating is reduced by 1, to a minimum of 1. |
| 3 | HARD TO LOAD | Loading takes an extra action per bullet. |
| 4 | GREASY | The weapon loses its punch, and its Crit Rating is increased by 1. |
| 5 | MISALIGNED | The weapon ain\u2019t shootin\u2019 straight. Suffer a \u22121 penalty on SHOOTIN\u2019 rolls. |
| 6 | WEAK HAMMER | If the weapon suffers Trouble twice in the same scene it breaks beyond repair. |

"""
        content = content[:wcr_si] + new_wcr + content[wcr_ei:]
        changes += 1
        print("  FIXED: Weapon Conditions - Ranged table")

    # ---- FIX 10: Weapon Conditions - Melee (plain text -> table) ----
    wcm_marker = "### Weapon Conditions (Melee)\n"
    wcm_end = "### Gambling\n"
    if wcm_marker in content and wcm_end in content:
        wcm_si = content.index(wcm_marker) + len(wcm_marker)
        wcm_ei = content.index(wcm_end)
        new_wcm = """
| D6 | Condition | Impact |
| --- | --- | --- |
| 1 | BLUNT | When you attack with this weapon your final total of successes is reduced by 1, to a minimum of 0. |
| 2 | LOOSE HANDLE | The weapon loses its punch, and its Crit Rating is increased by 1. |
| 3 | BENT | The weapon is bent or twisted, and harder to handle. Suffer a \u22121 penalty to FIGHTIN\u2019 rolls. |
| 4 | HARD TO HOLD | When you suffer Trouble after a pushed roll, add +1 to the Trouble total when using this weapon. |
| 5 | CHIPPED | Your weapon loses a random weapon quality. |
| 6 | WEAKENED | If the weapon suffers Trouble twice in the same scene it breaks beyond repair. |

"""
        content = content[:wcm_si] + new_wcm + content[wcm_ei:]
        changes += 1
        print("  FIXED: Weapon Conditions - Melee table")

    # ---- FIX 11: Damned Cards Table ----
    dct_marker = "D6 The damned cards Cheat Bluff Play"
    if dct_marker in content:
        idx = content.index(dct_marker)
        # Find end of the garbled block (6 entries, all on ~one line)
        line_end = idx
        while line_end < len(content) and content[line_end] != '\n':
            line_end += 1
        # Check next few lines for continuation
        after = content[line_end+1:]
        extra_end = 0
        for i, ch in enumerate(after):
            if ch == '\n':
                next_line = after[i+1:after.index('\n', i+1)] if '\n' in after[i+1:] else ''
                if not next_line.strip() or next_line.startswith('#') or next_line.startswith('\n'):
                    extra_end = i + 1
                    break

        new_dct = (
            "| D6 | The damned cards | Cheat | Bluff | Play |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| 1 | The deck is givin\u2019 you nothin\u2019! | +3 | 0 | \u22122 |\n"
            "| 2 | The cards are angry with you | +2 | +1 | \u22121 |\n"
            "| 3 | Just about evens, but you\u2019re not happy | +1 | +2 | 0 |\n"
            "| 4 | Just about evens, but it\u2019s ok | 0 | +2 | +1 |\n"
            "| 5 | The deck is lovin\u2019 you, givin\u2019 you all you want! | \u22121 | +1 | +2 |\n"
            "| 6 | Aces high! You\u2019re on a killin\u2019 run! | \u22122 | 0 | +3 |"
        )
        content = content[:idx] + new_dct + content[line_end:]
        changes += 1
        print("  FIXED: Damned Cards table")

    # ---- FIX 12: NPC Stat Blocks ----
    # Process each NPC stat block: find lines containing "GRIT X QUICK X CUNNING X DOCITY X"
    # followed by skills, description, Talents: line, and Gear: line
    npc_pattern = re.compile(
        r'^([^\n]+?GRIT\s+\d\s+QUICK\s+\d\s+CUNNING\s+\d\s+DOCITY\s+\d\s+.+?)$',
        re.MULTILINE
    )
    npc_count = 0
    for m in npc_pattern.finditer(content):
        raw_line = m.group(1)
        # Skip if already formatted (starts with **)
        if raw_line.strip().startswith('**'):
            continue
        parsed = parse_npc(raw_line)
        if not parsed:
            continue
        name, attrs, skill_line, desc = parsed

        # Find Talents and Gear lines after this stat block
        after_pos = m.end()
        remaining = content[after_pos:after_pos + 500]

        talents_line = ""
        gear_line = ""
        talents_match = re.search(r'\nTalents:\s*(.+?)\.', remaining)
        gear_match = re.search(r'\nGear:\s*(.+?)\.', remaining)

        # Build the replacement
        formatted = f"**{name}** \u2014 {attrs}\n{skill_line}"
        if desc:
            formatted += f"\n{desc}"

        # Replace the stat block line
        old_text = raw_line
        content = content.replace(old_text, formatted, 1)
        npc_count += 1

        # Fix Talents line (add bold)
        if talents_match:
            old_talents = "Talents:" + talents_match.group(0).split("Talents:", 1)[1]
            old_talents = old_talents.rstrip()
            new_talents = format_talents(old_talents.strip())
            if old_talents in content:
                content = content.replace(old_talents, new_talents, 1)

        # Fix Gear line (add bold)
        if gear_match:
            old_gear = "Gear:" + gear_match.group(0).split("Gear:", 1)[1]
            old_gear = old_gear.rstrip()
            new_gear = format_gear(old_gear.strip())
            if old_gear in content:
                content = content.replace(old_gear, new_gear, 1)

    if npc_count:
        changes += 1
        print(f"  FIXED: {npc_count} NPC stat blocks reformatted")

    if changes:
        write_file(path, content)
    return changes

###############################################################################
# CH09 FIXES
###############################################################################
def fix_ch09():
    print("\n=== CH09 ===")
    path = os.path.join(BASE, '09-the-new-mexico-campaign.md')
    content = read_file(path)
    changes = 0

    # Fix NPC stat blocks
    npc_pattern = re.compile(
        r'^([^\n]+?GRIT\s+\d\s+QUICK\s+\d\s+CUNNING\s+\d\s+DOCITY\s+\d\s+.+?)$',
        re.MULTILINE
    )
    for m in npc_pattern.finditer(content):
        raw_line = m.group(1)
        if raw_line.strip().startswith('**'):
            continue
        parsed = parse_npc(raw_line)
        if not parsed:
            continue
        name, attrs, skill_line, desc = parsed
        formatted = f"**{name}** \u2014 {attrs}\n{skill_line}"
        if desc:
            formatted += f"\n{desc}"
        content = content.replace(raw_line, formatted, 1)
        changes += 1

    # Fix Talents lines
    for tm in re.finditer(r'^Talents:\s+.+?\.$', content, re.MULTILINE):
        old_t = tm.group(0)
        new_t = format_talents(old_t)
        content = content.replace(old_t, new_t, 1)

    # Fix orphan separators + weapon data for CLARENCE KING
    # |---|---|---|---|---|---|---|---|
    # |Colt 45 Peacemaker|Single|-1|+1|3|1|Medium|6|
    old_ck_weapons = (
        "|---|---|---|---|---|---|---|---|\n"
        "|Colt 45 Peacemaker|Single|-1|+1|3|1|Medium|6|"
    )
    new_ck_weapons = (
        WEAPON_HEADER + "\n"
        "| Colt 45 Peacemaker | Single | -1 | +1 | 3 | 1 | Medium | 6 |"
    )
    content, c = safe_replace(content, old_ck_weapons, new_ck_weapons,
                              "Clarence King weapon table")
    changes += c

    # Fix PHELIM QUINLIVAN weapon table (plain text format)
    old_pq_weapons = (
        "DRAW  ATTACK\n"
        "WEAPON ACTION DAMAGE CRITICAL RANGE AMMO\n"
        "MOD MOD\n"
        "Quality Blade N/A - +1 1 1 Arms -\n"
        "Colt 45 Peacemaker Single -1 +1 3 1 Medium 6"
    )
    if old_pq_weapons not in content:
        # Try alternate spacing
        old_pq_weapons = "DRAW  ATTACK"
        pq_idx = content.find(old_pq_weapons)
        if pq_idx != -1:
            # Find the block from DRAW to end of weapon data
            block_end = pq_idx
            lines_after = content[pq_idx:pq_idx+500].split('\n')
            weapon_lines = 0
            for i, line in enumerate(lines_after):
                if i == 0:
                    continue  # DRAW ATTACK header
                stripped = line.strip()
                if stripped.startswith('WEAPON') or stripped.startswith('MOD'):
                    continue
                if stripped and not stripped.startswith('#') and not stripped.startswith('\n'):
                    # Could be weapon data
                    if any(w in stripped for w in ['Blade', 'Peacemaker', 'Single', 'Lever', 'Double', 'Breech', 'Walker', 'Winchester', 'Spencer', 'Cooper', 'Shotgun', 'Kosh', 'Metropolitan', 'Carbine']):
                        weapon_lines = i
                    else:
                        break
                else:
                    break
            if weapon_lines > 0:
                old_block = '\n'.join(lines_after[:weapon_lines+1])
                # Parse weapons from the plain text
                weapon_data = '\n'.join(lines_after[3:weapon_lines+1])  # Skip headers
                new_block = WEAPON_HEADER
                # Manually parse Quinlivan's weapons
                new_block += "\n| Quality Blade | N/A | \u2014 | +1 | 1 | 1 | Arms | \u2014 |"
                new_block += "\n| Colt 45 Peacemaker | Single | -1 | +1 | 3 | 1 | Medium | 6 |"
                content = content.replace(old_block, new_block, 1)
                changes += 1
                print("  FIXED: Quinlivan weapon table")

    if changes:
        write_file(path, content)
    return changes

###############################################################################
# CH10 FIXES
###############################################################################
def fix_ch10():
    print("\n=== CH10 ===")
    path = os.path.join(BASE, '10-patience-is-a-virtue.md')
    content = read_file(path)
    changes = 0

    # Fix NPC stat blocks (same approach as Ch06/09)
    npc_pattern = re.compile(
        r'^([^\n]+?GRIT\s+\d\s+QUICK\s+\d\s+CUNNING\s+\d\s+DOCITY\s+\d\s+.+?)$',
        re.MULTILINE
    )
    npc_count = 0
    for m in npc_pattern.finditer(content):
        raw_line = m.group(1)
        if raw_line.strip().startswith('**'):
            continue
        parsed = parse_npc(raw_line)
        if not parsed:
            continue
        name, attrs, skill_line, desc = parsed
        formatted = f"**{name}** \u2014 {attrs}\n{skill_line}"
        if desc:
            formatted += f"\n{desc}"
        content = content.replace(raw_line, formatted, 1)
        npc_count += 1

    if npc_count:
        changes += 1
        print(f"  FIXED: {npc_count} NPC stat blocks reformatted")

    # Fix Talents lines
    for tm in re.finditer(r'^Talents:\s+.+?\.$', content, re.MULTILINE):
        old_t = tm.group(0)
        new_t = format_talents(old_t)
        if old_t in content:
            content = content.replace(old_t, new_t, 1)

    # Fix all orphan separators + weapon rows
    # Pattern: |---|...|  followed by weapon data rows
    orphan_pattern = re.compile(
        r'\|---\|---\|---\|---\|---\|---\|---\|---\|\n'
        r'(\|.+?\|(?:\n\|.+?\|)*)',
        re.MULTILINE
    )
    for om in orphan_pattern.finditer(content):
        old_weapon_block = om.group(0)
        weapon_rows = om.group(1)
        new_weapon_block = WEAPON_HEADER + "\n" + weapon_rows
        content = content.replace(old_weapon_block, new_weapon_block, 1)
        changes += 1
        print(f"  FIXED: Orphan separator -> weapon table header")

    # Fix remaining standalone orphan separators (no weapon data after)
    standalone_orphan = "|---|---|---|---|---|---|---|---|\n"
    while standalone_orphan in content:
        # Check what's after it
        idx = content.index(standalone_orphan)
        after = content[idx + len(standalone_orphan):idx + len(standalone_orphan) + 100]
        if after.strip().startswith('|') and not after.strip().startswith('|---'):
            break  # Has data, skip (should have been caught above)
        content = content.replace(standalone_orphan, "", 1)
        changes += 1
        print("  FIXED: Removed standalone orphan separator")

    # Fix the garbled dog table header
    old_dog = '|**DOG**||||**ABILITIES**|**ABILITIES**|**ABILITIES**|**ATTACKS**|\n|---|---|---|---|---|---|---|---|'
    if old_dog in content:
        # This is a garbled header for Tyler Peyton's dog (Digger) with no data after it
        # The dog stats were lost in extraction - remove the garbled header
        content = content.replace(old_dog, "", 1)
        changes += 1
        print("  FIXED: Removed garbled dog table header (no data)")

    # Fix plain-text weapon tables (DRAW ATTACK format)
    draw_pattern = re.compile(
        r'^DRAW\s+ATTACK\n'
        r'WEAPON\s+ACTION\s+DAMAGE\s+CRITICAL\s+RANGE\s+AMMO\n'
        r'MOD\s+MOD\n'
        r'(.+?)(?=\n\n|\n[A-Z\*\|#]|\n\*\*)',
        re.MULTILINE | re.DOTALL
    )

    # Manually fix known weapon tables in Ch10
    weapon_replacements = [
        # Floyd Higgins
        ("DRAW  ATTACK\nWEAPON ACTION DAMAGE CRITICAL RANGE AMMO\nMOD MOD\nWinchester 1873 Lever N/A +2 2 1 Long 15\nHunting Blade N/A N/A +2 2 1 Arms -",
         WEAPON_HEADER + "\n| Winchester 1873 | Lever | N/A | +2 | 2 | 1 | Long | 15 |\n| Hunting Blade | N/A | N/A | +2 | 2 | 1 | Arms | \u2014 |"),
        # Tyler Peyton
        ("DRAW  ATTACK\nWEAPON ACTION DAMAGE CRITICAL RANGE AMMO\nMOD MOD\nMetropolitan Navy  Single 0 +1 2 1 Medium 6\n1864\nHunting Blade N/A N/A +1 2 1 Arms N/A",
         WEAPON_HEADER + "\n| Metropolitan Navy 1864 | Single | 0 | +1 | 2 | 1 | Medium | 6 |\n| Hunting Blade | N/A | N/A | +1 | 2 | 1 | Arms | N/A |"),
        # Billy Conway
        ("DRAW  ATTACK\nWEAPON ACTION DAMAGE CRITICAL RANGE AMMO\nMOD MOD\nShotgun Breech N/A +1 3 3 Medium 2\nHunting Blade N/A N/A +1 2 1 Arms N/A",
         WEAPON_HEADER + "\n| Shotgun | Breech | N/A | +1 | 3 | 3 | Medium | 2 |\n| Hunting Blade | N/A | N/A | +1 | 2 | 1 | Arms | N/A |"),
        # Maxwell Kinnear
        ("DRAW  ATTACK\nWEAPON ACTION DAMAGE CRITICAL RANGE AMMO\nMOD MOD\nColt Walker Single -2 +1 2 1 Medium 6\nHunting Blade N/A N/A +1 2 1 Arms N/A",
         WEAPON_HEADER + "\n| Colt Walker | Single | -2 | +1 | 2 | 1 | Medium | 6 |\n| Hunting Blade | N/A | N/A | +1 | 2 | 1 | Arms | N/A |"),
        # Julius Halliday
        ("DRAW  ATTACK\nWEAPON ACTION DAMAGE CRITICAL RANGE AMMO\nMOD MOD\nMetropolitan Navy  Single 0 +1 2 1 Medium 6\n1864\nKosh N/A N/A 0 1 3 Arms N/A",
         WEAPON_HEADER + "\n| Metropolitan Navy 1864 | Single | 0 | +1 | 2 | 1 | Medium | 6 |\n| Kosh | N/A | N/A | 0 | 1 | 3 | Arms | N/A |"),
    ]

    for old_w, new_w in weapon_replacements:
        if old_w in content:
            content = content.replace(old_w, new_w, 1)
            changes += 1
            print(f"  FIXED: Weapon table (DRAW ATTACK format)")
        else:
            # Try with different line endings
            old_w_crlf = old_w.replace('\n', '\r\n')
            if old_w_crlf in content:
                content = content.replace(old_w_crlf, new_w.replace('\n', '\r\n'), 1)
                changes += 1
                print(f"  FIXED: Weapon table (DRAW ATTACK format, CRLF)")

    # Fix the dog stat table for Floyd Higgins
    old_dogs = "ABILITIES FIGHTIN'  MOVE HAWKEYE\nDOGS GRIT QUICK CUNNING ATTACKS\n                                                                       (GRIT) (QUICK) (CUNNING)\nGuard Dog  4 3 2 3 2 1 Bite: Damage 2, Crit 2\nScarlet\n(+1 to FIGHTIN\u2019 when Grappling)\nTracker  2 4 3 0 2 3 Bite: Damage 1, Crit 2\nDog Rebel"
    if old_dogs in content:
        new_dogs = (
            "| Dog | GRIT | QUICK | CUNNING | FIGHTIN\u2019 | MOVE | HAWKEYE | Attacks |\n"
            "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
            "| Guard Dog Scarlet | 4 | 3 | 2 | 3 | 2 | 1 | Bite: Damage 2, Crit 2 (+1 to FIGHTIN\u2019 when Grappling) |\n"
            "| Tracker Dog Rebel | 2 | 4 | 3 | 0 | 2 | 3 | Bite: Damage 1, Crit 2 |"
        )
        content = content.replace(old_dogs, new_dogs, 1)
        changes += 1
        print("  FIXED: Floyd Higgins dog stat table")

    if changes:
        write_file(path, content)
    return changes

###############################################################################
# MAIN
###############################################################################
def main():
    total = 0
    total += fix_ch08()
    total += fix_ch07()
    total += fix_ch06()
    total += fix_ch09()
    total += fix_ch10()
    print(f"\n{'='*60}")
    print(f"TOTAL FIXES APPLIED: {total}")

if __name__ == '__main__':
    main()
