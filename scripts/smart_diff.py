#!/usr/bin/env python3
"""Smart diff: find genuine content gaps between PDF and markdown.

Extracts complete sentences from PDF pages, normalizes aggressively to remove
hyphenation/spacing artifacts, and checks if the content exists in markdown.
Reports only genuinely missing or significantly altered content.
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
    """Aggressive normalization: lowercase, fix hyphenation, collapse spaces, strip most punctuation."""
    text = text.lower()
    # Normalize unicode quotes/dashes
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    # Fix PDF hyphenation: "strug- gle" -> "struggle"
    text = re.sub(r'(\w)-\s+(\w)', r'\1\2', text)
    # Remove all non-alphanumeric except spaces
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_sentences(page_text):
    """Extract meaningful sentences from PDF page text."""
    # Join lines, fixing hyphenation
    text = page_text.replace('-\n', '')
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text).strip()

    # Split on sentence boundaries
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

    # Filter: keep sentences with 8+ words that look like real content
    results = []
    for s in sentences:
        s = s.strip()
        words = s.split()
        if len(words) >= 8:
            # Skip if it looks like a table row (lots of numbers/short words)
            alpha_words = [w for w in words if len(w) > 2]
            if len(alpha_words) >= 4:
                results.append(s)
    return results


def check_sentence_in_markdown(sentence, md_norm, threshold=0.7):
    """Check if a sentence appears in the markdown using word overlap."""
    sent_norm = normalize(sentence)
    sent_words = sent_norm.split()

    if len(sent_words) < 5:
        return True  # skip very short

    # First try: exact substring match
    if sent_norm in md_norm:
        return True

    # Second try: check if a large contiguous chunk (6+ words) matches
    for window in range(min(len(sent_words), 10), 5, -1):
        for i in range(len(sent_words) - window + 1):
            chunk = ' '.join(sent_words[i:i+window])
            if chunk in md_norm:
                return True

    return False


def is_header_or_noise(text):
    """Detect spaced-out headers and other PDF formatting noise."""
    # Spaced headers like "C O N T E N T S"
    if re.search(r'[A-Z]\s[A-Z]\s[A-Z]', text):
        return True
    # Page numbers like "-10-"
    if re.match(r'^[-–]\s*\d+\s*[-–]$', text.strip()):
        return True
    # Chapter headers repeated
    if re.match(r'^chapter\s+\d+', text.strip().lower()):
        return True
    return False


def main():
    doc = fitz.open(str(PDF_PATH))

    print("# Smart Content Diff Report")
    print(f"PDF: {PDF_PATH.name}")
    print()

    total_missing = 0

    for md_file, start_page, end_page in CHAPTERS:
        md_path = COREBOOK / md_file
        if not md_path.exists():
            print(f"## {md_file} — FILE NOT FOUND\n")
            continue

        md_text = md_path.read_text(encoding="utf-8")
        md_norm = normalize(md_text)

        chapter_missing = []

        for page_num in range(start_page, end_page + 1):
            page = doc[page_num - 1]  # 0-indexed
            page_text = page.get_text()

            if not page_text.strip():
                continue

            sentences = extract_sentences(page_text)
            page_missing = []

            for sent in sentences:
                if is_header_or_noise(sent):
                    continue
                if not check_sentence_in_markdown(sent, md_norm):
                    page_missing.append(sent)

            if page_missing:
                chapter_missing.append((page_num, page_missing))

        if chapter_missing:
            print(f"## {md_file}")
            for page_num, sentences in chapter_missing:
                print(f"\n### Page {page_num}")
                for s in sentences:
                    # Truncate very long sentences
                    display = s[:200] + "..." if len(s) > 200 else s
                    print(f"  - {display}")
                total_missing += len(sentences)
            print()
        else:
            print(f"## {md_file} — OK\n")

    print(f"---\nTotal potentially missing sentences: {total_missing}")
    doc.close()


if __name__ == "__main__":
    main()
