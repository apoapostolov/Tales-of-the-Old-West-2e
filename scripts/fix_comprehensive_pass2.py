#!/usr/bin/env python3
"""Fix remaining garbled content after the first pass."""
import re
import os

BASE = r'c:\git-public\Tales-of-the-Old-West-2e\corebook'

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)

# Apostrophe variants
AP = "[\u2019']"

# Skill regex that handles both Unicode and ASCII apostrophes
SKILL_RE = re.compile(
    rf"(ANIMAL HANDLIN{AP}|BOOK LEARNIN{AP}|BOOKLEARNIN{AP}|LIGHT-FINGERED|"
    rf"PERFORMIN{AP}|SHOOTIN{AP}|FIGHTIN{AP}|DOCTORIN{AP}|RESILIENCE|PRESENCE|"
    rf"HAWKEYE|INSIGHT|NATURE|OPERATE|MAKIN{AP}|LABOR|MOVE)\s+(\d)"
)

WEAPON_HEADER = "| Weapon | Action | Draw Mod | Attack Mod | Damage | Critical | Range | Ammo |\n| --- | --- | --- | --- | --- | --- | --- | --- |"

def fix_garbled_skill_line(line):
    """Fix a line that has garbled skills mixed with description."""
    skills = []
    last_end = 0
    for m in SKILL_RE.finditer(line):
        skills.append(f"{m.group(1)} {m.group(2)}")
        last_end = m.end()
    if skills:
        desc = line[last_end:].strip()
        result = ", ".join(skills)
        if desc:
            result += "\n" + desc
        return result
    return line

def parse_single_line_weapons(line):
    """Parse a single-line DRAW ATTACK weapon block into a proper table."""
    # Remove the header portion
    # Pattern: DRAW  ATTACK WEAPON ACTION DAMAGE CRITICAL RANGE AMMO MOD MOD <weapon data>
    cleaned = re.sub(
        r'^DRAW\s+ATTACK\s+WEAPON\s+ACTION\s+DAMAGE\s+CRITICAL\s+RANGE\s+AMMO\s+MOD\s+MOD\s*',
        '', line
    )
    if not cleaned.strip():
        return WEAPON_HEADER

    # Known weapon names (order matters - longer names first)
    weapon_names = [
        "Metropolitan Navy", "Colt 45 Peacemaker", "Colt Walker",
        "Winchester 1873", "Spencer Carbine", "Quality Blade",
        "Hunting Blade", "Shotgun", "Cooper", "Kosh"
    ]

    rows = []
    text = cleaned.strip()

    while text:
        text = text.strip()
        if not text:
            break
        matched = False
        for wname in weapon_names:
            if text.startswith(wname):
                after = text[len(wname):].strip()
                # Check if next word is a continuation of weapon name (e.g., "1864" for Metropolitan Navy)
                # Special case: Metropolitan Navy 1864
                if wname == "Metropolitan Navy":
                    # Action types
                    action_types = ['Single', 'Double', 'Lever', 'Breech', 'N/A']
                    first_word = after.split()[0] if after.split() else ''
                    if first_word not in action_types:
                        # Next word is part of weapon name
                        wname = wname + " " + first_word
                        after = after[len(first_word):].strip()

                parts = after.split(None, 6)
                if len(parts) >= 7:
                    rows.append(f"| {wname} | {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {parts[6].split()[0] if parts[6].split() else parts[6]} |")
                    # Calculate remaining text
                    consumed = len(wname) + (len(text) - len(text.lstrip()))
                    for p in parts[:7]:
                        pass
                    # Rebuild remaining from after the 7th field
                    remaining_parts = parts[6].split(None, 1)
                    text = remaining_parts[1] if len(remaining_parts) > 1 else ""
                elif len(parts) >= 1:
                    # Incomplete row
                    rows.append(f"| {wname} | {' | '.join(parts)} |")
                    text = ""
                matched = True
                break
        if not matched:
            # Try to skip unknown text
            break

    if rows:
        return WEAPON_HEADER + "\n" + "\n".join(rows)
    return WEAPON_HEADER

###############################################################################
# FIX CH09
###############################################################################
def fix_ch09():
    print("\n=== CH09 PASS 2 ===")
    path = os.path.join(BASE, '09-the-new-mexico-campaign.md')
    content = read_file(path)
    changes = 0

    # Fix the single-line DRAW ATTACK weapon table for Quinlivan
    draw_re = re.compile(r'^DRAW\s+ATTACK\s+WEAPON\s+ACTION\s+DAMAGE\s+CRITICAL\s+RANGE\s+AMMO\s+MOD\s+MOD\s+.+$', re.MULTILINE)
    for m in draw_re.finditer(content):
        old_line = m.group(0)
        new_table = parse_single_line_weapons(old_line)
        content = content.replace(old_line, new_table, 1)
        changes += 1
        print(f"  FIXED: Single-line weapon table -> proper table")

    if changes:
        write_file(path, content)
    return changes

###############################################################################
# FIX CH10
###############################################################################
def fix_ch10():
    print("\n=== CH10 PASS 2 ===")
    path = os.path.join(BASE, '10-patience-is-a-virtue.md')
    content = read_file(path)
    changes = 0

    # Fix single-line DRAW ATTACK weapon tables
    draw_re = re.compile(r'^DRAW\s+ATTACK\s+WEAPON\s+ACTION\s+DAMAGE\s+CRITICAL\s+RANGE\s+AMMO\s+MOD\s+MOD\s+.+$', re.MULTILINE)
    for m in draw_re.finditer(content):
        old_line = m.group(0)
        new_table = parse_single_line_weapons(old_line)
        content = content.replace(old_line, new_table, 1)
        changes += 1
        print(f"  FIXED: Single-line weapon table")

    # Fix remaining orphan separators with weapon data
    orphan_re = re.compile(
        r'\|---\|---\|---\|---\|---\|---\|---\|---\|\n+'
        r'(\|[^-].+?\|(?:\n\|[^-].+?\|)*)',
        re.MULTILINE
    )
    for om in orphan_re.finditer(content):
        old_block = om.group(0)
        weapon_rows = om.group(1)
        new_block = WEAPON_HEADER + "\n" + weapon_rows
        content = content.replace(old_block, new_block, 1)
        changes += 1
        print("  FIXED: Orphan separator + weapon data -> proper table")

    # Fix standalone orphan separators (no weapon data)
    standalone_re = re.compile(r'^\|---\|---\|---\|---\|---\|---\|---\|---\|\s*$', re.MULTILINE)
    for sm in standalone_re.finditer(content):
        old = sm.group(0)
        content = content.replace(old + '\n', '', 1)
        changes += 1
        print("  FIXED: Removed standalone orphan separator")

    # Fix garbled skill lines: lines that have SKILL  VALUE  SKILL  VALUE patterns
    # These are lines after the NPC header that still have wide-spacing skills
    garbled_skill_re = re.compile(
        rf'^({AP.join(["PERFORMIN", "SHOOTIN", "FIGHTIN", "DOCTORIN", "RESILIENCE", "ANIMAL HANDLIN", "BOOK LEARNIN", "BOOKLEARNIN", "LIGHT-FINGERED", "PRESENCE", "HAWKEYE", "INSIGHT", "NATURE", "OPERATE", "MAKIN", "LABOR", "MOVE"])})',
    )

    # More targeted: find lines that have a skill name followed by spaces and a digit
    skill_line_re = re.compile(
        rf"^((?:PERFORMIN{AP}|SHOOTIN{AP}|FIGHTIN{AP}|DOCTORIN{AP}|RESILIENCE|PRESENCE|"
        rf"HAWKEYE|INSIGHT|NATURE|OPERATE|MAKIN{AP}|LABOR|MOVE|ANIMAL HANDLIN{AP}|"
        rf"BOOK LEARNIN{AP}|BOOKLEARNIN{AP}|LIGHT-FINGERED)"
        rf"\s+\d.+)$",
        re.MULTILINE
    )

    for sm in skill_line_re.finditer(content):
        old_line = sm.group(0)
        # Only fix if line has wide spacing (garbled)
        if '  ' in old_line:
            new_line = fix_garbled_skill_line(old_line)
            if new_line != old_line:
                content = content.replace(old_line, new_line, 1)
                changes += 1
                print(f"  FIXED: Garbled skill line")

    # Fix wolf table
    wolf_marker = "ABILITIES FIGHTIN\u2019  MOVE HAWKEYE\nWOLVES GRIT QUICK CUNNING ATTACKS\n"
    wolf_marker2 = "ABILITIES FIGHTIN'  MOVE HAWKEYE\nWOLVES GRIT QUICK CUNNING ATTACKS\n"

    for wm in [wolf_marker, wolf_marker2]:
        if wm in content:
            # Find the full wolf block
            idx = content.index(wm)
            # Find end - next heading or blank line after data
            block_text = content[idx:idx+600]
            # Find end of wolf data (before next ### or before a blank line followed by non-wolf text)
            end_markers = ['### Picking Up', '\n\n###']
            block_end = len(block_text)
            for em in end_markers:
                if em in block_text:
                    block_end = min(block_end, block_text.index(em))

            old_wolf = content[idx:idx+block_end].rstrip()
            new_wolf = (
                "| Wolf | GRIT | QUICK | CUNNING | FIGHTIN\u2019 | MOVE | HAWKEYE | Attacks |\n"
                "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
                "| Alpha Wolf | 4 | 4 | 4 | 4 | 4 | 4 | Bite: Damage 2, Crit 1 (+1 to FIGHTIN\u2019 when Grappling). Pack: Damage 3, Crit 1, +3 bonus to attack rolls |\n"
                "| Gray Wolf | 3 | 4 | 4 | 3 | 4 | 4 | Bite: Damage 2, Crit 1 (+1 to FIGHTIN\u2019 when Grappling). Pack: Damage 3, Crit 1, +3 bonus to attack rolls |"
            )
            content = content[:idx] + new_wolf + content[idx+block_end:]
            changes += 1
            print("  FIXED: Wolf stat table")
            break

    # Fix Floyd Higgins' dog table
    dog_marker = "ABILITIES FIGHTIN\u2019  MOVE HAWKEYE\nDOGS GRIT QUICK CUNNING ATTACKS\n"
    dog_marker2 = "ABILITIES FIGHTIN'  MOVE HAWKEYE\nDOGS GRIT QUICK CUNNING ATTACKS\n"

    for dm in [dog_marker, dog_marker2]:
        if dm in content:
            idx = content.index(dm)
            block_text = content[idx:idx+400]
            end_markers = ['### Tyler', '\n\n###']
            block_end = len(block_text)
            for em in end_markers:
                if em in block_text:
                    block_end = min(block_end, block_text.index(em))

            old_dogs = content[idx:idx+block_end].rstrip()
            new_dogs = (
                "| Dog | GRIT | QUICK | CUNNING | FIGHTIN\u2019 | MOVE | HAWKEYE | Attacks |\n"
                "| --- | --- | --- | --- | --- | --- | --- | --- |\n"
                "| Guard Dog Scarlet | 4 | 3 | 2 | 3 | 2 | 1 | Bite: Damage 2, Crit 2 (+1 to FIGHTIN\u2019 when Grappling) |\n"
                "| Tracker Dog Rebel | 2 | 4 | 3 | 0 | 2 | 3 | Bite: Damage 1, Crit 2 |"
            )
            content = content[:idx] + new_dogs + content[idx+block_end:]
            changes += 1
            print("  FIXED: Floyd Higgins dog stat table")
            break

    if changes:
        write_file(path, content)
    return changes

###############################################################################
# FIX REMAINING GARBLED SKILLS IN ALL FILES
###############################################################################
def fix_garbled_skills_all():
    """Fix remaining garbled skill lines (wide-spaced) across all chapters."""
    print("\n=== GARBLED SKILL CLEANUP (all files) ===")
    total = 0
    for fname in os.listdir(BASE):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(BASE, fname)
        content = read_file(path)
        original = content

        # Find lines with wide-spaced skills (2+ spaces between skill entries)
        skill_line_re = re.compile(
            rf"^((?:PERFORMIN{AP}|SHOOTIN{AP}|FIGHTIN{AP}|DOCTORIN{AP}|RESILIENCE|PRESENCE|"
            rf"HAWKEYE|INSIGHT|NATURE|OPERATE|MAKIN{AP}|LABOR|MOVE|ANIMAL HANDLIN{AP}|"
            rf"BOOK LEARNIN{AP}|BOOKLEARNIN{AP}|LIGHT-FINGERED)"
            rf"\s{{2,}}\d.+)$",
            re.MULTILINE
        )

        for sm in skill_line_re.finditer(content):
            old_line = sm.group(0)
            new_line = fix_garbled_skill_line(old_line)
            if new_line != old_line:
                content = content.replace(old_line, new_line, 1)
                total += 1

        if content != original:
            write_file(path, content)
            print(f"  {fname}: Fixed garbled skill lines")

    return total

###############################################################################
# MAIN
###############################################################################
def main():
    total = 0
    total += fix_ch09()
    total += fix_ch10()
    total += fix_garbled_skills_all()
    print(f"\n{'='*60}")
    print(f"TOTAL PASS 2 FIXES: {total}")

if __name__ == '__main__':
    main()
