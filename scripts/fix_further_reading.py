"""
Convert the Further Reading section in Ch07 from a wall of space-separated
entries into a bullet-point list. The two blobs of text (before and after
States of the West) are both reformatted. The second blob is also moved
to sit under Further Reading so the section is contiguous.
"""

import re

filepath = r'c:\git-public\Tales-of-the-Old-West-2e\corebook\07-the-west-in-the-1870s.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# ── Blob 1: everything between "### Further Reading\n\n" and "\n\n### States"
blob1_raw = (
    "_The Cheyenne Indians_ by George Bird Grinnell "
    "_Bury My Heart at Wounded Knee_ by Dee Brown "
    "_Blood and Thunder_ by Hampton Sides "
    "_Empire of the Summer Moon_ by S.C. Gwynne "
    "_The Real Deadwood_ by John Edward Ames "
    "_Dodge City_ by Tom Clavin "
    "_Gunfighters, Highwaymen and Vigilantes_ by Roger D. McGrath "
    "_The Worst Hard Time_ by Timothy Egan "
    "_Lonesome Dove_ by Larry McMurtry _(fiction, but more honest about cowboy life than most history books)_ "
    "_Roughing It_ by Mark Twain "
    "_Killers of the Flower Moon_ by David Grann "
    "_The Indifferent Stars Above_ by Daniel James Brown _(on the Donner Party)_ "
    "_Massacre at Mountain Meadows_ by Walker, Turley, and Leonard "
    "_One Vast Winter Count_ by Colin G. Calloway "
    "_Driven Out_ by Jean Pfaelzer _(on anti-Chinese violence)_ "
    "_The Devil in the White City_ by Erik Larson _(Gilded Age context)_ "
    "_Slavery by Another Name_ by Douglas A. Blackmon _(on convict leasing)_ "
    "_1491_ by Charles C. Mann "
    "_Impressions of an Indian Childhood_ by Zitkala Sa "
    "_The Earth is Weeping_ by Peter Cozzens "
    "_Black Elk Speaks_ as told through John Neihardt by Nicholas Black Elk "
    "_The Rediscovery of America_ by Ned Blackhawk "
    "_And Still The Waters Run_ by Angie Debo "
    "_The Mammoth Book of Native Americans_ edited by Jon E. Lewis "
    "_New Mexico, A History_ by Sanchez, Spude and Gomez"
)

# ── Blob 2: the orphaned paragraph after States of the West
blob2_raw = (
    "_The Historical Atlas of Native Americans_ by Dr. Ian Barnes "
    "_River of Blood_ edited by Richard Cahan & Michael Williams "
    "_American Slavery_ by Peter Kolchin "
    "_Uncle Tom\u2019s Story of His Life_ \u2014An Autobiography of Reverend Josiah Henson by Josiah Henson "
    "_Black Cowboys in the American West_ edited by Glasrud and Searles "
    "_The Wild West_ by Frederick Nolan "
    "_Cult of Glory\u2014the Bold and Brutal History of the Texas Rangers_ by Doug J. Swanson "
    "_Mexicanos_ by Manuel G Gonzalez "
    "The Cherokee Nation Youtube: https://www. youtube.com/channel/UCRX-8MCNvhzPMejv4oi_FRA"
)

def blob_to_bullets(blob):
    # Split on a space that precedes a new entry.
    # New entries start with: _Capital, _1 (for _1491_), or "The " (non-italic)
    parts = re.split(r' (?=_[A-Z1]|The [A-Z])', blob)
    return '\n'.join(f'- {p.strip()}' for p in parts if p.strip())

blob1_bullets = blob_to_bullets(blob1_raw)
blob2_bullets = blob_to_bullets(blob2_raw)

all_bullets = blob1_bullets + '\n' + blob2_bullets

# ── Build the new Further Reading + States of the West block ─────────────────
old_block = (
    "### Further Reading\n\n"
    + blob1_raw
    + "\n\n### States of the West\n\n"
    "> _And their dates of incorporation: \u2022 Texas\u20141845 \u2022 California\u20141850 \u2022 Oregon\u20141859 \u2022 Kansas\u20141861 \u2022 Nevada\u20141864 \u2022 Nebraska\u20141867 \u2022 Colorado\u20141876 \u2022 Dakota\u20141889 \u2022 Montana\u20141889 \u2022 Washington State\u20141889 \u2022 Idaho\u20141890 \u2022 Wyoming\u20141890 \u2022 Utah\u20141896 \u2022 Oklahoma\u20141907 \u2022 Arizona\u20141912 \u2022 New Mexico\u20141912_"
    "\n\n"
    + blob2_raw
)

new_block = (
    "### Further Reading\n\n"
    + all_bullets
    + "\n\n### States of the West\n\n"
    "> _And their dates of incorporation: \u2022 Texas\u20141845 \u2022 California\u20141850 \u2022 Oregon\u20141859 \u2022 Kansas\u20141861 \u2022 Nevada\u20141864 \u2022 Nebraska\u20141867 \u2022 Colorado\u20141876 \u2022 Dakota\u20141889 \u2022 Montana\u20141889 \u2022 Washington State\u20141889 \u2022 Idaho\u20141890 \u2022 Wyoming\u20141890 \u2022 Utah\u20141896 \u2022 Oklahoma\u20141907 \u2022 Arizona\u20141912 \u2022 New Mexico\u20141912_"
)

if old_block not in content:
    # Try to find the actual text in the file for debugging
    idx = content.find("### Further Reading")
    print("=== ACTUAL TEXT FROM FILE (250 chars after marker) ===")
    print(repr(content[idx:idx+500]))
    raise ValueError("old_block not found — check the repr above for differences")

content_new = content.replace(old_block, new_block, 1)
content_new = re.sub(r'\n{3,}', '\n\n', content_new)

with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content_new)

print(f"Done. {len(content):,} -> {len(content_new):,} chars")
print("\n--- Preview of Further Reading section ---")
idx = content_new.find("### Further Reading")
print(content_new[idx:idx+1200])
