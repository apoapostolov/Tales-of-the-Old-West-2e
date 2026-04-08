#!/usr/bin/env python3
"""Fix Chapter 10 lifepath upbringing tables.
Strategy: tokenize garbled single-line blocks and reassemble entries."""
import re
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

FILENAME = '10-patience-is-a-virtue.md'
with open(FILENAME, 'r', encoding='utf-8') as f:
    data = f.read()

ATTRIBUTES = ["Grit", "Quick", "Cunning", "Docity"]
ABILITIES = [
    "FIGHTIN'", "LABOR", "PRESENCE", "RESILIENCE",
    "LIGHT-FINGERED", "MOVE", "HAWKEYE", "INSIGHT",
    "ANIMAL HANDLIN'", "SHOOTIN'", "NATURE", "PERFORMIN'",
    "BOOKLEARNIN'", "DOCTORIN'", "MAKIN'", "OPERATE",
]

# Build regex that matches any stat token (attribute or ability + value)
attr_pattern = '|'.join(re.escape(a) for a in ATTRIBUTES)
ability_pattern = '|'.join(re.escape(a) for a in ABILITIES)
STAT_RE = re.compile(
    rf'(?:{attr_pattern}|{ability_pattern})\s+\d'
)

# Region names that appear inline in the garbled blocks
INLINE_REGIONS = [
    "British North America",
    "Continental Northwest",
    "Europe",
    "The Northeast",
    "Southeast",
    ", Southern Great Plains, Mexico and South America",
    "The South",
    "West Coast and Great Basin",
    "East Asia and the Pacific",
    "India, and Equatorial and Southern Africa",
]


def parse_garbled_line(line):
    """Parse a garbled single-line block into structured entries.
    
    Returns list of (region_or_None, roll, narrative, attrs_dict, abilities_list)
    """
    # Strategy:
    # 1. Find all stat token positions
    # 2. Find all potential entry boundaries (digit 1-6 followed by narrative)
    # 3. For each entry, collect its stats and narrative
    
    # Step 1: Find all stat tokens and their positions
    stat_positions = []  # (start, end, type, name, value)
    for m in re.finditer(rf'({attr_pattern})\s+(\d)', line):
        stat_positions.append((m.start(), m.end(), 'attr', m.group(1), int(m.group(2))))
    for m in re.finditer(rf"({ability_pattern})\s+(\d)", line):
        stat_positions.append((m.start(), m.end(), 'ability', m.group(1), int(m.group(2))))
    stat_positions.sort(key=lambda x: x[0])
    
    # Build a set of character ranges covered by stat tokens
    stat_ranges = set()
    for start, end, *_ in stat_positions:
        for i in range(start, end):
            stat_ranges.add(i)
    
    # Step 2: Find entry boundaries
    # Look for patterns like: (end_of_abilities) (\d) (start_of_narrative)
    # A roll number is a digit 1-6 that is NOT part of a stat token
    
    entries_raw = []
    
    # Find all digits in the line that could be roll numbers
    for m in re.finditer(r'(?:^|\s)(\d)\s', line):
        digit_pos = m.start(1)
        digit = int(m.group(1))
        
        # Skip if this digit is inside a stat token
        if digit_pos in stat_ranges:
            continue
        
        # Skip digits > 6 (not valid roll numbers)
        if digit < 1 or digit > 6:
            continue
        
        # Check what follows: should be narrative text (not a stat name)
        after = line[m.end():m.end()+30].strip()
        
        # Skip if followed by a stat name
        is_stat_value = False
        for s_start, s_end, *_ in stat_positions:
            if abs(digit_pos - s_end) <= 2:
                is_stat_value = True
                break
        if is_stat_value:
            continue
            
        # Check: the position right before this digit should be either:
        #   - Start of line
        #   - End of previous entry's stats (an ability value digit)
        #   - A region name transition
        entries_raw.append((digit_pos, digit))
    
    if not entries_raw:
        return None
    
    # Step 3: Also find inline region names
    region_positions = []
    for region in INLINE_REGIONS:
        idx = line.find(region)
        while idx != -1:
            region_positions.append((idx, region.strip().lstrip(', ')))
            idx = line.find(region, idx + 1)
    region_positions.sort()
    
    # Step 4: For each entry, extract the text and parse stats
    results = []
    
    for i, (entry_start, roll) in enumerate(entries_raw):
        # Entry text extends from this position to the next entry start
        if i + 1 < len(entries_raw):
            entry_end = entries_raw[i + 1][0]
        else:
            entry_end = len(line)
        
        entry_text = line[entry_start:entry_end]
        # Remove leading roll number
        entry_text = re.sub(r'^\d\s+', '', entry_text)
        
        # Find which region this entry belongs to
        current_region = None
        for rpos, rname in region_positions:
            if rpos < entry_start:
                current_region = rname
        
        # Extract stats for this entry (those within the entry's range)
        attrs = {}
        abilities = []
        for s_start, s_end, s_type, s_name, s_value in stat_positions:
            if entry_start <= s_start < entry_end:
                if s_type == 'attr':
                    attrs[s_name] = s_value
                else:
                    abilities.append((s_name, s_value))
        
        # Remove stat tokens from narrative
        narrative = entry_text
        # Remove from right to left to preserve positions
        stat_tokens_in_entry = [
            (s_start - entry_start - len(str(roll)) - 1, s_end - entry_start - len(str(roll)) - 1, s_name, s_value)
            for s_start, s_end, s_type, s_name, s_value in stat_positions
            if entry_start <= s_start < entry_end
        ]
        
        # Use regex replacement instead (more reliable)
        for attr in ATTRIBUTES:
            narrative = re.sub(rf'\b{re.escape(attr)}\s+\d', '', narrative)
        for ability in ABILITIES:
            narrative = re.sub(rf'{re.escape(ability)}\s+\d', '', narrative)
        
        # Also strip any inline region names that are inside this entry
        for rpos, rname in region_positions:
            if entry_start <= rpos < entry_end:
                # The region name is inside this entry's text range
                # Find and remove it from narrative
                for region_full in INLINE_REGIONS:
                    narrative = narrative.replace(region_full, '')
        
        # Clean up whitespace
        narrative = re.sub(r'\s+', ' ', narrative).strip()
        # Fix hyphenated word breaks: "hunt- ing" → "hunting", "shop- keepers" → "shopkeepers"  
        narrative = re.sub(r'(\w)- (\w)', r'\1\2', narrative)
        # Fix "com- munities" style breaks
        narrative = re.sub(r'(\w)-\s+(\w)', r'\1\2', narrative)
        # Remove trailing region headers
        narrative = narrative.strip()
        
        results.append((current_region, roll, narrative, attrs, abilities))
    
    return results


def format_entries(entries):
    """Format parsed entries into clean markdown blocks."""
    out_lines = []
    current_region = None
    
    for region, roll, narrative, attrs, abilities in entries:
        # Add region header if it changed
        if region and region != current_region:
            if current_region is not None:
                out_lines.append('')
            out_lines.append(f'**{region}**')
            out_lines.append('')
            current_region = region
        
        out_lines.append(f'**{roll}.** {narrative}')
        
        if attrs:
            attr_parts = []
            for a in ATTRIBUTES:
                if a in attrs:
                    attr_parts.append(f'{a} {attrs[a]}')
            out_lines.append(f'  *Attributes:* {", ".join(attr_parts)}')
        
        if abilities:
            ab_parts = [f'{name} {val}' for name, val in abilities]
            out_lines.append(f'  *Abilities:* {", ".join(ab_parts)}')
        
        out_lines.append('')
    
    return '\n'.join(out_lines)


# Find and process garbled lines
lines = data.split('\n')
new_lines = []
fixes = 0

for i, line in enumerate(lines):
    # Check if this line is a garbled upbringing block
    # Key indicator: contains at least 3 "Grit" patterns AND at least 3 "Docity" patterns
    grit_count = len(re.findall(r'\bGrit\s+\d', line))
    docity_count = len(re.findall(r'\bDocity\s+\d', line))
    
    if grit_count >= 3 and docity_count >= 3 and len(line) > 500:
        entries = parse_garbled_line(line)
        if entries and len(entries) >= 3:
            formatted = format_entries(entries)
            new_lines.append(formatted)
            fixes += 1
            print(f'  Line {i+1}: parsed {len(entries)} entries ({grit_count} Grit tokens)')
        else:
            new_lines.append(line)
            print(f'  Line {i+1}: FAILED to parse (got {len(entries) if entries else 0} entries)')
    else:
        new_lines.append(line)

data = '\n'.join(new_lines)

# Also fix remaining issues:
# 1. Fix "Te " in region headers  
data = data.replace('|**Te ', '|**The ')

# 2. Fix "Pacifc" typo
data = data.replace('Pacifc', 'Pacific')

# 3. Collapse duplicate-column table headers
# Pattern: |**X**|**X**|**X**|**X**|\n|---|---|---|---|
def collapse_dup_table(match):
    row = match.group(1)
    cell = re.search(r'\*\*(.+?)\*\*', row)
    if cell:
        return f'\n**{cell.group(1)}**\n'
    return match.group(0)

data = re.sub(r'\n(\|\*\*[^|]+\*\*\|(?:\*\*[^|]+\*\*\|)*)\n\|[-|]+\|\n', collapse_dup_table, data)

# 4. Clean up consecutive blank lines
while '\n\n\n' in data:
    data = data.replace('\n\n\n', '\n\n')

with open(FILENAME, 'w', encoding='utf-8') as f:
    f.write(data)

print(f'\nTotal garbled blocks reformatted: {fixes}')
