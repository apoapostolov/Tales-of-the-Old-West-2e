---
name: pdf-to-rpg-markdown
description: |
  Use when converting a tabletop RPG PDF into clean, structured markdown for
  `corebook/`, `rpg_projects/`, or similar source-document work. Covers
  layout-aware extraction, multi-pass cleanup, Tales of the Old West-specific
  repair rules, and final normalization.
---

# PDF to RPG Markdown

This skill documents a repeatable pipeline for turning RPG PDFs into
clean markdown that can be versioned, split by chapter, and edited
without losing structure.

The key idea is simple: extract conservatively, clean deterministically,
and only then do any manual repair. RPG books are not plain prose. They
carry running headers, decorative chapter titles, sidebars, tables,
epigraphs, and column breaks that need explicit handling.

## Source Of Truth

Read before you convert or repair:

- The PDF you are converting
- This `SKILL.md`
- The relevant chapter files in `corebook/`
- Any local `AGENTS.md` in the chapter or project folder

For repeatable cleanup work, prefer existing project scripts in `scripts/`
and project references in `references/` or nearby project notes.

## Workflow

1. Locate the source PDF and decide where the markdown should live.
2. Choose the extractor that matches the document:
   - `pymupdf4llm` when layout fidelity matters and you need reading order,
     table preservation, and heading detection.
   - `pdftotext -layout` when the document is mostly text and you want a
     fast first pass.
   - `markitdown` when the file is already fairly clean and the structure is
     not especially tricky.
3. Save a raw draft first. Do not clean in place.
4. Run deterministic cleanup passes before manual edits.
5. Split into chapter files only after the manuscript structure is stable.
6. Record recurring fixes in project notes so the next conversion is cheaper.
7. Validate the final result against the source PDF.

## Extraction

### Preferred Stack

- `pymupdf4llm` for RPG sourcebooks with headings, sidebars, and tables
- `wordninja` for dejoining spaced-out heading text

Install:

```bash
pip install pymupdf4llm wordninja
```

Basic extraction:

```python
from pathlib import Path
import pymupdf4llm

md = pymupdf4llm.to_markdown(str(Path("rulebook.pdf")))
Path("rulebook.raw.md").write_text(md, encoding="utf-8")
```

`pymupdf4llm` is preferred because it is column-aware and usually keeps:

- paragraph flow in reading order
- bold and italic spans
- heading markup
- pipe-table structure
- image placeholders and picture-text blocks

## RPG Book Defaults

- Treat the PDF as a source document, not prose to rewrite.
- Preserve chapter order and section order.
- Keep a raw staged file if the first pass is messy.
- Normalize structure without inventing missing content.
- Use manual repair when page art or table layout has destroyed the reading
  order beyond safe regex cleanup.
- Keep derived markdown beside the PDF or in a clearly named sibling file.
- Reuse project-specific cleanup scripts and notes when the same failure mode
  appears again.

## Cleanup Pipeline

The pipeline is a sequence of independent passes. Order matters because later
passes depend on earlier normalization.

### Pass 1: Front Matter and Noise Removal

Remove non-content elements that extraction often preserves faithfully:

- page numbers such as `–7–`, `– 88 –`, or `# – 14 –`
- copyright lines and distribution notices
- table-of-contents rows with dot leaders
- obvious scan or packaging noise that is not manuscript text

For Tales of the Old West, the front matter usually includes a repeated
copyright/distribution block and a heavily spaced table of contents. Remove
that whole region before trying to clean headings.

### Pass 2: Running Headers

RPG PDFs often repeat the chapter header on every page.

Cleanup rules:

1. Convert the first occurrence of each chapter header into a real `##`
   heading.
2. Remove later occurrences as running headers.
3. Track chapter keys by normalized lowercase text with collapsed whitespace.

For Tales of the Old West, this typically means `Chapter N - Title` should
appear once as the real section heading, not on every page.

### Pass 3: Spaced Heading Reconstruction

Decorative headings often come out with spaces between every letter.

Detection rule:

- treat a heading as spaced if more than 20% of its space-separated tokens
  are single alphabetic characters
- never treat sentence-like text with punctuation as a spaced heading

Reconstruction rule:

1. Split on 2+ spaces to find real word boundaries.
2. Collapse internal spaces within each group.
3. Run `wordninja.split()` on non-trivial collapsed text.
4. Apply smart title casing.
5. Apply a corrections dictionary for known edge cases.

Tales-specific correction examples:

```python
HEADING_CORRECTIONS = {
    "Npcs And Abilities": "NPCs and Abilities",
    "Introduction To Rpgs": "Introduction to RPGs",
    "Don'T Roll Too Often": "Don't Roll Too Often",
    "Npc S And Abilities": "NPCs and Abilities",
    "Non Player Characters": "Non-Player Characters",
    "Non Typical Harm": "Non-Typical Harm",
    "Looking Back": "Looking Back",
    "Looking Forward": "Looking Forward",
    "F Scott Fitzgerald": "F. Scott Fitzgerald",
    "Herbalist": "Herbalist",
    "Bronc Buster": "Bronc Buster",
    "Pistoleer": "Pistoleer",
    "Rabble Rouser": "Rabble Rouser",
    "Fast Actions": "Fast Actions",
    "Conflict Modifications": "Conflict Modifications",
    "Overwatch": "Overwatch",
    "Heatstroke": "Heatstroke",
    "Life in Town": "Life in Town",
    "Salaries in the Old West": "Salaries in the Old West",
}
```

### Pass 4: Picture Block Conversion

Some extractors emit image placeholders and picture-text blocks.

Rules:

- remove placeholder lines that only say the picture was intentionally omitted
- split picture-text blocks on `<br>`
- strip bold markers from the extracted lines
- if the block is a caption, discard it
- if the block is table-like, rebuild it as a pipe table
- otherwise keep it as plain text

### Pass 5: Heading Hierarchy Normalization

`pymupdf4llm` can detect headings but does not know the intended hierarchy.
Normalize it explicitly:

- `## Chapter N - Title` stays `##` and gets title-cased in the title portion
- `## **bold text**` becomes `### bold text`
- `## non-chapter text` becomes `### text`
- `## "quote text"` becomes `> *"quote text"*`
- duplicate chapter headings created by the spaced-heading pass are removed

Attribution rules:

- standalone all-caps bold lines become blockquote attributions
- short name-like `###` headings that follow a blockquote become `> — NAME`

### Pass 6: Sidebar Conversion

Long italic paragraphs often represent sidebar callouts.

- convert long italic-only paragraphs into blockquotes
- keep short captions out of the body when they are clearly picture or sidebar
  labels

### Pass 7: Paragraph Joining

PDF column breaks commonly split sentences across line breaks or blank lines.

Join text when:

- the current line does not end with sentence-terminal punctuation
- the next line begins with lowercase text
- there is a single blank line between two text fragments that obviously
  continue the same sentence

Do not join structural content:

- headings
- blockquotes
- lists
- tables
- code fences

### Pass 8: Inline Table Cleanup

- replace `<br>` inside pipe-table cells with spaces
- preserve the table structure rather than letting wrapped cell text leak
  into prose

### Pass 9: Whitespace Normalization

- strip trailing whitespace
- collapse 3+ consecutive blank lines to 2
- ensure blank lines around headings
- trim leading and trailing blank lines

## Tales Of The Old West Cleanup Rules

The Tales manuscript exposed a recurring set of failure modes. Keep these
rules even when the base pipeline changes.

### 1. Front Matter, Page Numbers, and TOC Noise

Remove repeated page numbers, copyright/distribution lines, and the entire
table of contents block when it appears as extraction noise. The TOC in this
book is especially noisy because decorative spacing and dot leaders get
preserved exactly.

### 2. Broken, Truncated, and Orphaned Headings

Tales PDFs split headings across columns and pages.

- repair partial heading words when the intended title is obvious
- delete orphan fragments that are clearly sentence stubs
- remove garbled merged-heading lines that are really cross-column bleed
- cross-check against the PDF table of contents or nearby chapter headers

Common examples from this book include:

- `He rba li st` -> `Herbalist`
- `Bron C Buster` -> `Bronc Buster`
- `LIF E IN TO WN` -> `Life in Town`
- `SAL AR IE S IN THE O LD WE ST` -> `Salaries in the Old West`
- `Father Brayton Car Mody` -> `Father Brayton Carmody`
- `Francisco Castellano S` -> `Francisco Castellanos`

### 3. Missing Possessives and Apostrophes

Extraction often separates possessive `s` or drops apostrophes.

- `Man S Best Friend` -> `Man's Best Friend`
- `Your Horse S Tackle` -> `Your Horse's Tackle`
- `Carson S Folly` -> `Carson's Folly`
- `King S People in...` -> `King's People in...`

Use the correct apostrophe character for the manuscript and keep the fix
consistent across the file.

### 4. Bold and Heading Confusion

Sometimes bold inline terms land inside heading syntax.

- if a `###` line contains bold markers in the middle of sentence text, treat
  it as body prose, not a real heading
- if a heading is only a misread bold term, restore the inline bold markers
- if a heading text is really an ampersand split or punctuation loss, repair
  it by meaning, not by the literal extraction artifact

### 5. Sidebar-Split Paragraphs and Orphaned Text

Two-column layout often slices a paragraph in half and drops sidebar text in
between.

- restore the sentence to its original flow when the continuation is obvious
- move orphaned sidebar fragments back to the paragraph they belong to
- search for broken sentence joins where the line ends mid-thought and the
  next visible text continues with lowercase prose

### 6. Running Headers Embedded in Content

Removing standalone headers is not enough.

- also remove running headers when they appear inside paragraphs as stray
  substrings
- treat appendix and chapter titles as searchable header strings, not only
  as standalone lines

### 7. Garbled Multi-Column Table Data

This is the hardest class of failure.

Tell-tale signs:

- a line is very long and contains several roll numbers or repeated stat
  patterns
- description text is split between the wrong columns
- data from adjacent rows is compressed into one cell
- a table continuation header gets merged with the first data row

Fix strategy:

1. Read the original PDF page or spread.
2. Determine the intended row and column structure.
3. Reconstruct the table explicitly.
4. Replace the garbled block in one operation.

### 8. Broken Pipe Tables

Broken pipe tables need a full rewrite when the row structure is lost.

Common cases:

- column-swapped descriptions
- multiple logical rows merged into one markdown row
- repeated header rows from page breaks
- plain text that should have been a table
- table cells with broken words or split words at cell boundaries

The rule is simple: every logical entry should end up in exactly one row.

### 9. Loose Bullet Lists

If extraction inserts blank lines between bullet items, compact them so the
list renders as a tight list instead of a loose one.

### 10. Project-Specific Manual Passes

After the deterministic pipeline, chapter-by-chapter manual cleanup is still
normal.

When you do manual repair for Tales:

- keep one script or note per recurring fix
- prefer batch/page-range repairs over document-wide guesswork
- do not invent missing text
- preserve the manuscript voice and structure

## Known Limitations

- Complex tables with merged cells or nested headers often need manual repair.
- Decorative fonts may not be detected as headings.
- Rotated text, vertical text, and right-to-left text are not handled well.
- OCR is not included. Scanned PDFs need a separate OCR pass first.

## Project References

Keep reusable notes with the project when a reference area exists:

- add a project notes file for successful conversions and recurring failure modes
- record tool versions and install notes alongside the project or in a
  dedicated references folder
- keep chapter-level or script-level notes when a specific repair pattern repeats

## Validation

Check the final markdown before you trust it:

- no page-number artifacts remain
- no running headers remain
- spaced headings are reconstructed correctly
- chapter hierarchy reads cleanly from book title to section headings
- epigraphs and attributions are formatted as blockquotes
- sidebar text is isolated from body prose
- tables are valid pipe tables with one logical entry per row
- no `<br>` tags remain in body text
- no picture placeholders remain
- no multi-row compression remains in tables
- paragraphs flow naturally without mid-sentence breaks
- markdown lint passes if the file stays in the repository

## Splitting Into Chapter Files

After cleanup, split the single markdown file into per-chapter files only if
the chapter boundaries are stable and obvious.

Typical approach:

1. Find all `## Chapter N - Title` headings.
2. Use those headings as split markers.
3. Write one file per chapter using the repository naming convention.
4. Keep the unsplit source markdown until the split has been verified.
