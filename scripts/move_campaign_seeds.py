"""
Move the "Campaign Seeds" section from Chapter 07 to Chapter 08,
inserting it before the existing "Campaign Tales" section.
"""

import re

ch07 = r'c:\git-public\Tales-of-the-Old-West-2e\corebook\07-the-west-in-the-1870s.md'
ch08 = r'c:\git-public\Tales-of-the-Old-West-2e\corebook\08-campaigns-in-the-old-west.md'

with open(ch07, 'r', encoding='utf-8') as f:
    c07 = f.read()

with open(ch08, 'r', encoding='utf-8') as f:
    c08 = f.read()

# ── Extract the Campaign Seeds block from Ch 07 ──────────────────────────────
start_marker = '### Campaign Seeds\n'
end_marker   = '### Further Reading\n'

start_idx = c07.find(start_marker)
end_idx   = c07.find(end_marker)

if start_idx == -1:
    raise ValueError('Campaign Seeds marker not found in ch07')
if end_idx == -1:
    raise ValueError('Further Reading marker not found in ch07')

seeds_block = c07[start_idx:end_idx]   # includes trailing blank line before end_marker

# ── Remove the block from Ch 07 (leave Further Reading in place) ─────────────
c07_new = c07[:start_idx] + c07[end_idx:]
c07_new = re.sub(r'\n{3,}', '\n\n', c07_new)

# ── Insert into Ch 08 before "Campaign Tales" ────────────────────────────────
ch08_marker = '### Campaign Tales\n'
ch08_idx = c08.find(ch08_marker)
if ch08_idx == -1:
    raise ValueError('Campaign Tales marker not found in ch08')

# Insert seeds block (with a blank line separator) before "Campaign Tales"
c08_new = c08[:ch08_idx] + seeds_block + '\n' + c08[ch08_idx:]
c08_new = re.sub(r'\n{3,}', '\n\n', c08_new)

# ── Write both files ──────────────────────────────────────────────────────────
with open(ch07, 'w', encoding='utf-8', newline='\n') as f:
    f.write(c07_new)

with open(ch08, 'w', encoding='utf-8', newline='\n') as f:
    f.write(c08_new)

print(f'Ch07: {len(c07):,} -> {len(c07_new):,} chars')
print(f'Ch08: {len(c08):,} -> {len(c08_new):,} chars')

# Verify section headers in both files
print('\n--- Ch07 tail headers ---')
for i, line in enumerate(c07_new.splitlines()):
    if line.startswith('### ') and i > 950:
        print(f'  {i+1}: {line}')

print('\n--- Ch08 new headers around insertion ---')
lines08 = c08_new.splitlines()
for i, line in enumerate(lines08):
    if line.startswith('### Campaign'):
        print(f'  {i+1}: {line}')
