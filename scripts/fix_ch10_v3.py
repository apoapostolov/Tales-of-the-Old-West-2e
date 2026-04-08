#!/usr/bin/env python3
"""Fix Chapter 10 lifepath upbringing tables - v3.
Uses Grit positions as anchors to split entries."""
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

# Regex that matches an ability name followed by its value
ABILITY_RE = re.compile(
    r"(?:" + "|".join(re.escape(a) for a in ABILITIES) + r")\s+\d"
)

# Regex for each attribute
ATTR_RE = {
    attr: re.compile(rf'\b{re.escape(attr)}\s+(\d)')
    for attr in ATTRIBUTES
}

# Combined: any stat token (attribute or ability)
ALL_STAT_RE = re.compile(
    r"(?:" + "|".join(re.escape(a) for a in ATTRIBUTES) +
    r"|" + "|".join(re.escape(a) for a in ABILITIES) + r")\s+\d"
)

# Region names that appear inline
INLINE_REGIONS = [
    "British North America",
    "Europe ",
    "The Northeast ",
    ", Southern Great Plains, Mexico and South America",
    "The South ",
    "West Coast and Great Basin",
    "India, and Equatorial and Southern Africa",
]


def extract_stats(text):
    """Extract all attributes and abilities from text.
    Returns (attrs_dict, abilities_list)."""
    attrs = {}
    for attr in ATTRIBUTES:
        m = ATTR_RE[attr].search(text)
        if m:
            attrs[attr] = int(m.group(1))
    
    abilities = []
    for m in ABILITY_RE.finditer(text):
        token = m.group()
        parts = token.rsplit(None, 1)
        if len(parts) == 2:
            abilities.append((parts[0], int(parts[1])))
    
    return attrs, abilities


def strip_stats(text):
    """Remove all stat tokens from text, returning narrative."""
    result = ALL_STAT_RE.sub('', text)
    # Clean up whitespace
    result = re.sub(r'\s+', ' ', result).strip()
    return result


def find_after_last_ability(text, docity_pos):
    """After Docity \d at docity_pos, find where abilities end.
    Returns position after the last ability value following Docity."""
    # Find Docity + value
    m = re.search(r'Docity\s+\d', text[docity_pos:])
    if not m:
        return len(text)
    
    pos = docity_pos + m.end()
    
    # Scan forward: consume any abilities that follow
    while pos < len(text):
        remaining = text[pos:].lstrip()
        offset = len(text[pos:]) - len(remaining)
        
        # Try to match an ability at this position
        am = ABILITY_RE.match(remaining)
        if am:
            pos = pos + offset + am.end()
        else:
            break
    
    return pos


def parse_garbled_line(line):
    """Parse a garbled line into structured entries using Grit as anchor."""
    
    # Find all Grit positions
    grit_positions = [m.start() for m in re.finditer(r'\bGrit\s+\d', line)]
    
    if len(grit_positions) < 2:
        return None
    
    entries = []
    
    for i, grit_pos in enumerate(grit_positions):
        # Each entry spans from this Grit to the next Grit
        if i + 1 < len(grit_positions):
            next_grit_pos = grit_positions[i + 1]
        else:
            next_grit_pos = len(line)
        
        # The entry's stat block goes from Grit to end of abilities after Docity
        segment = line[grit_pos:next_grit_pos]
        
        # Find Docity in this segment
        docity_match = re.search(r'\bDocity\s+\d', segment)
        if not docity_match:
            # No Docity found - something is wrong, include whole segment
            entry_stat_text = segment
            trailing_text = ""
        else:
            # Find where abilities after Docity end
            end_pos = find_after_last_ability(segment, docity_match.start())
            entry_stat_text = segment[:end_pos]
            trailing_text = segment[end_pos:].strip()
        
        # Extract stats from the entry
        attrs, abilities = extract_stats(entry_stat_text)
        
        # The narrative for this entry comes from TWO places:
        # A) Text BEFORE this Grit (the "pre-text" from previous segment's trailing)
        # B) Text interleaved within the stat block itself
        
        # Get the narrative fragments from within the stat block
        narrative_within = strip_stats(entry_stat_text)
        
        # The pre-text (roll number + narrative start) comes from:
        # - For entry 0: text before first Grit
        # - For entry i>0: trailing text from previous entry
        
        # Store trailing text for next entry's pre-text
        entries.append({
            'attrs': attrs,
            'abilities': abilities,
            'narrative_within': narrative_within,
            'trailing_text': trailing_text,
        })
    
    # Now assemble the narratives
    # Pre-text for entry 0 is the text before the first Grit
    pre_texts = [line[:grit_positions[0]].strip()]
    for i in range(len(entries) - 1):
        pre_texts.append(entries[i]['trailing_text'])
    
    # Build final entries
    result = []
    for i, entry in enumerate(entries):
        pre_text = pre_texts[i]
        
        # Extract roll number from pre_text
        roll_match = re.match(r'(\d)\s*(.*)', pre_text)
        if roll_match:
            roll = int(roll_match.group(1))
            narrative_start = roll_match.group(2).strip()
        else:
            # Check for region name before roll number
            found_roll = False
            for region in INLINE_REGIONS:
                if pre_text.startswith(region.strip()):
                    remainder = pre_text[len(region):].strip().lstrip(', ')
                    rm = re.match(r'(\d)\s*(.*)', remainder)
                    if rm:
                        roll = int(rm.group(1))
                        narrative_start = rm.group(2).strip()
                        found_roll = True
                        break
            if not found_roll:
                # Last resort: try to find any digit
                rm = re.search(r'(\d)\s+(\w)', pre_text)
                if rm:
                    roll = int(rm.group(1))
                    narrative_start = pre_text[rm.start(2):].strip()
                else:
                    roll = 0
                    narrative_start = pre_text
        
        # Combine narrative: start + within
        full_narrative = narrative_start
        if entry['narrative_within']:
            if full_narrative:
                full_narrative += " " + entry['narrative_within']
            else:
                full_narrative = entry['narrative_within']
        
        # Clean up narrative
        full_narrative = re.sub(r'\s+', ' ', full_narrative).strip()
        # Fix hyphenated word breaks
        full_narrative = re.sub(r'(\w)- (\w)', r'\1\2', full_narrative)
        full_narrative = re.sub(r'(\w)-\s{2,}(\w)', r'\1\2', full_narrative)
        # Remove region names that leaked into narrative
        for region in INLINE_REGIONS:
            full_narrative = full_narrative.replace(region.strip(), '').strip()
        full_narrative = re.sub(r'^[,\s]+', '', full_narrative)
        full_narrative = re.sub(r'\s+', ' ', full_narrative).strip()
        
        result.append((roll, full_narrative, entry['attrs'], entry['abilities']))
    
    return result


def format_entries(entries):
    """Format parsed entries into clean markdown."""
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


# Process the file
lines = data.split('\n')
new_lines = []
fixes = 0

for i, line in enumerate(lines):
    grit_count = len(re.findall(r'\bGrit\s+\d', line))
    
    if grit_count >= 3 and len(line) > 500:
        entries = parse_garbled_line(line)
        if entries and len(entries) >= 3:
            formatted = format_entries(entries)
            new_lines.append(formatted)
            fixes += 1
            rolls = [e[0] for e in entries]
            print(f'  Line {i+1}: {len(entries)} entries, rolls={rolls}')
        else:
            new_lines.append(line)
            print(f'  Line {i+1}: parse failed')
    else:
        new_lines.append(line)

data = '\n'.join(new_lines)

# Additional fixes
data = data.replace('|**Te ', '|**The ')
data = data.replace('Pacifc', 'Pacific')

# Collapse duplicate-column headers
def collapse_header(match):
    row = match.group(0)
    cell = re.search(r'\*\*(.+?)\*\*', row)
    if cell:
        return f'**{cell.group(1)}**'
    return row

# Match: |**X**|**X**|...|  followed by |---|---|...|
data = re.sub(
    r'^\|(\*\*[^|\n]+\*\*\|){2,}\n\|[-|]+\|',
    lambda m: collapse_header(m),
    data,
    flags=re.MULTILINE
)

# Clean consecutive blank lines
while '\n\n\n' in data:
    data = data.replace('\n\n\n', '\n\n')

# Remove remaining "Appendix: your tale begins" standalone lines at start-of-line
data = re.sub(r'^Appendix: your tale begins\s*$', '', data, flags=re.MULTILINE)
while '\n\n\n' in data:
    data = data.replace('\n\n\n', '\n\n')

with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write(data)

print(f'\nTotal garbled blocks reformatted: {fixes}')
