#!/usr/bin/env python3
"""Fix Chapter 10 lifepath upbringing tables - v4.
Uses Docity end-of-abilities as definitive entry boundary."""
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

FILENAME = '10-patience-is-a-virtue.md'
with open(FILENAME, 'r', encoding='utf-8') as f:
    data = f.read()

ATTRIBUTES = ["Grit", "Quick", "Cunning", "Docity"]
ABILITIES = [
    "ANIMAL HANDLIN'", "BOOKLEARNIN'", "DOCTORIN'", "FIGHTIN'",
    "HAWKEYE", "INSIGHT", "LABOR", "LIGHT-FINGERED",
    "MAKIN'", "MOVE", "NATURE", "OPERATE",
    "PERFORMIN'", "PRESENCE", "RESILIENCE", "SHOOTIN'",
]

# Build ability regex - matches ability name + space + digit
ABILITY_NAMES_RE = "|".join(re.escape(a) for a in ABILITIES)
ABILITY_TOKEN_RE = re.compile(rf'(?:{ABILITY_NAMES_RE})\s+\d')

# Attribute regex  
ATTR_NAMES_RE = "|".join(re.escape(a) for a in ATTRIBUTES)
ATTR_TOKEN_RE = re.compile(rf'(?:{ATTR_NAMES_RE})\s+\d')

# Any stat token
ALL_STAT_RE = re.compile(rf'(?:{ATTR_NAMES_RE}|{ABILITY_NAMES_RE})\s+\d')

# Region names that may appear inline
INLINE_REGION_NAMES = [
    "British North America",
    "Europe",
    "The Northeast",
    "The South",
    "West Coast and Great Basin",
    "East Asia and the Pacific",
    "India, and Equatorial and Southern Africa",
    ", Southern Great Plains, Mexico and South America",
]


def find_entry_boundaries(line):
    """Find entry boundaries using Docity as end marker.
    Returns list of (entry_start, entry_end) positions."""
    
    # Find all Docity positions
    docity_matches = list(re.finditer(r'\bDocity\s+\d', line))
    if not docity_matches:
        return []
    
    boundaries = []  # list of end-of-entry positions
    
    for dm in docity_matches:
        pos = dm.end()
        # Scan forward consuming ability tokens
        while pos < len(line):
            remaining = line[pos:]
            # Skip whitespace
            stripped = remaining.lstrip(' ')
            ws_consumed = len(remaining) - len(stripped)
            
            # Try to match an ability token at the start
            m = ABILITY_TOKEN_RE.match(stripped)
            if m:
                pos = pos + ws_consumed + m.end()
            else:
                break
        
        boundaries.append(pos)
    
    # Entry ranges: (start_i, end_i) where
    # start_0 = 0 (start of line)
    # end_i = entry boundary_i  
    # start_{i+1} = boundary_i
    ranges = []
    prev = 0
    for b in boundaries:
        ranges.append((prev, b))
        prev = b
    
    return ranges


def parse_entry_text(text):
    """Parse a single entry's text into (roll, narrative, attrs, abilities).
    
    Input: text like '4 Your father was a soldier... Grit 5 FIGHTIN' 1 he was invalided... Quick 4 RESILIENCE 1 Cunning 3 SHOOTIN' 2 Docity 3 HAWKEYE 2'
    """
    # Extract attributes
    attrs = {}
    for attr in ATTRIBUTES:
        m = re.search(rf'\b{re.escape(attr)}\s+(\d)', text)
        if m:
            attrs[attr] = int(m.group(1))
    
    # Extract abilities
    abilities = []
    for m in ABILITY_TOKEN_RE.finditer(text):
        tok = m.group()
        parts = tok.rsplit(None, 1)
        if len(parts) == 2:
            abilities.append((parts[0], int(parts[1])))
    
    # Strip all stat tokens to get narrative
    narrative = ALL_STAT_RE.sub('', text)
    
    # Strip inline region names
    for region in INLINE_REGION_NAMES:
        narrative = narrative.replace(region, ' ')
    
    # Clean whitespace
    narrative = re.sub(r'\s+', ' ', narrative).strip()
    
    # Fix hyphenated word breaks: "hunt- ing" → "hunting"
    narrative = re.sub(r'(\w)- (\w)', r'\1\2', narrative)
    narrative = re.sub(r'(\w)-\s{2,}(\w)', r'\1\2', narrative)
    
    # Extract roll number from start
    roll_match = re.match(r'^(\d)\s+(.*)$', narrative)
    if roll_match:
        roll = int(roll_match.group(1))
        narrative = roll_match.group(2).strip()
    else:
        roll = 0
        # Try to find roll number after stripping
        rm = re.search(r'^\s*(\d)\s+', narrative)
        if rm:
            roll = int(rm.group(1))
            narrative = narrative[rm.end():].strip()
    
    # Clean up leftover comma/period issues
    narrative = narrative.strip().strip(',').strip()
    
    return roll, narrative, attrs, abilities


def format_entries(entries):
    """Format entries as markdown."""
    lines = []
    for roll, narrative, attrs, abilities in entries:
        lines.append(f'**{roll}.** {narrative}')
        if attrs:
            parts = [f'{a} {attrs[a]}' for a in ATTRIBUTES if a in attrs]
            lines.append(f'  *Attributes:* {", ".join(parts)}')
        if abilities:
            parts = [f'{n} {v}' for n, v in abilities]
            lines.append(f'  *Abilities:* {", ".join(parts)}')
        lines.append('')
    return '\n'.join(lines)


# ============================================================
# Process the file
# ============================================================
file_lines = data.split('\n')
new_lines = []
fixes = 0

for idx, line in enumerate(file_lines):
    grit_count = len(re.findall(r'\bGrit\s+\d', line))
    docity_count = len(re.findall(r'\bDocity\s+\d', line))
    
    if grit_count >= 3 and docity_count >= 3 and len(line) > 500:
        boundaries = find_entry_boundaries(line)
        
        if len(boundaries) >= 3:
            entries = []
            for start, end in boundaries:
                chunk = line[start:end].strip()
                if not chunk:
                    continue
                roll, narrative, attrs, abilities = parse_entry_text(chunk)
                
                # Skip entries with no attributes (not real entries)
                if len(attrs) >= 3:
                    entries.append((roll, narrative, attrs, abilities))
            
            if len(entries) >= 3:
                formatted = format_entries(entries)
                new_lines.append(formatted)
                fixes += 1
                rolls = [e[0] for e in entries]
                has4 = all(len(e[2]) == 4 for e in entries)
                print(f'  Line {idx+1}: {len(entries)} entries, rolls={rolls}, all-4-attrs={has4}')
            else:
                new_lines.append(line)
                print(f'  Line {idx+1}: only {len(entries)} valid entries, skipping')
        else:
            new_lines.append(line)
            print(f'  Line {idx+1}: only {len(boundaries)} boundaries, skipping')
    else:
        new_lines.append(line)

data = '\n'.join(new_lines)

# ============================================================
# Additional fixes
# ============================================================
# Fix "Te " in table headers
data = data.replace('|**Te ', '|**The ')

# Fix "Pacifc" typo
data = data.replace('Pacifc', 'Pacific')

# Collapse duplicate-column table headers:
# |**X**|**X**|...|  +  |---|---|...|  →  **X**
def collapse_dup_header(match):
    row = match.group(0)
    cell = re.search(r'\*\*(.+?)\*\*', row)
    if cell:
        return f'**{cell.group(1).strip()}**'
    return row

data = re.sub(
    r'^\|(?:\*\*[^|\n]+\*\*\|){2,}\n\|[-|]+\|',
    collapse_dup_header,
    data,
    flags=re.MULTILINE
)

# Remove remaining standalone "Appendix: your tale begins" lines
data = re.sub(r'^Appendix: your tale begins\s*$', '', data, flags=re.MULTILINE)

# Clean consecutive blank lines
while '\n\n\n' in data:
    data = data.replace('\n\n\n', '\n\n')

with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write(data)

print(f'\nTotal garbled blocks reformatted: {fixes}')
