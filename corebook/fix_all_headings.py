"""Master heading fix script for all TOTW chapters."""
import re, glob, sys

# Exact heading replacements (old → new)
EXACT = {
    # Ch04
    '### He rba li st': '### Herbalist',
    '### Bron C Buster': '### Bronc Buster',
    '### L ucky': '### Lucky',
    "### Man S Best Friend": "### Man\u2019s Best Friend",
    '### P is to Leer': '### Pistoleer',
    '### Rabble Ro User': '### Rabble Rouser',
    '### Hay Maker': '### Haymaker',
    '### Light Footed': '### Light-Footed',
    '### Lock Picker': '### Lockpicker',
    # Ch05
    '### Sneak Attacks Ambushes': '### Sneak Attacks & Ambushes',
    '### Coup De Grace': '### Coup de Grace',
    # Ch06
    '### Creating your Com Padre': '### Creating Your Compadre',
    '### Your Com Padres in Play': '### Your Compadres in Play',
    '### a Note on Prices': '### A Note on Prices',
    "### Your Horse S Tackle": "### Your Horse\u2019s Tackle",
    '### Bron C Bustin': "### Bronc Bustin\u2019",
    '### Weapon Qualities Conditions': '### Weapon Qualities & Conditions',
    '### Weapon Conditions Ranged': '### Weapon Conditions (Ranged)',
    '### Weapon Conditions Melee': '### Weapon Conditions (Melee)',
    # Ch07
    # (none remaining)
    # Ch08
    '### L aw': '### Law',
    '### a Business in Action': '### A Business in Action',
    '### Creating a Dynasty': '### Creating a Dynasty',
    # Ch09
    '### a Brief History of New Mexico': '### A Brief History of New Mexico',
    "### King S People in Jorn Ada Springs": "### King\u2019s People in Jornada Springs",
    "### Don a Lmc Ginn": "### Dona McGinn",
    "### Marion Freeman and Jimmy H Arles Den": "### Marion Freeman and Jimmy Harlesden",
    "### King S People in Steaming Rock": "### King\u2019s People in Steaming Rock",
    "### Adventure 1 - Founder S Day": "### Adventure 1 - Founder\u2019s Day",
    "### Carson S Folly": "### Carson\u2019s Folly",
    "### King S People in Carson S Folly": "### King\u2019s People in Carson\u2019s Folly",
    "### Story 2 - for the Love of a Horse": "### Story 2 - For the Love of a Horse",
    "### The People of Carson S Folly": "### The People of Carson\u2019s Folly",
    "### Adventure 5- a Chip in the Big Game": "### Adventure 5 - A Chip in the Big Game",
    # Ch10
    "### Rockcliffe S Lie": "### Rockcliffe\u2019s Lie",
    "### If the Player Characters Save Patience and Reveal Rockcliffe S Lie": "### If the Player Characters Save Patience and Reveal Rockcliffe\u2019s Lie",
    "### What of the family you lef t behind?": "### What of the Family You Left Behind?",
    "### If You Have a Good Idea": "### If You Have a Good Idea",
}

# Regex heading replacements (pattern → replacement)
REGEX = [
    # Ch02 - attribution
    (r'^\> \u2014 F\.\s*S\s*C\s*O\s*T\s*T\s+F\s*ITZ\s*GE\s*R\s*ALD\s*$', '> \u2014 F. SCOTT FITZGERALD'),
    # Ch02 stat blocks - garbled age table header
    (r'^\*\*P\s*lay\s*er\s*C\s*h\s*a\s*r\s*ac\s*t\s*er\s+age\s+t\s*a\s*bl\s*e\s*-\*\*\s*C\s*h\s*o\s*o\s*se\s+yo\s*ur\s*age\s*:', '**Player Character Age Table** - Choose your age:'),
    # Ch03 - fragment heading
    (r'^### ing, make a PRESENCE roll\.\s*$', ''),
    # Ch05
    (r'^### Fa\s*st\s+Ac\s*t\s*ion\s*s\s*$', '### Fast Actions'),
    (r'^### c\s*on\s*fl\s*ic\s*t\s+mod\s*ific\s*at\s*ion\s*s\s*$', '### Conflict Modifications'),
    (r'^### O\s*ve\s*rw\s*at\s*ch\s*$', '### Overwatch'),
    (r'^### DAM\s*AGE\s*$', '### Damage'),
    (r'^### He\s*at\s*st\s*ro\s*ke\s*$', '### Heatstroke'),
    (r'^### Fi\s*re\s*$', '### Fire'),
    # Ch06
    (r'^### LIF\s*E\s+IN\s+TO\s*WN\s*$', '### Life in Town'),
    (r'^### Wh\s*at\s+do\s*y\s*ou\s+do\s*\?\s*$', '### What Do You Do?'),
    (r'^### SAL\s*AR\s*IE\s*S\s+IN\s+THE\s+O\s*LD\s+WE\s*ST\s*$', '### Salaries in the Old West'),
    (r'^### Wh\s*o\s*a\s*r\s*e\s+t\s*h\s*e\s*y\s*\?\s*$', '### Who Are They?'),
    (r'^### W\s*hat\s+a\s*r\s*e\s+t\s*h\s*e\s*i\s*r\s+at\s*t\s*r\s*i\s*b\s*u\s*t\s*es\s*\?\s*$', '### What Are Their Attributes?'),
    (r'^### W\s*h\s*at\s+a\s*re\s+t\s*h\s*e\s*i\s*r\s*a\s*bi\s*li\s*t\s*i\s*e\s*s\s*a\s*n\s*d\s+t\s*a\s*le\s*n\s*t\s*\?\s*$', '### What Are Their Abilities and Talent?'),
    (r'^### co\s*mpa\s*d\s*re\s*\u2019?s\s*pe\s*rso\s*n\s*a\s*li\s*t\s*y\?\s*$', "### Compadre\u2019s Personality?"),
    (r'^### What is your\s*$', ''),  # Remove orphan heading (merge with next)
    (r'^### W\s*h\s*at\s*\u2019?s\s*t\s*h\s*e\s*i\s*r\s*t\s*a\s*le\s*\?\s*$', "### What\u2019s Their Tale?"),
    (r'^### Ro\s*ll\s+t\s*h\s*e\s+d\s*e\s*a\s*l.*ca\s*rd\s*s\s*t\s*re\s*at.*yo\s*u\s*\?\s*$', '### Roll the Deal - How Are the Cards Treating You?'),
    (r'^### N\s*O\s+S\s*UC\s*C\s*E\s*S\s*S\s*E\s*S\s*\?\s*$', '### No Successes?'),
    (r'^### Th\s*e\s+n\s*e\s*x\s*t\s+se\s*ssi\s*o\s*n\s*\?\s*$', '### The Next Session?'),
    (r'^### C\s*HE\s*AT\s*IN\s*G\s*$', '### Cheating'),
    (r'^### P\s*l\s*ay\s*!\s*$', '### Play!'),
    (r'^### S\s*u\s*c\s*c\s*e\s*s\s*se\s*s\s*!\s*$', '### Successes!'),
    (r'^### Q\s*ua\s*li\s*ti\s*e\s*s\s*$', '### Qualities'),
    (r'^### R\s*O\s*D\s*E\s*O.*R\s*O\s*D\s*E\s*O.*WHE.*R\s*O\s*D\s*E\s*O\s*\?\s*$', '### Rodeo, Rodeo, Wherefore Art Thou, Rodeo?'),
    (r'^### TR\s*AC\s*KIN\s*G\s+IN\s+AC\s*TIO\s*N\s*$', '### Tracking in Action'),
    # Ch07
    (r'^### T\s*HE\s+L\s*AN\s*D\s*$', '### The Land'),
    # Ch08
    (r'^### WHIC\s*H\s*AS\s*PE\s*C\s*T\s*\?\s*$', '### Which Aspect?'),
    (r'^### W\s*h\s*e\s*n\s+d\s*o\s*e\s*s\s*t\s*h\s*e\s+se\s*a\s*so\s*n\s+t\s*urn\s*\?\s*$', '### When Does the Season Turn?'),
    (r'^### F\s*ORT\s*UN\s*E\s*S\s+IN\s+PL\s*AY\s*$', '### Fortunes in Play'),
    (r'^### C\s*AM\s*PAIGN\s+TALE\s*S\s*$', '### Campaign Tales'),
    (r'^### The Tall Tale of V\s*Ear\s*S\s*Vale\s*$', '### The Tall Tale of Vears Vale'),
    (r'^### W\s*H\s*AT\s+H\s*A\s*P\s*P\s*E\s*N\s*E\s*D\s+T\s*O\s+O\s*LD\s*P\s*O\s*S\s*S\s*UM\s+TAT\s*E\s*\?\s*$', '### What Happened to Old Possum Tate?'),
    (r'^### a little oasis amid the wilderness\.\s*$', ''),  # Fragment, not a real heading
    # Ch09
    (r'^### WHY\s+A\s*C\s*AM\s*PAIGN\s*F\s*R\s*AM\s*E\s*WO\s*R\s*K\s*\?\s*$', '### Why a Campaign Framework?'),
    (r'^### WHAT\s*\u2019?S\s+IN\s+T\s*HE\s+C\s*AM\s*PAIGN\s*$', "### What\u2019s in the Campaign"),
    (r'^### Adv\s*e\s*n\s*t\s*u\s*r\s*e\s+1\s+-\s*A\s*n\s+of\s*f\s*e\s*r\s*y\s*ou\s+c\s*a\s*n.*r\s*e\s*f\s*u\s*se\s*\?\s*$', "### Adventure 1 - An Offer You Can\u2019t Refuse?"),
    (r'^### St\s*o\s*ry\s+3\s+-\s*Wh\s*at\s+g\s*oe\s*s\s*a\s*r\s*ou\s*n\s*d.*$', '### Story 3 - What Goes Around...'),
    (r'^### E\s*mma\s+be\s*ck\s*$', '### Emma Beck'),
    (r'^### Adv\s*en\s*t\s*u\s*r\s*e\s+6\s+-\s*L\s*on\s*g\s+l\s*i\s*v\s*e\s+t\s*h\s*e\s+ki\s*n\s*g\s*\?\s*$', '### Adventure 6 - Long Live the King?'),
    # Ch10
    (r'^### W\s*e\s*l\s*c\s*om\s*e\s+t\s*o\s*n\s*e\s*w\s+m\s*e\s*x\s*i\s*c\s*o.*1\s*87\s*3\s*$', '### Welcome to New Mexico Territory, 1873'),
    (r'^### WHAT\s*IS\s+GO\s*IN\s*G\s*O\s*N\s*\?\s*$', '### What Is Going On?'),
    (r'^### T\s*H\s*E\s+S\s*E\s*CO\s*N\s*D\s+S\s*CE\s*N\s*E.*REQUE\s*S\s*T\s+F\s*R\s*O\s*M\s*A\s+F\s*R\s*I\s*E\s*N\s*D\s*\?\s*$', '### The Second Scene - A Request from a Friend?'),
    (r'^### A\s*P\s*P\s*END\s*I\s*X\s*:\s+YO\s*UR\s+TA\s*L\s*E\s+BE\s*GIN\s*S\s*$', '### Appendix: Your Tale Begins'),
    (r'^### Wh\s*o\s*a\s*r\s*e\s+y\s*ou\s*\?\s*$', '### Who Are You?'),
    (r'^### St\s*ep\s+1\s*:\s+Wh\s*e\s*r\s*e\s+w\s*e\s*r\s*e\s+y\s*ou\s+b\s*orn\s*\?\s*$', '### Step 1: Where Were You Born?'),
    (r'^### St\s*ep\s+2\s*:\s*Wh\s*at\s+w\s*a\s*s\s+y\s*ou\s*r\s+u\s*pb\s*r\s*i\s*n\s*gi\s*n\s*g\s*\?\s*$', '### Step 2: What Was Your Upbringing?'),
    (r'^### St\s*e\s*p\s+3\s*:\s*W\s*h\s*at\s+of\s+t\s*h\s*e\s+f\s*a\s*m\s*i\s*ly.*b\s*e\s*h\s*in\s*d\s*\?\s*$', '### Step 3: What of the Family You Left Behind?'),
    (r'^### St\s*e\s*p\s+4\s*:\s*Wh\s*at\s+did\s*y\s*ou\s+do\s*f\s*or\s+yo\s*ur\s*F\s*ir\s*s\s*t\s+L\s*iv\s*in\s*g\s*\?\s*$', '### Step 4: What Did You Do for Your First Living?'),
    (r'^### S\s*t\s*e\s*p\s*5\s*:\s+Yo\s*ur\s*ch\s*a\s*rac\s*t\s*e\s*r.*S\s*e\s*cond\s*L\s*i\s*vi\s*n\s*g\.\s*$', "### Step 5: Your Character\u2019s Second Living."),
    (r'^### S\s*t\s*e\s*p\s*6\s*:\s+Yo\s*ur\s*ch\s*a\s*rac\s*t\s*e\s*r.*Th\s*i\s*r\s*d\s*L\s*i\s*vi\s*n\s*g\.\s*$', "### Step 6: Your Character\u2019s Third Living."),
    (r'^### St\s*e\s*p\s*7\s*:\s+T\s*h\s*e\s+f\s*i\s*n\s*a\s*l\s+t\s*ou\s*c\s*h\s*e\s*s\.\s*$', '### Step 7: The Final Touches.'),
    (r'^### St\s*ep\s*8\s*:\s+Wh\s*at\s+is\s*y\s*ou\s*r\s+Fa\s*i\s*t\s*h\s*\?\s*$', '### Step 8: What Is Your Faith?'),
    (r'^### S\s*t\s*e\s*p\s*9\s*:\s+W\s*h\s*at\s+i\s*s\s*yo\s*ur\s*Bi\s*g\s*D\s*re\s*am\s*\?\s*$', '### Step 9: What Is Your Big Dream?'),
    (r'^### S\s*t\s*e\s*p\s*1\s*0\s*:\s+W\s*h\s*o\s+i\s*s\s*yo\s*ur\s*Pa\s*rd\s*n\s*e\s*r\s*\?\s*$', '### Step 10: Who Is Your Pardner?'),
    (r'^### W\s*h\s*e\s*r\s*e\s+w\s*e\s*r\s*e\s+y\s*ou\s+b\s*or\s*n\s*\?\s*$', '### Where Were You Born?'),
    (r'^### W\s*hat\s+w\s*a\s*s\s*y\s*ou\s*r\s+u\s*pb\s*r\s*i\s*n\s*gi\s*n\s*g\s*\?\s*$', '### What Was Your Upbringing?'),
    (r'^### Finding a Living\s*$', '### Finding a Living'),
    (r'^### Yo\s*ur\s*f\s*i\s*rst\s+li\s*vi\s*n\s*g.*yo\s*un\s*gst\s*e\s*r\s*\?\s*$', '### Your First Living - What Did You Do as a Youngster?'),
    (r'^### Yo\s*ur\s*s\s*e\s*c\s*on\s*d\s*l\s*iv\s*in\s*g.*20\s*s\s+a\s*n\s*d\s*3\s*0\s*s\s*\?\s*$', '### Your Second Living - What Did You Do in Your 20s and 30s?'),
    (r'^### A\s*t\s*hi\s*rd\s*a\s*n\s*d\s*f\s*in\s*a\s*l\s+l\s*iv\s*in\s*g.*pl\s*ay\s*\?\s*$', '### A Third and Final Living Before Starting Play?'),
    (r'^### Wh\s*at\s+i\s*s\s*y\s*ou\s*r\s+f\s*a\s*i\s*t\s*h\s*\?\s*$', '### What Is Your Faith?'),
    (r'^### W\s*h\s*at\s+i\s*s\s*yo\s*ur\s*bi\s*g\s*d\s*re\s*a\s*m\s*\?\s*$', '### What Is Your Big Dream?'),
    (r'^### W\s*h\s*o\s+i\s*s\s*yo\s*ur\s*pa\s*rd\s*n\s*e\s*r\s*\?\s*$', '### Who Is Your Pardner?'),
    (r'^### W\s*h\s*o\s+a\s*re\s+yo\s*u.*w\s*h\s*at\s*d\s*o\s+yo\s*u\s*l\s*o\s*o\s*k\s*li\s*ke\s*\?\s*$', '### Who Are You, and What Do You Look Like?'),
    # Ch10 - Grifter was pre-fixed, but search for Outlaw pattern
    (r'^### Gr\s*If\s*Ter\s*$', '### Grifter'),
]

total = 0
for fn in sorted(glob.glob('*.md')):
    data = open(fn, 'r', encoding='utf-8').read()
    changes = 0

    # Exact replacements
    for old, new in EXACT.items():
        if old in data:
            data = data.replace(old, new)
            changes += 1
            print(f'  {fn}: exact: {old!r} -> {new!r}')

    # Regex replacements (line by line)
    lines = data.split('\n')
    for i, line in enumerate(lines):
        if not line.startswith('###'):
            # Also check attributions
            if line.startswith('> '):
                for pattern, replacement in REGEX:
                    if re.match(pattern, line):
                        print(f'  {fn}:{i+1}: regex: {line!r} -> {replacement!r}')
                        lines[i] = replacement
                        changes += 1
                        break
            continue
        for pattern, replacement in REGEX:
            if re.match(pattern, line, re.IGNORECASE):
                if replacement == '':
                    # Remove the heading line entirely (it's a fragment)
                    print(f'  {fn}:{i+1}: REMOVE: {line!r}')
                else:
                    print(f'  {fn}:{i+1}: regex: {line!r} -> {replacement!r}')
                lines[i] = replacement
                changes += 1
                break

    data = '\n'.join(lines)

    # Clean up empty lines left by removed headings
    while '\n\n\n' in data:
        data = data.replace('\n\n\n', '\n\n')

    if changes > 0:
        open(fn, 'w', encoding='utf-8').write(data)
        print(f'{fn}: {changes} fixes applied')
        total += changes

print(f'\nTotal: {total} fixes across all files')
