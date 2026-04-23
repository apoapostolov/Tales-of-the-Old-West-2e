import re

def clean_anti_ai(text):
    # Rule: Hard, plain, concrete sentences. Kill adverbs. No signposting.
    reps = [
        # AI meta commentary / signposting
        (r"This distinction matters to a campaign because [^\.]+\.\s*", ""),
        (r"The action is broadly linear\.\s*", "The column goes one direction. "),
        (r"The shape is firm, but it should never feel locked\.\s*", "The events are tight but not locked. "),
        (r"This is one of the best places for the party itself to crack by motive\.\s*", ""),
        (r"The best thing about this offer is that a player can defend taking it without ever thinking himself the villain of the chapter\.\s*", "A player takes it and justifies it. "),
        (r"Do not hide the chapter behind one successful roll\.\s*", "One failed roll does not end the chapter. "),
        (r"Do not underestimate how destructive players can be at a fork\.\s*", ""),
        (r"This opening arc should take time\.\s*", "Let the opening breathe. "),
        (r"Keep this chapter hard and specific\.\s*", ""),
        (r"That is enough\. The larger truth will show itself\.\s*", ""),
        (r"This is where the party should begin asking itself harder questions\.\s*", ""),
        (r"The broad rhythm is straightforward\.\s*", ""),
        (r"\bOn the surface, this is an escort-and-survey job\.\s*", "The visible task is escort and survey. "),

        # Clichés
        (r"\bvery\b\s+", ""),
        (r"\bsuddenly\b\s+", ""),
        (r"\bextremely\b\s+", ""),
        (r"\bmenacingly\b\s+", ""),

        # Make description concrete
        (r"handsome in the polished cavalry way", "polished like cavalry brass"),
        (r"The first impression he gives is of order held together by temper\.", "He is order held up by temper."),
        (r"The first impression is steadiness\.", "He is steady."),
        (r"The first impression is smoothness\.", "He is smooth."),
        (r"The first impression is practical force\.", "He is practical force."),
        (r"The first impression she leaves is self-possession\.", "She holds her own ground."),
        (r"The first impression is calm attention\.", "He gives calm attention."),

        # Dialogue blocks
        (r"Captain Rowe asks for more regular troops and was refused\.", "Rowe asked for regular troops. Washington refused him."),

        # Remove "furthermore", "moreover" etc
        (r"\bFurthermore, \b", ""),
        (r"\bMoreover, \b", ""),
        (r"\bIn conclusion, \b", ""),
        (r"\bIt is important to note that \b", ""),
        (r"\bAs such, \b", ""),

        # Kill empty adjectives
        (r"\brugged\b\s*", ""),

    ]

    for old, new in reps:
        text = re.sub(old, new, text)

    return text

with open("supplement-2-montana-campaign/book-content/02-the-yellowstone-line.md", "r", encoding="utf-8") as f:
    original = f.read()

revised = clean_anti_ai(original)

with open("supplement-2-montana-campaign/book-content/02-the-yellowstone-line.md", "w", encoding="utf-8") as f:
    f.write(revised)
