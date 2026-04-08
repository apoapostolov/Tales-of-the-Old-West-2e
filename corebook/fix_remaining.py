#!/usr/bin/env python3
"""Fix all remaining formatting issues across corebook chapters."""
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
total_fixes = 0

def fix_file(filename, fixes_description, fix_func):
    """Apply a fix function to a file and report results."""
    global total_fixes
    with open(filename, 'r', encoding='utf-8') as f:
        original = f.read()
    result, count = fix_func(original)
    if result != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(result)
        total_fixes += count
        print(f"  [{filename}] {count} fix(es): {fixes_description}")
    else:
        print(f"  [{filename}] No changes needed for: {fixes_description}")

# ============================================================
# Chapter 03 - teach- word split in Presence description
# ============================================================
def fix_ch03(data):
    count = 0
    old = "add weight to your teach-\n\n**Failure**"
    new = "add weight to your teachings, you make a PRESENCE roll.\n\n**Failure**"
    if old in data:
        data = data.replace(old, new)
        count += 1
    return data, count

fix_file('03-rolling-the-bones.md', 'teach- word split in Presence', fix_ch03)

# ============================================================
# Chapter 05 - Multiple fixes
# ============================================================
def fix_ch05(data):
    count = 0

    # Fix 1: Remove orphaned paragraph fragment between Falling and Falling from your Horse
    old_orphan = """### Falling

Falling on a hard surface automatically inflicts an amount of damage equal to the height of the fall (in meters) divided by 2, rounding all fractions down. In a controlled jump, roll MOVE\u2014each success reduces the damage by one. Depending on the circumstances the GM may call for a critical injury as a result of the fall.

ability. To resist the poison you need to get as many successes as the Potency rating of the poison. If you fail the roll you suffer the full effect. If you succeed, you only suffer the limited effect of the poison.

### Falling from your Horse"""

    new_orphan = """### Falling

Falling on a hard surface automatically inflicts an amount of damage equal to the height of the fall (in meters) divided by 2, rounding all fractions down. In a controlled jump, roll MOVE\u2014each success reduces the damage by one. Depending on the circumstances the GM may call for a critical injury as a result of the fall.

### Falling from your Horse"""

    if old_orphan in data:
        data = data.replace(old_orphan, new_orphan)
        count += 1

    # Fix 2: Rejoin the split text and add Lethal Poison heading
    old_potency = "you must roll your RESILIENCE L e t h a l po i so n"
    new_potency = """you must roll your RESILIENCE ability. To resist the poison you need to get as many successes as the Potency rating of the poison. If you fail the roll you suffer the full effect. If you succeed, you only suffer the limited effect of the poison.

### Lethal Poison"""
    if old_potency in data:
        data = data.replace(old_potency, new_potency)
        count += 1

    # Fix 3: ### Limited Effect** : → **Limited Effect** :
    old_limited = "### Limited Effect** : You take 1 point of Vexes."
    new_limited = "**Limited Effect** : You take 1 point of Vexes."
    if old_limited in data:
        data = data.replace(old_limited, new_limited)
        count += 1

    return data, count

fix_file('05-conflict-and-damage.md', 'orphan text + Lethal Poison heading + Limited Effect', fix_ch05)

# ============================================================
# Chapter 06 - L oc at ion garbled heading + paragraph split
# ============================================================
def fix_ch06(data):
    count = 0

    old_loc = "L oc at ion The location of your property"
    new_loc = "### Location\n\nThe location of your property"
    if old_loc in data:
        data = data.replace(old_loc, new_loc)
        count += 1

    old_split = "selling your\n\nwares to passers-by"
    new_split = "selling your wares to passers-by"
    if old_split in data:
        data = data.replace(old_split, new_split)
        count += 1

    return data, count

fix_file('06-life-in-the-old-west.md', 'garbled Location heading + paragraph split', fix_ch06)

# ============================================================
# Chapter 08 - Originals in orphan heading + Carmody fix
# ============================================================
def fix_ch08(data):
    count = 0

    # Remove orphaned "### Originals in" heading
    old_originals = "\n### Originals in\n\n### Background"
    new_originals = "\n### Background"
    if old_originals in data:
        data = data.replace(old_originals, new_originals)
        count += 1

    # Fix Carmody name
    old_carmody = "### Father Car Mody Goes to Work"
    new_carmody = "### Father Carmody Goes to Work"
    if old_carmody in data:
        data = data.replace(old_carmody, new_carmody)
        count += 1

    return data, count

fix_file('08-campaigns-in-the-old-west.md', 'orphan heading + Carmody name', fix_ch08)

# ============================================================
# Chapter 09 - Garbled names + orphaned text
# ============================================================
def fix_ch09(data):
    count = 0

    # Fix Erikaga heading
    old = "### Erika Ga\n\nA young Native American brave"
    new = "### Erikaga\n\nA young Native American brave"
    if old in data:
        data = data.replace(old, new)
        count += 1

    # Fix Carmody heading
    old = "### Father Brayton Car Mody"
    new = "### Father Brayton Carmody"
    if old in data:
        data = data.replace(old, new)
        count += 1

    # Fix Castellanos heading
    old = "### Francisco Castellano S\n"
    new = "### Francisco Castellanos\n"
    if old in data:
        data = data.replace(old, new)
        count += 1

    # Remove garbled "V e da  m on r oe" running header
    # It appears at the start of the Obedience Whitley paragraph
    old = "V e da  m on r oe Obedience was once enslaved"
    new = "Obedience was once enslaved"
    if old in data:
        data = data.replace(old, new)
        count += 1

    return data, count

fix_file('09-the-new-mexico-campaign.md', 'Erikaga + Carmody + Castellanos + Veda Monroe', fix_ch09)

# ============================================================
# Chapter 10 - Running headers, production note, embedded headers
# ============================================================
def fix_ch10(data):
    count = 0

    # Fix 1: Remove production note
    old = '**Need a Chapter spread here??? Will blend into Chapter 10 otherwise...**\n\n'
    if old in data:
        data = data.replace(old, '')
        count += 1

    # Fix 2: Remove standalone "Appendix: your tale begins" running headers
    # (but NOT the actual ### Appendix: Your Tale Begins heading)
    lines = data.split('\n')
    new_lines = []
    removed = 0
    for i, line in enumerate(lines):
        if line.strip() == 'Appendix: your tale begins':
            removed += 1
        else:
            new_lines.append(line)
    if removed > 0:
        data = '\n'.join(new_lines)
        count += removed

    # Fix 3: Remove embedded running header in paragraph
    old = 'attribute point of Appendix: your tale begins your choice'
    new = 'attribute point of your choice'
    if old in data:  # Check before replace since we already modified data
        data = data.replace(old, new)
        count += 1

    # Fix 4: Remove broken heading "### pire, the Middle East and North Africa The Ottoman Em"
    old = '### pire, the Middle East and North Africa The Ottoman Em\n'
    if old in data:
        data = data.replace(old, '')
        count += 1

    # Fix 5: Clean up consecutive blank lines that result from removals
    while '\n\n\n' in data:
        data = data.replace('\n\n\n', '\n\n')

    return data, count

fix_file('10-patience-is-a-virtue.md', 'running headers + production note + embedded headers', fix_ch10)

print(f"\nTotal fixes applied: {total_fixes}")
