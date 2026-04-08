#!/usr/bin/env python3
"""Fix Chapter 10 lifepath tables: parse garbled PDF data into clean format."""
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

FILENAME = '10-patience-is-a-virtue.md'
with open(FILENAME, 'r', encoding='utf-8') as f:
    data = f.read()

fixes = 0

# ============================================================
# Fix 1: Remove duplicate ### Appendix: Your Tale Begins running headers
# (keep only the first one at the start of the appendix section)
# ============================================================
lines = data.split('\n')
first_found = False
new_lines = []
for line in lines:
    if line.strip() == '### Appendix: Your Tale Begins':
        if not first_found:
            first_found = True
            new_lines.append(line)
        else:
            # Skip this duplicate running header
            fixes += 1
    else:
        new_lines.append(line)
data = '\n'.join(new_lines)

# ============================================================
# Fix 2: Fix "Te " → "The " in table headers
# ============================================================
data_new = data.replace('|**Te ', '|**The ')
if data_new != data:
    count = data.count('|**Te ') - data_new.count('|**Te ')
    fixes += count
    data = data_new

# ============================================================
# Fix 3: Fix "Pacifc" → "Pacific" typo
# ============================================================
if 'Pacifc' in data:
    data = data.replace('Pacifc', 'Pacific')
    fixes += 1

# ============================================================
# Fix 4: Collapse duplicate-column region headers into single-column
# Pattern: |**X**|**X**|**X**|**X**| → **X** (bold line)
# ============================================================
def collapse_dup_header(match):
    global fixes
    # Get the cell content from first column
    full = match.group(0)
    # Extract the bold text from the first cell
    cell_match = re.search(r'\|\*\*(.+?)\*\*\|', full)
    if cell_match:
        content = cell_match.group(1).strip()
        fixes += 1
        return f'**{content}**'
    return full

# Match table rows where all cells have the same bold content, followed by separator row
pattern = r'^\|(\*\*[^|]+\*\*\|){2,}\n\|[-|]+\|'
data = re.sub(pattern, lambda m: collapse_dup_header(m), data, flags=re.MULTILINE)

# Also handle single-row duplicate headers without separator
# For Living Outcome tables: |**X**|**X**|**X**|**X**|**X**|\n|---|---|---|---|---|\n|**Roll**|...
pattern2 = r'^\|(\*\*LIVING OUTCOME TABLE[^|]+\*\*\|){2,}\n(\|---\|[^\n]*\n)(\|\*\*Roll\*\*\|.+)'
def fix_living_header(match):
    global fixes
    cell = re.search(r'\|\*\*(.+?)\*\*\|', match.group(0))
    if cell:
        title = cell.group(1).strip()
        fixes += 1
        return f'**{title}**\n\n{match.group(2)}{match.group(3)}'
    return match.group(0)
data = re.sub(pattern2, fix_living_header, data, flags=re.MULTILINE)


# ============================================================
# Fix 5: Parse garbled upbringing entries into clean format
# ============================================================
# Known ability names in the game
ABILITIES = [
    "FIGHTIN'", "LABOR", "PRESENCE", "RESILIENCE",
    "LIGHT-FINGERED", "MOVE", "HAWKEYE", "INSIGHT",
    "ANIMAL HANDLIN'", "SHOOTIN'", "NATURE", "PERFORMIN'",
    "BOOKLEARNIN'", "DOCTORIN'", "MAKIN'", "OPERATE",
]

ATTRIBUTES = ["Grit", "Quick", "Cunning", "Docity"]

def parse_upbringing_block(text):
    """Parse a garbled block of upbringing entries into clean format.
    
    Input: garbled text like:
    "4 Your father was a soldier... Grit 5 FIGHTIN' 1 he was invalided... Quick 4 RESILIENCE 1..."
    
    Output: list of (roll, narrative, attributes_dict, abilities_list) tuples
    """
    entries = []
    
    # First, handle region name that might appear inline
    # Example: "British North America 1 You grew up..."
    # We need to detect these and split them out
    
    # Split into individual entries by detecting roll numbers
    # Roll numbers are 1-6 and appear at the start or after a region name
    # Pattern: number followed by text that doesn't start with another attribute
    
    # Strategy: find all attribute/ability tokens and mark their positions
    tokens = []
    
    for attr in ATTRIBUTES:
        for m in re.finditer(r'\b' + re.escape(attr) + r'\s+(\d)', text):
            tokens.append((m.start(), m.end(), 'attr', attr, int(m.group(1))))
    
    for ability in ABILITIES:
        for m in re.finditer(re.escape(ability) + r'\s+(\d)', text):
            tokens.append((m.start(), m.end(), 'ability', ability, int(m.group(1))))
    
    tokens.sort(key=lambda x: x[0])
    
    # Now find roll entry boundaries: a digit 1-6 that starts an entry
    # These are identified by: (start of text OR after a complete set of 4 attributes) + digit
    entry_starts = []
    
    # Find positions of digits 1-6 that could be roll numbers
    for m in re.finditer(r'(?:^|\s)(\d)\s+(?=[A-Z])', text):
        digit = int(m.group(1))
        if 1 <= digit <= 6:
            entry_starts.append((m.start(), digit))
    
    if not entry_starts:
        return None  # Can't parse this block
    
    # For each entry, extract the text between this entry start and the next
    parsed = []
    for i, (start, roll) in enumerate(entry_starts):
        if i + 1 < len(entry_starts):
            end = entry_starts[i + 1][0]
        else:
            end = len(text)
        
        entry_text = text[start:end].strip()
        # Remove the leading roll number
        entry_text = re.sub(r'^\d\s+', '', entry_text)
        
        # Extract all attributes and abilities from this entry
        entry_tokens = [(t[0] - start, t[1] - start, t[2], t[3], t[4]) 
                       for t in tokens if start <= t[0] < end]
        
        attrs = {}
        abilities = []
        
        for _, _, ttype, name, value in entry_tokens:
            if ttype == 'attr':
                attrs[name] = value
            else:
                abilities.append((name, value))
        
        # Build narrative by removing all stat tokens from the text
        narrative = entry_text
        # Remove from right to left to preserve positions
        for tok_start, tok_end, _, _, _ in sorted(entry_tokens, key=lambda x: x[0], reverse=True):
            adj_start = tok_start - (start - start)  # already adjusted above
            # Actually we need to remove from the entry_text
            pass
        
        # Simpler approach: use regex to strip all stat tokens
        for attr in ATTRIBUTES:
            narrative = re.sub(r'\b' + re.escape(attr) + r'\s+\d\b', '', narrative)
        for ability in ABILITIES:
            narrative = re.sub(re.escape(ability) + r'\s+\d', '', narrative)
        
        # Clean up extra whitespace
        narrative = re.sub(r'\s+', ' ', narrative).strip()
        # Fix split words with hyphens: "hunt- ing" → "hunting"
        narrative = re.sub(r'(\w)-\s+(\w)', r'\1\2', narrative)
        # Fix "shop- keepers" type splits
        narrative = re.sub(r'(\w)-\s*\n?\s*(\w)', r'\1\2', narrative)
        # Remove trailing periods if doubled
        narrative = narrative.rstrip()
        
        parsed.append((roll, narrative, attrs, abilities))
    
    return parsed

def format_entries(entries, region_name=None):
    """Format parsed entries into clean markdown."""
    lines = []
    if region_name:
        lines.append(f'**{region_name}**')
        lines.append('')
    
    for roll, narrative, attrs, abilities in entries:
        lines.append(f'**{roll}.** {narrative}')
        
        if attrs:
            attr_parts = []
            for a in ATTRIBUTES:
                if a in attrs:
                    attr_parts.append(f'{a} {attrs[a]}')
            lines.append(f'  **Attributes:** {", ".join(attr_parts)}')
        
        if abilities:
            ab_parts = [f'{name} {val}' for name, val in abilities]
            lines.append(f'  **Abilities:** {", ".join(ab_parts)}')
        
        lines.append('')
    
    return '\n'.join(lines)

# Find and replace each garbled upbringing block
# These blocks are between region table headers and the next section/header

# Let's identify the garbled blocks by looking for the pattern:
# A table header line (region) → separator → garbled text → next table header or section

# Actually, let's be more surgical. The garbled blocks all share a pattern:
# they contain "Grit \d" and "Quick \d" and "Cunning \d" and "Docity \d" 
# all on the same or consecutive lines within a paragraph (no heading markers)

# Find all garbled upbringing paragraphs
garbled_pattern = re.compile(
    r'^(\d\s+.+?(?:Grit\s+\d.+?Quick\s+\d.+?Cunning\s+\d.+?Docity\s+\d.+?))+$',
    re.MULTILINE | re.DOTALL
)

# Let's try a different approach - work line by line and find paragraphs
# that contain attribute data
paragraphs = data.split('\n\n')
new_paragraphs = []
block_fixes = 0

# Track region context
current_region = None
REGION_NAMES = {
    'The Ottoman Empire, the Middle East and North Africa': 'The Ottoman Empire, the Middle East and North Africa',
    'British North America': 'British North America',
    'Continental Northwest and the Great Northern Plains': 'Continental Northwest and the Great Northern Plains',
    'The Great Lakes and Midwest': 'The Great Lakes and Midwest, including The Six Nations and "Indian Territory"',
    'Europe': 'Europe',
    'The Northeast': 'The Northeast',
    'Southeast': 'Southeast',
    'The South': 'The South, Southern Great Plains, Mexico and South America',
    'West Coast and Great Basin': 'West Coast and Great Basin',
    'East Asia and the Pacific': 'East Asia and the Pacific',
    'India, and Equatorial and Southern Africa': 'India, and Equatorial and Southern Africa',
}

for para in paragraphs:
    # Check if this paragraph contains garbled upbringing data
    # Key indicator: contains multiple "Grit \d" patterns
    grit_count = len(re.findall(r'Grit\s+\d', para))
    
    if grit_count >= 2 and 'Docity' in para:
        # This is a garbled upbringing block
        # Check for inline region names
        working = para.strip()
        
        # Detect inline region names (e.g., "British North America 1 You grew up...")
        # These appear as text before a digit that starts an entry
        region_splits = []
        for region_key in ['British North America', 'Continental Northwest', 
                          'Europe ', 'The Northeast', 'Southeast',
                          ', Southern Great Plains, Mexico and South America',
                          'The South', 'West Coast and Great Basin',
                          'East Asia and the Pacific', 'India, and Equatorial and Southern Africa']:
            if region_key in working:
                idx = working.index(region_key)
                region_splits.append((idx, region_key.strip()))
        
        # Parse the entries
        entries = parse_upbringing_block(working)
        
        if entries and len(entries) >= 2:
            formatted = format_entries(entries)
            new_paragraphs.append(formatted)
            block_fixes += 1
        else:
            new_paragraphs.append(para)  # Keep original if parsing fails
    else:
        new_paragraphs.append(para)

if block_fixes > 0:
    data = '\n\n'.join(new_paragraphs)
    fixes += block_fixes
    print(f'  Reformatted {block_fixes} garbled upbringing block(s)')

# ============================================================
# Fix 6: Clean the Family Background table
# ============================================================
# The 2D6 Family Background section is readable but could use cleanup
# Fix any remaining "Appendix: your tale begins" that might be remnants
old_remnant = '\nAppendix: your tale begins\n'
while old_remnant in data:
    data = data.replace(old_remnant, '\n')
    fixes += 1

# ============================================================
# Final: Clean up consecutive blank lines
# ============================================================
while '\n\n\n' in data:
    data = data.replace('\n\n\n', '\n\n')

with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write(data)

print(f'\nTotal ch10 fixes: {fixes}')
