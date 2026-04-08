#!/usr/bin/env python3
"""Fix Chapter 10 lifepath upbringing tables - v5.
Uses Docity as entry boundary. Handles U+2019 smart quotes in ability names."""
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

FILENAME = '10-patience-is-a-virtue.md'
with open(FILENAME, 'r', encoding='utf-8') as f:
    data = f.read()

SQ = '\u2019'  # Right single quotation mark (smart quote)

ATTRIBUTES = ["Grit", "Quick", "Cunning", "Docity"]
ABILITIES = [
    f"ANIMAL HANDLIN{SQ}", f"BOOKLEARNIN{SQ}", f"DOCTORIN{SQ}", f"FIGHTIN{SQ}",
    "HAWKEYE", "INSIGHT", "LABOR", "LIGHT-FINGERED",
    f"MAKIN{SQ}", "MOVE", "NATURE", "OPERATE",
    f"PERFORMIN{SQ}", "PRESENCE", "RESILIENCE", f"SHOOTIN{SQ}",
]

# Build regexes
ABILITY_NAMES_RE = "|".join(re.escape(a) for a in ABILITIES)
ATTR_NAMES_RE = "|".join(re.escape(a) for a in ATTRIBUTES)
ABILITY_TOKEN_RE = re.compile(rf'(?:{ABILITY_NAMES_RE})\s+\d')
ALL_STAT_RE = re.compile(rf'(?:{ATTR_NAMES_RE}|{ABILITY_NAMES_RE})\s+\d')

INLINE_REGIONS = [
    "British North America",
    "The Northeast",
    "The South",
    "West Coast and Great Basin",
    "East Asia and the Pacific",
    "India, and Equatorial and Southern Africa",
    ", Southern Great Plains, Mexico and South America",
]
# Note: "Europe" omitted to avoid stripping "European"/"Europeans" from narrative


def find_entry_boundaries(line):
    """Find entry boundaries using Docity + trailing abilities as end markers."""
    docity_matches = list(re.finditer(r'\bDocity\s+\d', line))
    if not docity_matches:
        return []
    
    boundaries = []
    for dm in docity_matches:
        pos = dm.end()
        while pos < len(line):
            remaining = line[pos:]
            stripped = remaining.lstrip(' ')
            ws = len(remaining) - len(stripped)
            m = ABILITY_TOKEN_RE.match(stripped)
            if m:
                pos = pos + ws + m.end()
            else:
                break
        boundaries.append(pos)
    
    ranges = []
    prev = 0
    for b in boundaries:
        ranges.append((prev, b))
        prev = b
    
    return ranges


def parse_entry_text(text):
    """Parse a single entry's text into (roll, narrative, attrs, abilities)."""
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
    
    # Strip stats to get narrative
    narrative = ALL_STAT_RE.sub('', text)
    
    # Strip inline region names - use word boundary to avoid stripping "European"
    for region in INLINE_REGIONS:
        narrative = narrative.replace(region, ' ')
    # Handle "Europe" separately with word boundary
    narrative = re.sub(r'\bEurope\b(?!an)', ' ', narrative)
    
    # Clean whitespace
    narrative = re.sub(r'\s+', ' ', narrative).strip()
    
    # Fix hyphenated word breaks
    narrative = re.sub(r'(\w)- (\w)', r'\1\2', narrative)
    narrative = re.sub(r'(\w)-\s{2,}(\w)', r'\1\2', narrative)
    
    # Extract roll number from start
    roll_match = re.match(r'^(\d)\s+(.*)$', narrative)
    if roll_match:
        roll = int(roll_match.group(1))
        narrative = roll_match.group(2).strip()
    else:
        roll = 0
    
    # Clean leading commas/periods
    narrative = re.sub(r'^[,.\s]+', '', narrative).strip()
    
    return roll, narrative, attrs, abilities


def format_entries(entries):
    """Format entries as clean markdown."""
    lines = []
    for roll, narrative, attrs, abilities in entries:
        # Normalize ability names for display: smart quote → ASCII
        display_abilities = [(n.replace(SQ, "'"), v) for n, v in abilities]
        
        lines.append(f'**{roll}.** {narrative}')
        if attrs:
            parts = [f'{a} {attrs[a]}' for a in ATTRIBUTES if a in attrs]
            lines.append(f'  *Attributes:* {", ".join(parts)}')
        if display_abilities:
            parts = [f'{n} {v}' for n, v in display_abilities]
            lines.append(f'  *Abilities:* {", ".join(parts)}')
        lines.append('')
    return '\n'.join(lines)


# ============================================================
# Process
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
                if len(attrs) >= 3:
                    entries.append((roll, narrative, attrs, abilities))
            
            if len(entries) >= 3:
                formatted = format_entries(entries)
                new_lines.append(formatted)
                fixes += 1
                rolls = [e[0] for e in entries]
                ab_counts = [len(e[3]) for e in entries]
                print(f'  Line {idx+1}: {len(entries)} entries, rolls={rolls}, abilities/entry={ab_counts}')
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    else:
        new_lines.append(line)

data = '\n'.join(new_lines)

# Additional fixes
data = data.replace('|**Te ', '|**The ')
data = data.replace('Pacifc', 'Pacific')
# Fix remaining "Te " in collapsed headers where it's at start of bold text
data = re.sub(r'\*\*Te ', '**The ', data)
# Fix "Te " within bold text (mid-string)
data = data.replace(' Te ', ' The ')

# Collapse duplicate-column table headers
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

# Remove remaining standalone running headers
data = re.sub(r'^Appendix: your tale begins\s*$', '', data, flags=re.MULTILINE)

# Clean consecutive blank lines  
while '\n\n\n' in data:
    data = data.replace('\n\n\n', '\n\n')

with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write(data)

print(f'\nTotal garbled blocks reformatted: {fixes}')
