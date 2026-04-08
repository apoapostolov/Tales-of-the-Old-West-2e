#!/usr/bin/env python3
"""Pass 2 fixes: garbled text, paragraph splits, orphan artifacts."""
import re
from pathlib import Path

COREBOOK = Path(__file__).parent.parent / "corebook"
total_fixes = 0


def fix_file(filename, description, fix_func):
    global total_fixes
    path = COREBOOK / filename
    original = path.read_text(encoding="utf-8")
    result, count = fix_func(original)
    if result != original:
        path.write_text(result, encoding="utf-8")
        total_fixes += count
        print(f"  [{filename}] {count} fix(es): {description}")
    else:
        print(f"  [{filename}] OK: {description}")


# ============================================================
# Garbled spaced-character text reconstruction
# ============================================================
# These are standalone lines or bold text where PDF decorative
# fonts caused spaced characters in the extraction.

GARBLED_EXACT = {
    # ch04 - talent names (should be ### headings)
    "De a dly  s t r ik e You know where to hit a man":
        "### Deadly Strike\n\nYou know where to hit a man",
    "Ha r d t o h i t You\u2019re a tough opponent":
        "### Hard to Hit\n\nYou\u2019re a tough opponent",
    "Q u i c k  dr aw You draw your weapon faster":
        "### Quick Draw\n\nYou draw your weapon faster",
    # ch05 - inline section header
    "Fi r e a r m s  &  a m m u n it i on In":
        "### Firearms & Ammunition\n\nIn",
    # ch06 - bold section headers
    "**Ri f les , s h o t gu n s a n d  bo w s**":
        "### Rifles, Shotguns and Bows",
    "**wea p on qu a l i t i e s -  r a n ge d**":
        "### Weapon Qualities - Ranged",
    "**W ea p on qu a l i t i e s -  m e l e e**":
        "### Weapon Qualities - Melee",
    # ch06 - standalone garbled names (sidebar artifacts after description)
    "\nA ppa l o o sa\n":
        "\n",
    "\nAm er ic a n s a d d l e b r e d\n":
        "\n",
    # ch06 - inline garbled text
    "W e lls Fa rgo  C o ach gun":
        "**Wells Fargo Coachgun**",
    "C h oos e  y ou r  t ac t i c":
        "### Choose Your Tactic",
    # ch03 - trouble table headers
    "**T roub le  o u t c o m e  t a bl e  -  c on fl ic t / ph ysic a l**":
        "**Trouble Outcome Table - Conflict / Physical**",
    "**Troub le  o u t c o m e  t a bl e  -  m e n t a l / soc ia l**":
        "**Trouble Outcome Table - Mental / Social**",
    # ch03 - garbled table sub-header
    "Nu m be r  o f  ac t i v e  t r oubl e  d ic e D6":
        "Number of active trouble dice D6",
    # ch09 - NPC name artifacts (sidebar names after descriptions)
    "\nLya n n e  vi gle\n":
        "\n",
    "\nE m e r s on  m u r r ay\n":
        "\n",
    "\nE dw a rd  \u2018e d d i e \u2019 t yle r\n":
        "\n",
    "\nA n d re w  ro be rt  mi lle r\n":
        "\n",
    # ch10 - NPC name artifact
    "\nEl l i s r oc k c l if f e\n":
        "\n",
    # ch10 - running header/index
    "\nTales of the old west - index\n":
        "\n",
}

# ch10 - "torn cloth-" at end of paragraph (word split before a list)
TORN_CLOTH_OLD = "in torn cloth-"
TORN_CLOTH_NEW = "in torn clothing."

# ch08 - garbled amenities table header (825-char collapsed line)
# Replace the whole garbled line with two section headings + note
AMENITIES_GARBLED_START = "A M EN IT I E S  -  FA R MI N G AM E N ITIE S  -  M E R C AN T ILE"

# ch05 - garbled barrier table line with "Bo w s" merged
BARRIER_GARBLED = "Adobe WallBo w s &  sli n gsh o t s 8"
BARRIER_FIX = "Adobe Wall 8\n\n### Bows & Slingshots"

# ch10 - fully garbled sentence
CH10_GARBLED_SENTENCE = "I f th e  pl ay e r  c h a r ac t e rs leav e  pat ie n c e  w it h  pe y t on a n d  u ph ol d r oc k c l i f f e \u2019 s li e"
CH10_SENTENCE_FIX = "### If the Player Characters Leave Patience with Peyton and Uphold Rockcliffe\u2019s Lie"

# Targeted paragraph joins that the general logic can't catch
# (lines ending with closing quotes mid-sentence)
TARGETED_JOINS = [
    ('Called \u201Chot horses\u201D\n\nbecause they love to run',
     'Called \u201Chot horses\u201D because they love to run'),
]


def fix_garbled_text(data):
    count = 0
    for old, new in GARBLED_EXACT.items():
        if old in data:
            data = data.replace(old, new)
            count += 1
    if BARRIER_GARBLED in data:
        data = data.replace(BARRIER_GARBLED, BARRIER_FIX)
        count += 1
    if CH10_GARBLED_SENTENCE in data:
        data = data.replace(CH10_GARBLED_SENTENCE, CH10_SENTENCE_FIX)
        count += 1
    for old, new in TARGETED_JOINS:
        if old in data:
            data = data.replace(old, new)
            count += 1
    if TORN_CLOTH_OLD in data:
        data = data.replace(TORN_CLOTH_OLD, TORN_CLOTH_NEW)
        count += 1
    if AMENITIES_GARBLED_START in data:
        # Replace the entire garbled line with structured headings
        lines = data.split("\n")
        new_lines = []
        for line in lines:
            if AMENITIES_GARBLED_START in line:
                new_lines.append("### Amenities - Farming")
                new_lines.append("")
                new_lines.append("### Amenities - Mercantile")
                new_lines.append("")
                new_lines.append("*(See rulebook table for full amenity data with Rank, Min Tally, and Aspect modifiers.)*")
                count += 1
            else:
                new_lines.append(line)
        data = "\n".join(new_lines)
    return data, count


# ============================================================
# Paragraph join: lowercase continuation after blank line
# ============================================================
def fix_paragraph_splits(data):
    """Join paragraphs split across blank lines where continuation
    starts with lowercase."""
    lines = data.split("\n")
    result = []
    count = 0
    i = 0
    while i < len(lines):
        if (
            i + 2 < len(lines)
            and lines[i].strip() != ""
            and not lines[i].strip().startswith("#")
            and not lines[i].strip().startswith("|")
            and not lines[i].strip().startswith(">")
            and not re.match(r'^\*[^*]', lines[i].strip())  # skip list items (* x) but not bold (**x)
            # Strip trailing markdown emphasis markers before checking punctuation
            and not re.search(r'[.!?:;"\u201D\u2019)\]`][\s_*]*$', lines[i].strip())
            and lines[i + 1].strip() == ""
            and lines[i + 2].strip() != ""
            and re.match(r'^[a-z]', lines[i + 2].strip())
            and not lines[i + 2].strip().startswith("|")
            and not lines[i + 2].strip().startswith("-")
        ):
            # Join: keep current line, skip blank, append next line
            result.append(lines[i].rstrip() + " " + lines[i + 2].strip())
            count += 1
            i += 3
        else:
            result.append(lines[i])
            i += 1
    return "\n".join(result), count


# ============================================================
# Hyphen-split words at end of line
# ============================================================
def fix_hyphen_splits(data):
    """Join words split with hyphen at end of line."""
    count = 0
    lines = data.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Check for word-hyphen at end of line (not in headings/tables/lists)
        if (
            i + 1 < len(lines)
            and re.search(r'\w-$', stripped)
            and not stripped.startswith("#")
            and not stripped.startswith("|")
            and not stripped.startswith(">")
            and not stripped.startswith("-")
        ):
            next_line = lines[i + 1].strip()
            # Only join if next line starts with lowercase (word continuation)
            if next_line and re.match(r'^[a-z]', next_line):
                # Remove the trailing hyphen and join
                joined = line.rstrip()[:-1] + next_line
                result.append(joined)
                count += 1
                i += 2
                continue
            # Also handle: hyphen at end, then blank line, then continuation
            elif (
                next_line == ""
                and i + 2 < len(lines)
                and lines[i + 2].strip()
                and re.match(r'^[a-z]', lines[i + 2].strip())
            ):
                # Check if it's a list item following (don't join with list)
                if not lines[i + 2].strip().startswith("-"):
                    joined = line.rstrip()[:-1] + lines[i + 2].strip()
                    result.append(joined)
                    count += 1
                    i += 3
                    continue
        result.append(line)
        i += 1
    return "\n".join(result), count


# ============================================================
# Clean up triple blank lines left by fixes
# ============================================================
def clean_blanks(data):
    count = 0
    while "\n\n\n" in data:
        data = data.replace("\n\n\n", "\n\n")
        count += 1
    return data, count


# ============================================================
# Apply all fixes to each chapter
# ============================================================
for f in sorted(COREBOOK.glob("*.md")):
    fname = f.name
    text = f.read_text(encoding="utf-8")
    original = text
    changes = 0

    # Pass 1: Garbled text
    text, c = fix_garbled_text(text)
    changes += c

    # Pass 2: Paragraph splits
    text, c = fix_paragraph_splits(text)
    changes += c

    # Pass 3: Hyphen splits
    text, c = fix_hyphen_splits(text)
    changes += c

    # Pass 4: Clean blanks
    text, c = clean_blanks(text)
    changes += c

    if text != original:
        f.write_text(text, encoding="utf-8")
        total_fixes += changes
        print(f"{fname}: {changes} total fixes")
    else:
        print(f"{fname}: clean")

print(f"\n=== Total: {total_fixes} fixes applied ===")
