"""
Rename all vignette headings (strip '## Vignette — ' prefix) and move each
vignette from its current end-of-chapter position to a specified mid-chapter
position between content sections.

Run from the repo root: python scripts/move_vignettes.py
"""
from __future__ import annotations

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent / "1870s-the-old-west"

# For each file: list of (vignette_title_fragment, target_section_fragment)
# The vignette is inserted AFTER the section whose heading contains target_section_fragment.
# All vignette headings are renamed regardless (strips '## Vignette — ' prefix).
MOVES: dict[str, list[tuple[str, str]]] = {
    "01-peoples-and-conflict.md": [
        ("Two Voices in a Saloon", "4. The Chinese"),
    ],
    "02-native-cultures.md": [
        ("A Comanche Scout in His Mother Tongue", "1. Southern Plains — the Comanche"),
    ],
    "03-borderlands.md": [
        # Trail Down to River → after §3 Cattle and Horse Trade (early);
        # Casco at Vespers naturally follows §11 Hacienda, stays near end
        ("The Trail Down to the River", "3. The Cattle and Horse Trade"),
    ],
    "04-childhood.md": [
        ("Caleb at the Woodpile", "6. Toys, Games, Songs"),
    ],
    "05-women.md": [
        ("Eliza on Wash Day",          "1. The Homestead Woman"),
        ("Mrs. Whittaker in the Parlor", "3. The Town Woman"),
        ("Eliza and the Letter",       "7. Black Women in the West"),
    ],
    "06-food-and-drink.md": [
        ("The Trail Breakfast",      "1. The Trail Cook — the Wagon and the Herd"),
        ("Biscuit at Three O'Clock", "4. The Chinese Cookhouse"),
    ],
    "07-work-and-trades.md": [
        ("Branding at the Spring Roundup", "1. Ranching"),
        ("The Dude at the Chuckwagon",     "6. Tracking"),
    ],
    "08-material-culture.md": [
        ("At the Mercantile", "4. Clothing — by Class and Region"),
    ],
    "09-language-and-print.md": [
        ("A Letter Home",           "12. Letters and Correspondence"),
        ("The Forged Bill of Sale", "14. Legal Documents"),
    ],
    "10-religion-and-faith.md": [
        ("The Funeral", "5. The Mormon Settlement"),
    ],
    "11-frontier-survival-and-hunt.md": [
        ("The Blue Norther",         "2. Weather"),
        ("The Stand at First Light", "10. The Market Hunter"),
    ],
    "12-availability.md": [
        ("The Wrong Decade", "5. Communication — What Reaches Whom and How Fast"),
    ],
    "13-prices-and-anchors.md": [
        ("Settling Up",         "2. Drinks, Food, Lodging — The Saloon and Mercantile"),
        ("The Widow's Account", "7. Distance and Time — How Far and How Long"),
    ],
    "14-towns-economy-law.md": [
        ("Saturday Night in Front Street", "4. Law on the Frontier — Who Did What"),
    ],
    "15-competence-and-procedures.md": [
        ("Saddling at First Light", "2. Horsemanship Procedures"),
        ("Caught in the Open",      "5. Survival"),
    ],
    "16-cowboy-life.md": [
        ("Four Days on the Cimarron", "3. The Cattle Drive"),
        ("Six Weeks to Newton",       "8. Hierarchy"),
    ],
    "17-horse-culture.md": [
        # target uses the section number to distinguish from the renamed vignette
        ("The Horse Trade", "6. The Horse Trade"),
    ],
    "18-mining-camps.md": [
        ("Shift Change at Three", "4. The Hierarchy"),
    ],
    "19-army-life.md": [
        ("First Call", "2. The Daily Routine"),
    ],
    "20-outlaw-craft.md": [
        ("The Killing at the Card Table", "4. The Bank Robbery"),
    ],
    "21-gambling.md": [
        ("Faro at Midnight", "2. Faro — Procedure"),
    ],
    "22-music-and-entertainment.md": [
        ("Second Watch", "3. The Saloon and the Dance Hall"),
    ],
    "23-medicine-and-death.md": [
        ("Two Holes",                 "2. Gunshot Wounds"),
        ("The Doctor in the Sickroom", "6. Medicines, Period-Correct"),
    ],
    "24-dark-frontier.md": [
        ("The Cold Stove", "7. Domestic Violence and the Family Killing"),
    ],
    "25-regional-landscapes.md": [
        ("East of the Pecos", "3. The Texas Hill Country and South Texas"),
    ],
}


def split_sections(text: str) -> tuple[str, list[str]]:
    """Return (front_matter, list_of_section_strings).
    Each section string begins with '## ' and runs up to (not including)
    the next '## ' heading.
    """
    m = re.search(r"^## ", text, re.MULTILINE)
    if not m:
        return text, []
    front = text[: m.start()]
    rest = text[m.start() :]
    parts = re.split(r"(?=^## )", rest, flags=re.MULTILINE)
    return front, [p for p in parts if p]


def heading_of(section: str) -> str:
    return section.split("\n")[0]


def is_vignette_heading(heading: str) -> bool:
    return heading.startswith("## Vignette — ")


def rename_vignette(section: str) -> str:
    h = heading_of(section)
    if is_vignette_heading(h):
        new_h = h.replace("## Vignette — ", "## ", 1)
        return new_h + section[len(h) :]
    return section


def normalize_separator(section: str, is_last: bool) -> str:
    """Ensure non-last sections end with '---' + blank lines; last section ends cleanly."""
    stripped = section.rstrip("\n")
    if is_last:
        # Remove trailing --- if present
        stripped = re.sub(r"\n+---\s*$", "", stripped)
        return stripped + "\n"
    else:
        if not stripped.endswith("---"):
            stripped += "\n\n---"
        return stripped + "\n\n"


def process_file(filepath: pathlib.Path, moves: list[tuple[str, str]]) -> None:
    text = filepath.read_text(encoding="utf-8")
    front, sections = split_sections(text)
    if not sections:
        return

    # Step 1: record which indices were originally vignettes (before rename)
    orig_vignette_titles: dict[int, str] = {}
    for i, s in enumerate(sections):
        h = heading_of(s)
        if is_vignette_heading(h):
            orig_vignette_titles[i] = h[len("## Vignette — "):]

    # Step 2: rename all vignette headings
    sections = [rename_vignette(s) for s in sections]

    # Step 3: execute moves
    for title_frag, target_frag in moves:
        # Find the vignette section (match by exact renamed heading or partial)
        vig_idx: int | None = None
        for i, s in enumerate(sections):
            h = heading_of(s)
            # Must be originally a vignette
            if i in orig_vignette_titles and title_frag in orig_vignette_titles[i]:
                vig_idx = i
                break
        # Fallback: search by current heading
        if vig_idx is None:
            for i, s in enumerate(sections):
                h = heading_of(s)
                if h == f"## {title_frag}":
                    vig_idx = i
                    break

        if vig_idx is None:
            print(f"  WARNING: vignette not found: '{title_frag}' in {filepath.name}")
            continue

        # Find the target section (must not be the vignette itself)
        target_idx: int | None = None
        for i, s in enumerate(sections):
            if i == vig_idx:
                continue
            h = heading_of(s)
            if target_frag in h:
                target_idx = i
                break

        if target_idx is None:
            print(f"  WARNING: target section not found: '{target_frag}' in {filepath.name}")
            continue

        # Extract and reinsert
        vig = sections.pop(vig_idx)
        # Adjust target index if vignette was before it
        if target_idx > vig_idx:
            target_idx -= 1
        sections.insert(target_idx + 1, vig)

        # Update orig_vignette_titles indices to reflect the move
        new_orig: dict[int, str] = {}
        for old_i, title in orig_vignette_titles.items():
            if old_i == vig_idx:
                new_i = target_idx + 1
            elif vig_idx < old_i <= (target_idx + (1 if target_idx >= vig_idx else 0)):
                new_i = old_i - 1
            elif (target_idx + 1) <= old_i < vig_idx:
                new_i = old_i + 1
            else:
                new_i = old_i
            new_orig[new_i] = title
        orig_vignette_titles = new_orig

    # Step 4: normalize separators
    result_parts: list[str] = []
    for i, s in enumerate(sections):
        result_parts.append(normalize_separator(s, i == len(sections) - 1))

    result = front + "".join(result_parts)
    if result != text:
        filepath.write_text(result, encoding="utf-8")
        print(f"  updated: {filepath.name}")
    else:
        print(f"  unchanged: {filepath.name}")


def main() -> None:
    files = sorted(ROOT.glob("*.md"))
    changed = 0
    for f in files:
        moves = MOVES.get(f.name, [])
        old = f.read_text(encoding="utf-8")
        process_file(f, moves)
        if f.read_text(encoding="utf-8") != old:
            changed += 1
    print(f"\n{changed} file(s) changed.")


if __name__ == "__main__":
    main()
