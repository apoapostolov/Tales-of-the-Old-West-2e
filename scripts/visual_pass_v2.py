#!/usr/bin/env python3
"""Visual pass v2: find meaningful content gaps between PDF and markdown.

Strategy: extract 'key sentences' from each PDF page (8+ word sequences
that form complete thoughts), then check if they appear in the chapter markdown.
Reports only genuine content that appears to be missing or significantly altered.
"""
import re
import fitz
from pathlib import Path
from collections import defaultdict

PDF_PATH = Path("C:/git/lifestyle/rpg_projects/houserules/tales-of-the-old-west/Tales_of_the_Old_West_Core_Rules.pdf")
COREBOOK = Path(__file__).parent.parent / "corebook"

CHAPTERS = [
    ("01-welcome-to-the-old-west.md",   8,  13),
    ("02-your-player-character.md",     14,  35),
    ("03-rolling-the-bones.md",         36,  51),
    ("04-talents.md",                   52,  63),
    ("05-conflict-and-damage.md",       64,  85),
    ("06-life-in-the-old-west.md",      86, 141),
    ("07-the-west-in-the-1870s.md",    142, 159),
    ("08-campaigns-in-the-old-west.md",160, 209),
    ("09-the-new-mexico-campaign.md",  210, 251),
    ("10-patience-is-a-virtue.md",     252, 271),
]


def normalize(text):
    """Aggressive normalization for fuzzy matching."""
    text = text.lower()
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201C", '"').replace("\u201D", '"')
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def get_key_fragments(text, window=8):
    """Generate overlapping word-window fragments for matching."""
    words = normalize(text).split()
    fragments = set()
    for i in range(len(words) - window + 1):
        frag = ' '.join(words[i:i + window])
        fragments.add(frag)
    return fragments


def extract_sentences(pdf_text):
    """Extract sentence-like segments from PDF page text."""
    # Join lines that don't end with sentence terminators
    text = pdf_text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    # Split on sentence boundaries
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # Filter: keep sentences with 6+ words
    return [s.strip() for s in sentences if len(s.split()) >= 6]


def main():
    doc = fitz.open(str(PDF_PATH))

    issues_by_chapter = defaultdict(list)
    total_pages = 0
    total_issues = 0

    for md_file, start_page, end_page in CHAPTERS:
        md_path = COREBOOK / md_file
        if not md_path.exists():
            print(f"MISSING: {md_file}")
            continue

        md_text = md_path.read_text(encoding="utf-8")
        # Build fragment index from the markdown (8-word windows)
        md_frags = get_key_fragments(md_text, window=8)
        md_norm = normalize(md_text)

        for page_num in range(start_page, end_page + 1):
            page = doc[page_num - 1]
            pdf_text = page.get_text("text")
            total_pages += 1

            if not pdf_text.strip():
                continue

            sentences = extract_sentences(pdf_text)

            for sent in sentences:
                sent_norm = normalize(sent)
                words = sent_norm.split()
                if len(words) < 6:
                    continue

                # Check: does any 8-word window from this sentence appear in MD?
                found = False
                for i in range(len(words) - 7):
                    frag = ' '.join(words[i:i + 8])
                    if frag in md_frags:
                        found = True
                        break

                # Fallback: check shorter window (5 words) in normalized MD
                if not found:
                    for i in range(len(words) - 4):
                        frag = ' '.join(words[i:i + 5])
                        if frag in md_norm:
                            found = True
                            break

                if not found:
                    # Skip common PDF artifacts
                    if any(x in sent_norm for x in [
                        'tales of the old west',
                        'effekt publishing',
                        'free league',
                    ]):
                        continue
                    issues_by_chapter[md_file].append((page_num, sent[:120]))
                    total_issues += 1

    # Print report
    print(f"{'='*70}")
    print(f"VISUAL PASS COMPARISON REPORT")
    print(f"Pages checked: {total_pages}")
    print(f"Missing content fragments: {total_issues}")
    print(f"{'='*70}")
    print()

    for md_file, start_page, end_page in CHAPTERS:
        issues = issues_by_chapter.get(md_file, [])
        if not issues:
            print(f"✓ {md_file} (pages {start_page}-{end_page}): CLEAN")
        else:
            print(f"✗ {md_file} (pages {start_page}-{end_page}): {len(issues)} issues")
            by_page = defaultdict(list)
            for pnum, text in issues:
                by_page[pnum].append(text)
            for pnum in sorted(by_page):
                print(f"  Page {pnum}:")
                for t in by_page[pnum]:
                    print(f"    - {t}")
            print()


if __name__ == "__main__":
    main()
