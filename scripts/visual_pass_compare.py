#!/usr/bin/env python3
"""Visual pass comparison: extract PDF page text and compare against markdown chapters.

Produces a discrepancy report highlighting content in the PDF that doesn't
appear in the markdown, enabling targeted visual verification.
"""
import re
import fitz
from pathlib import Path

PDF_PATH = Path("C:/git/lifestyle/rpg_projects/houserules/tales-of-the-old-west/Tales_of_the_Old_West_Core_Rules.pdf")
COREBOOK = Path(__file__).parent.parent / "corebook"
OUTDIR = Path(__file__).parent.parent / "_visual_pass"

# Chapter page ranges (1-indexed, inclusive) from PDF TOC
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
    """Normalize text for comparison: lowercase, collapse whitespace, strip punctuation variants."""
    text = text.lower()
    # Normalize quotes
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    text = text.replace("\u201C", '"').replace("\u201D", '"')
    # Normalize dashes
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def extract_phrases(text, min_words=4):
    """Extract meaningful phrases (4+ words) from text for matching."""
    # Split into sentences/clauses
    text = normalize(text)
    # Remove markdown formatting
    text = re.sub(r'[#*_|>`\[\]]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    # Generate overlapping word windows
    words = text.split()
    phrases = set()
    for i in range(len(words) - min_words + 1):
        phrase = ' '.join(words[i:i + min_words])
        if len(phrase) > 15:  # skip very short phrases
            phrases.add(phrase)
    return phrases


def main():
    doc = fitz.open(str(PDF_PATH))
    report_lines = []
    report_lines.append("# Visual Pass Comparison Report")
    report_lines.append("")
    report_lines.append(f"PDF: {PDF_PATH.name} ({len(doc)} pages)")
    report_lines.append("")

    total_missing = 0
    total_pages_checked = 0

    for md_file, start_page, end_page in CHAPTERS:
        md_path = COREBOOK / md_file
        if not md_path.exists():
            report_lines.append(f"## {md_file} — FILE NOT FOUND")
            continue

        md_text = md_path.read_text(encoding="utf-8")
        md_normalized = normalize(md_text)
        md_phrases = extract_phrases(md_text, min_words=5)

        report_lines.append(f"## {md_file} (pages {start_page}-{end_page})")
        report_lines.append("")

        chapter_missing = 0

        for page_num in range(start_page, end_page + 1):
            page = doc[page_num - 1]  # 0-indexed
            pdf_text = page.get_text("text")
            total_pages_checked += 1

            if not pdf_text.strip():
                report_lines.append(f"- **Page {page_num}**: *empty/image-only*")
                continue

            # Extract meaningful phrases from PDF page
            pdf_phrases = extract_phrases(pdf_text, min_words=5)

            # Find phrases in PDF that don't appear in MD
            missing = []
            for phrase in sorted(pdf_phrases):
                if phrase not in md_phrases:
                    # Double check with simple substring
                    if phrase not in md_normalized:
                        missing.append(phrase)

            if missing:
                # Filter out common false positives (page numbers, headers, footers)
                filtered = []
                for m in missing:
                    # Skip if it's just numbers or very short
                    if re.match(r'^[\d\s.,-]+$', m):
                        continue
                    # Skip common PDF artifacts
                    if any(x in m for x in ['tales of the old west', 'page ', 'chapter ']):
                        continue
                    filtered.append(m)

                if filtered:
                    chapter_missing += len(filtered)
                    report_lines.append(f"### Page {page_num} — {len(filtered)} unmatched phrases")
                    for m in filtered[:10]:  # Cap at 10 per page
                        report_lines.append(f"  - `{m}`")
                    if len(filtered) > 10:
                        report_lines.append(f"  - *... and {len(filtered) - 10} more*")
                    report_lines.append("")
                else:
                    report_lines.append(f"- Page {page_num}: OK")
            else:
                report_lines.append(f"- Page {page_num}: OK")

        total_missing += chapter_missing
        if chapter_missing == 0:
            report_lines.append("- **All pages matched** ✓")
        else:
            report_lines.append(f"- **{chapter_missing} unmatched phrases across chapter**")
        report_lines.append("")

    report_lines.append("---")
    report_lines.append(f"**Total pages checked: {total_pages_checked}**")
    report_lines.append(f"**Total unmatched phrases: {total_missing}**")

    report_path = OUTDIR / "comparison_report.md"
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Report written to {report_path}")
    print(f"Pages checked: {total_pages_checked}, Unmatched phrases: {total_missing}")


if __name__ == "__main__":
    main()
