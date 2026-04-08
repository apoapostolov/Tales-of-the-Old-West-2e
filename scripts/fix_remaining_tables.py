#!/usr/bin/env python3
"""Fix all remaining garbled tables in Ch08 and Ch10."""
import re, sys, os

BASE = r"c:\git-public\Tales-of-the-Old-West-2e\corebook"

def read(fn):
    with open(os.path.join(BASE, fn), "r", encoding="utf-8") as f:
        return f.read()

def write(fn, content):
    with open(os.path.join(BASE, fn), "w", encoding="utf-8") as f:
        f.write(content)

def fix_ch08():
    c = read("08-campaigns-in-the-old-west.md")
    changes = 0

    # === 1. Seasonal Lifestyle Table ===
    old_lifestyle = (
        '| Seasonal Lifestyle Table Cost Modifier Modifier '
        'DESTITUTE: You have nothing, you want nothing, it costs you $0 0 \u22123 '
        'nothing. You may have a hovel or a tent to sleep in but you\u2019re '
        'little more than a vagrant. You hunt and gather (or steal) to eat, '
        'occasionally scrap- ing up the coin to have a bath and get your clothes '
        'laundered. But not often. Most good folk look down on you, if they even '
        'notice you at all. VERY POOR: You try your best but you have little. '
        'A small cabin $50 0 \u22122 maybe, that needs (or gets) little care. '
        'You have no extravagance in your life at all. Surviving is all you can '
        'manage, and that\u2019s not always a surety. Your clothes are threadbare. '
        'They smell too. You eat the most basic foods, all you can afford. '
        'SCRAPING BY: You aren\u2019t on the poverty line but you have no swag- '
        '$100 0 \u22121 ger, no pretense at any kind of an easy life. Every day '
        'is a struggle, and while you might think you\u2019re respectable, you '
        'aren\u2019t really respected. You\u2019re still just too poor. '
        'MANAGING: You are doing ok, if not well. You have enough to eat '
        '| Fame | Reputation |\n'
        '| --- | --- | --- |\n'
        '| and your clothes, if a little threadbare, are of sufficient quality '
        'to keep you warm, cool and dry. Your home is as good as all the other '
        'normal folk, and you live a decent, if simple, life. COMFORTABLE: You '
        'have good clothes, decent food, and you | $150 0 0 |  |\n'
        '| never run out of firewood. Your home is nicely appointed and the good '
        'people nod hello to you in the street. You are respectable. You might '
        'even get asked your opinion on civic matters, but not always. And they '
        'don\u2019t always listen to your view. WELL-OFF: Your lifestyle is opulent '
        'compared to everyone else in $350 +2 +2 the town. You wear the best '
        'quality clothes, you buy the best food from the stalls and markets, '
        'you have your place in the best saloon in town. Everyone knows who you '
        'are. They all nod good morning, and your opinion is sought. RICH: You '
        'are the best of the best. You are so rich that nothing both- $500 +4 +3 '
        'ers you. Everyone in town knows who you are and nothing is decided '
        'without your view being sought. They are all envious, and would gladly '
        'do anything to swap places with you. People of your caliber run the '
        'world, and you want to keep it that way. | $200 +1 +1 |  |'
    )

    new_lifestyle = """| Lifestyle | Cost | Fame | Reputation |
| --- | --- | --- | --- |
| **DESTITUTE:** You have nothing, you want nothing, it costs you nothing. You may have a hovel or a tent to sleep in but you\u2019re little more than a vagrant. You hunt and gather (or steal) to eat, occasionally scraping up the coin to have a bath and get your clothes laundered. But not often. Most good folk look down on you, if they even notice you at all. | $0 | 0 | \u22123 |
| **VERY POOR:** You try your best but you have little. A small cabin maybe, that needs (or gets) little care. You have no extravagance in your life at all. Surviving is all you can manage, and that\u2019s not always a surety. Your clothes are threadbare. They smell too. You eat the most basic foods, all you can afford. | $50 | 0 | \u22122 |
| **SCRAPING BY:** You aren\u2019t on the poverty line but you have no swagger, no pretense at any kind of an easy life. Every day is a struggle, and while you might think you\u2019re respectable, you aren\u2019t really respected. You\u2019re still just too poor. | $100 | 0 | \u22121 |
| **MANAGING:** You are doing ok, if not well. You have enough to eat and your clothes, if a little threadbare, are of sufficient quality to keep you warm, cool and dry. Your home is as good as all the other normal folk, and you live a decent, if simple, life. | $150 | 0 | 0 |
| **COMFORTABLE:** You have good clothes, decent food, and you never run out of firewood. Your home is nicely appointed and the good people nod hello to you in the street. You are respectable. You might even get asked your opinion on civic matters, but not always. And they don\u2019t always listen to your view. | $200 | +1 | +1 |
| **WELL-OFF:** Your lifestyle is opulent compared to everyone else in the town. You wear the best quality clothes, you buy the best food from the stalls and markets, you have your place in the best saloon in town. Everyone knows who you are. They all nod good morning, and your opinion is sought. | $350 | +2 | +2 |
| **RICH:** You are the best of the best. You are so rich that nothing bothers you. Everyone in town knows who you are and nothing is decided without your view being sought. They are all envious, and would gladly do anything to swap places with you. People of your caliber run the world, and you want to keep it that way. | $500 | +4 | +3 |"""

    if old_lifestyle in c:
        c = c.replace(old_lifestyle, new_lifestyle)
        changes += 1
        print("  [OK] Seasonal Lifestyle Table")
    else:
        # Try a regex approach - find from "| Seasonal Lifestyle" to "$200 +1 +1 |  |"
        pat = re.compile(
            r'\| Seasonal Lifestyle Table.*?\| \$200 \+1 \+1 \|  \|',
            re.DOTALL
        )
        m = pat.search(c)
        if m:
            c = c[:m.start()] + new_lifestyle + c[m.end():]
            changes += 1
            print("  [OK] Seasonal Lifestyle Table (regex)")
        else:
            print("  [SKIP] Seasonal Lifestyle Table - not found")

    # === 2. Town Fortune Roll Modifier ===
    old_modifier = (
        "Prosperity Modification to the town fortune roll "
        "10 or less -2 to Tens die "
        "11 to 14 -1 to Tens die "
        "15 to 18 -3 to Unit die (to a minimum of 1)\n"
        "24 to 27 +3 to Unit die (to a maximum of 6)\n"
        "28 to 31 +1 to Tens die "
        "32 or more +2 to Tens die"
    )

    new_modifier = """| Prosperity | Modification |
| --- | --- |
| 10 or less | \u22122 to Tens die |
| 11 to 14 | \u22121 to Tens die |
| 15 to 18 | \u22123 to Unit die (to a minimum of 1) |
| 19 to 23 | No modification |
| 24 to 27 | +3 to Unit die (to a maximum of 6) |
| 28 to 31 | +1 to Tens die |
| 32 or more | +2 to Tens die |"""

    if old_modifier in c:
        c = c.replace(old_modifier, new_modifier)
        changes += 1
        print("  [OK] Town Fortune Roll Modifier")
    else:
        print("  [SKIP] Town Fortune Roll Modifier - not found")

    # === 3. Personal Fortunes - Fix merged entries and section headers ===
    # Fix entry 11/12 merger - "11 Calamity! 12 Broken Hearts" should be two rows
    old_1112 = (
        "| 11 Calamity! "
        "12 Broken Hearts - Someone you love deeply loves you no more. "
        "This should be a romantic lover or a close friend. They spurn your "
        "affections. Have they just fallen out of love, or have you done "
        "something to drive them away? Have they been unfaithful, or lured "
        "by the affections of another? The GM decides. "
        "| - Roll D66 again, but the Tens die result is automatically 0. |"
    )
    new_1112 = (
        "| 11 | Calamity! - Roll D66 again, but the Tens die result is automatically 0. |\n"
        "| 12 | Broken Hearts - Someone you love deeply loves you no more. "
        "This should be a romantic lover or a close friend. They spurn your "
        "affections. Have they just fallen out of love, or have you done "
        "something to drive them away? Have they been unfaithful, or lured "
        "by the affections of another? The GM decides. |"
    )
    if old_1112 in c:
        c = c.replace(old_1112, new_1112)
        changes += 1
        print("  [OK] Personal Fortunes 11/12 split")
    else:
        print("  [SKIP] Personal Fortunes 11/12 - not found")

    # Fix entry 24/25 merger
    old_2425 = (
        "| 24 Leaking Roof "
        "wind and rain is now getting in. Pay $3D6 and get it fixed, or "
        "something inside is ruined by the rain (GM to decide). People sneer "
        "at your lack of attention, and whisper that if this is how you present "
        "your home what does it say about the kind of person you are? 25 "
        "| - You know that work you\u2019ve been putting off? Well, it\u2019s "
        "come back to bite you and the |"
    )
    new_2425 = (
        "| 24 | Leaking Roof - You know that work you\u2019ve been putting off? "
        "Well, it\u2019s come back to bite you and the wind and rain is now getting in. "
        "Pay $3D6 and get it fixed, or something inside is ruined by the rain "
        "(GM to decide). People sneer at your lack of attention, and whisper "
        "that if this is how you present your home what does it say about "
        "the kind of person you are? |"
    )
    if old_2425 in c:
        c = c.replace(old_2425, new_2425)
        changes += 1
        print("  [OK] Personal Fortunes 24/25 split")
    else:
        print("  [SKIP] Personal Fortunes 24/25 - not found")

    # Now fix entry 25 which should be a separate row after 24
    # After replacing 24, we need to add entry 25 back
    # Entry 25 text: "More Than Just a Spring Clean"
    old_25 = (
        "More Than Just a Spring Clean "
        "needs a complete overhaul to keep it spick and span. Spend "
        "2D6 \u00d7 $10 by the end of the season to fix it all up, or your "
        "home\u2019s Status is reduced by 1. "
        "| - The wind has battered your home and your windows are rattling. It |"
    )
    new_25 = (
        "| 25 | More Than Just a Spring Clean - The wind has battered your home "
        "and your windows are rattling. It needs a complete overhaul to keep "
        "it spick and span. Spend 2D6 \u00d7 $10 by the end of the season to "
        "fix it all up, or your home\u2019s Status is reduced by 1. |"
    )
    if old_25 in c:
        c = c.replace(old_25, new_25)
        changes += 1
        print("  [OK] Personal Fortunes 25 fix")
    else:
        print("  [SKIP] Personal Fortunes 25 - not found")

    # Fix entry 34/35 merger
    old_3435 = (
        "| 34 Argumentative "
        "with someone, or stressed about something, and you\u2019ve taken it "
        "out on others. 35 "
        "| - You have let your temper get the better of you one time too often. "
        "Maybe you\u2019re angry |"
    )
    new_3435 = (
        "| 34 | Argumentative - You have let your temper get the better of "
        "you one time too often. Maybe you\u2019re angry with someone, or stressed "
        "about something, and you\u2019ve taken it out on others. |"
    )
    if old_3435 in c:
        c = c.replace(old_3435, new_3435)
        changes += 1
        print("  [OK] Personal Fortunes 34/35 split")
    else:
        print("  [SKIP] Personal Fortunes 34/35 - not found")

    # Now fix entry 35 which should be its own row
    old_35 = (
        "Brush With The Law "
        "compadre. Are they in trouble, suspected of a crime, or are they in "
        "danger from someone else? "
        "| - A sheriff or marshal from out of town turns up, looking for a "
        "family member or |"
    )
    new_35 = (
        "| 35 | Brush With The Law - A sheriff or marshal from out of town "
        "turns up, looking for a family member or compadre. Are they in trouble, "
        "suspected of a crime, or are they in danger from someone else? |"
    )
    if old_35 in c:
        c = c.replace(old_35, new_35)
        changes += 1
        print("  [OK] Personal Fortunes 35 fix")
    else:
        print("  [SKIP] Personal Fortunes 35 - not found")

    # Fix entry 41/42 merger
    old_4142 = (
        "| 41 A Helping Hand "
        "This reputation may or may not be well deserved, but either way "
        "you get a lot of friendly slaps on the back. "
        "42 Peacemaker - You break up a bar fight that was getting nasty, "
        "and have gained greater respect from the locals. How those who "
        "were fighting feel about your intervention, and who they are, "
        "is another matter. "
        "| - You were seen to get involved in recent town festivals, and "
        "people think you\u2019re a good sort. |"
    )
    new_4142 = (
        "| 41 | A Helping Hand - You were seen to get involved in recent "
        "town festivals, and people think you\u2019re a good sort. This reputation "
        "may or may not be well deserved, but either way you get a lot of "
        "friendly slaps on the back. |\n"
        "| 42 | Peacemaker - You break up a bar fight that was getting nasty, "
        "and have gained greater respect from the locals. How those who were "
        "fighting feel about your intervention, and who they are, is another "
        "matter. |"
    )
    if old_4142 in c:
        c = c.replace(old_4142, new_4142)
        changes += 1
        print("  [OK] Personal Fortunes 41/42 split")
    else:
        print("  [SKIP] Personal Fortunes 41/42 - not found")

    # Fix section 3 header that has entry 51 merged in
    old_51hdr = (
        "| D66 Personal Fortunes "
        "51 Love Blossoms - Someone has expressed their love for you. "
        "It might be an old flame or someone new. It might be welcome or "
        "a complete pain in the ass. But nonetheless, this person seems "
        "to love you. |  |\n"
        "| --- | --- |"
    )
    new_51hdr = (
        "| D66 | Personal Fortunes |\n"
        "| --- | --- |\n"
        "| 51 | Love Blossoms - Someone has expressed their love for you. "
        "It might be an old flame or someone new. It might be welcome or "
        "a complete pain in the ass. But nonetheless, this person seems "
        "to love you. |"
    )
    if old_51hdr in c:
        c = c.replace(old_51hdr, new_51hdr)
        changes += 1
        print("  [OK] Personal Fortunes section 3 header/51")
    else:
        print("  [SKIP] Personal Fortunes section 3 header/51 - not found")

    # Fix all remaining Personal Fortunes entries that have D66 number embedded
    # Pattern: "| 03 A Rival is Dead ger of blame..." -> "| 03 | A Rival is Dead..."
    # Fix entries where D66 and description are in wrong columns
    pf_fixes = [
        # Entries where description text leaked into description column
        ("| 01 Death in the Family | - A family tragedy. |",
         "| 01 | Death in the Family - A family tragedy. |"),
        ("| 02 A Friend is Dead | - Someone close or important to you is found dead. |",
         "| 02 | A Friend is Dead - Someone close or important to you is found dead. |"),
        ("| 03 A Rival is Dead ger of blame will inevitably point your way. circumstances. The fin | - Someone you have crossed, an enemy or a rival, has been found dead under suspicious |",
         "| 03 | A Rival is Dead - Someone you have crossed, an enemy or a rival, has been found dead under suspicious circumstances. The finger of blame will inevitably point your way. |"),
        ("| 04 Disease in the Family hangs in the balance. | - A family member or compadre is seriously ill. They are not dead yet, but their life |",
         "| 04 | Disease in the Family - A family member or compadre is seriously ill. They are not dead yet, but their life hangs in the balance. |"),
        ("| 05 Scandal one, or just sleeping with the wrong p erson. The GM decides. | - Someone close to you has disgraced you and your name. It might be a criminal act, or a beastly |",
         "| 05 | Scandal - Someone close to you has disgraced you and your name. It might be a criminal act, or a beastly one, or just sleeping with the wrong person. The GM decides. |"),
        ("| 06 Gossip in Town your Reputation moves 3 steps in a negative direction (at the GM\u2019s discretion). | - People have been gossiping about you, and it\u2019s not good. Your Fame increases by 1, but |",
         "| 06 | Gossip in Town - People have been gossiping about you, and it\u2019s not good. Your Fame increases by 1, but your Reputation moves 3 steps in a negative direction (at the GM\u2019s discretion). |"),
        ("| 13 Contested Property mands you hand it over. It might be a family heirloom, a house or property, a claim to a mine, or an exp person has a strong claim, and others believe them. ensive animal. This | - Someone claims ownership of a much beloved or valuable possession, and de- |",
         "| 13 | Contested Property - Someone claims ownership of a much beloved or valuable possession, and demands you hand it over. It might be a family heirloom, a house or property, a claim to a mine, or an expensive animal. This person has a strong claim, and others believe them. |"),
        ("| 14 Terrible Illness y lose 1 point from a random attribute. contracted it. The | - One of your compadres gets very ill\u2014the GM decides on the disease and how they |",
         "| 14 | Terrible Illness - One of your compadres gets very ill\u2014the GM decides on the disease and how they contracted it. They lose 1 point from a random attribute. |"),
        ("| 15 Loyalty? why). They might make life a misery for you, or even leave your side, unless you can identify and resolve this problem. | - A random compadre becomes disillusioned with you or otherwise unhappy (the GM decides |",
         "| 15 | Loyalty? - A random compadre becomes disillusioned with you or otherwise unhappy (the GM decides why). They might make life a misery for you, or even leave your side, unless you can identify and resolve this problem. |"),
        ("| 16 Rabid Animal responsible. The town is angry, and the family of the victim is out for blood\u2014maybe your animal\u2019s, maybe yours, perhaps both. | - Someone has been killed in town, and it seems your horse, dog, or other animal was |",
         "| 16 | Rabid Animal - Someone has been killed in town, and it seems your horse, dog, or other animal was responsible. The town is angry, and the family of the victim is out for blood\u2014maybe your animal\u2019s, maybe yours, perhaps both. |"),
        ("| 21 Your Animal Companion Dies accident, illness or old age, or do you suspect that someone who hates you killed the animal out of spite? The GM decides. | - Your horse, dog, or other animal (not livestock) dies. This may be an |",
         "| 21 | Your Animal Companion Dies - Your horse, dog, or other animal (not livestock) dies. This may be an accident, illness or old age, or do you suspect that someone who hates you killed the animal out of spite? The GM decides. |"),
        ("| 22 Lost Something to someone else, but losing it is a very bad thing. It could just be a loss of cash (3D6 \u00d7 $10), maybe money you were collecting from the town for a club or the church fund. Decide with the GM which. | - You misplace something important, or has it been stolen? It might be yours or belong |",
         "| 22 | Lost Something - You misplace something important, or has it been stolen? It might be yours or belong to someone else, but losing it is a very bad thing. It could just be a loss of cash (3D6 \u00d7 $10), maybe money you were collecting from the town for a club or the church fund. Decide with the GM which. |"),
        ("| 23 A Friend No More than one. It could be a natural death, illness or accident, or maybe there were suspicious circumstances? | - One of your compadres or employees will die. Choose randomly if there is more |",
         "| 23 | A Friend No More - One of your compadres or employees will die. Choose randomly if there is more than one. It could be a natural death, illness or accident, or maybe there were suspicious circumstances? |"),
        ("| 26 Idle Chatter a negative direction. | - People have been gossiping about you, and it\u2019s not good. Your Reputation moves 1 step in |",
         "| 26 | Idle Chatter - People have been gossiping about you, and it\u2019s not good. Your Reputation moves 1 step in a negative direction. |"),
        ("| 31 A New Enemy be a complete mystery to you. But nonetheless, someone about town is bad-mouthing you. | - For some reason someone has taken a dislike to you. You may know for why, or it might |",
         "| 31 | A New Enemy - For some reason someone has taken a dislike to you. You may know for why, or it might be a complete mystery to you. But nonetheless, someone about town is bad-mouthing you. |"),
        ("| 32 Scarred / Marked have fallen out, or gone white prematurely, or you are pock-marked or visibly scarred. People look at you y now\u2014is this a bad omen? differentl | - You survive an illness or minor accident, but you\u2019ve been left marked. Your hair may |",
         "| 32 | Scarred / Marked - You survive an illness or minor accident, but you\u2019ve been left marked. Your hair may have fallen out, or gone white prematurely, or you are pock-marked or visibly scarred. People look at you differently now\u2014is this a bad omen? |"),
        ("| 33 Mistaken Identity? and people can\u2019t help but tar you with the same brush. | - You bear a passing resemblance to someone disliked, notorious or even outlawed, |",
         "| 33 | Mistaken Identity? - You bear a passing resemblance to someone disliked, notorious or even outlawed, and people can\u2019t help but tar you with the same brush. |"),
        ("| 36 Helping the Law outlaw or outlaw gang, and can give information to help apprehend them. The marshal might be right, or perhaps not. What do you do, and how can you convince the marshal you\u2019re not hiding something? | - A marshal arrives in town and seeks you out, certain you are an associate of a wanted |",
         "| 36 | Helping the Law - A marshal arrives in town and seeks you out, certain you are an associate of a wanted outlaw or outlaw gang, and can give information to help apprehend them. The marshal might be right, or perhaps not. What do you do, and how can you convince the marshal you\u2019re not hiding something? |"),
        ("| 43 Good Samaritan choice to risk yourself to save them, or leave them to their fates. What do you decide? | - You get the chance to rescue some strangers from a terrible danger. You have the |",
         "| 43 | Good Samaritan - You get the chance to rescue some strangers from a terrible danger. You have the choice to risk yourself to save them, or leave them to their fates. What do you decide? |"),
        ("| 44 Idle Banter | - You are being talked about in town, and people are saying nice things. Gain +1 Reputation. |",
         "| 44 | Idle Banter - You are being talked about in town, and people are saying nice things. Gain +1 Reputation. |"),
        ("| 45 An Exciting Find get of ore, a special plant, $2D6 in ancient coins, a young animal pup, etc). Agree with the GM what it is. | - You find something that you like, want or find exciting. It could be anything (a nug- |",
         "| 45 | An Exciting Find - You find something that you like, want or find exciting. It could be anything (a nugget of ore, a special plant, $2D6 in ancient coins, a young animal pup, etc). Agree with the GM what it is. |"),
        ("| 46 A Friend in a High Place should decide who this is, and why they are taking notice of you. | - Someone important takes notice of you for some reason. The player and GM |",
         "| 46 | A Friend in a High Place - Someone important takes notice of you for some reason. The player and GM should decide who this is, and why they are taking notice of you. |"),
        ("| 52 An Unexpected Legacy deeds to some unlikely claim, or a family heirloom or treasure. The GM decides. | - You have been left a legacy from an unexpected source. It may be money or title |",
         "| 52 | An Unexpected Legacy - You have been left a legacy from an unexpected source. It may be money or title deeds to some unlikely claim, or a family heirloom or treasure. The GM decides. |"),
        ("| 53 Hard working respectful nods in the street. | - You work hard at whatever it is you do with your time, and people have noticed. You get |",
         "| 53 | Hard working - You work hard at whatever it is you do with your time, and people have noticed. You get respectful nods in the street. |"),
        ("| 54 Touched by God People in the town are saying that you\u2019re touched by the Lord Almighty, and the angels are watching over you. | - You escape a near-miss accident or suffer lightly from what should be a terrible illness. |",
         "| 54 | Touched by God - You escape a near-miss accident or suffer lightly from what should be a terrible illness. People in the town are saying that you\u2019re touched by the Lord Almighty, and the angels are watching over you. |"),
        ("| 55 Handy with a Hammer passers-by. Maybe it\u2019ll bring good things, or even work your way. | - Your place is beautifully kept and draws the positive attention of visitors and |",
         "| 55 | Handy with a Hammer - Your place is beautifully kept and draws the positive attention of visitors and passers-by. Maybe it\u2019ll bring good things, or even work your way. |"),
        ("| 56 Frisky Animals birth, or someone has given you a gift of a new animal. | - You gain a new horse, dog, or other animal. An animal you already own may have given |",
         "| 56 | Frisky Animals - You gain a new horse, dog, or other animal. An animal you already own may have given birth, or someone has given you a gift of a new animal. |"),
        ("| 61 A Miraculous Rescue wolves or mountain lions. Their courage reflects well on you, and the town shows its gratitude. | - Your horse, dog, or compadre saves the life of a child under threat from snakes, |",
         "| 61 | A Miraculous Rescue - Your horse, dog, or compadre saves the life of a child under threat from snakes, wolves or mountain lions. Their courage reflects well on you, and the town shows its gratitude. |"),
        ("| 62 A Happy Worker is a Good Worker loyal to you than ever. They fall over themselves to help you out. | - Your compadres / outfit employees are a happy crew, and seem more |",
         "| 62 | A Happy Worker is a Good Worker - Your compadres / outfit employees are a happy crew, and seem more loyal to you than ever. They fall over themselves to help you out. |"),
        ("| 63 Your Reputation Precedes You going price for the first 6 months (GM decides). Gain a new compadre, but are they truly trustworthy? | - A random NPC approaches you and offers you their services at half the |",
         "| 63 | Your Reputation Precedes You - A random NPC approaches you and offers you their services at half the going price for the first 6 months (GM decides). Gain a new compadre, but are they truly trustworthy? |"),
        ("| 64 A Repentant Rival ship between you, and professing their future fidelity and trust. This is a good development, but can they be trusted? | - An enemy or deadly rival comes to you, expressing their unhappiness at the relation- |",
         "| 64 | A Repentant Rival - An enemy or deadly rival comes to you, expressing their unhappiness at the relationship between you, and professing their future fidelity and trust. This is a good development, but can they be trusted? |"),
        ("| 65 Never Too Late to Learn themselves. One of your compadres adds +2 to one ability, and +1 to two others. Agree which abilities with your GM, or roll randomly. | - A compadre has been hard at work, practicing, learning, or otherwise bettering |",
         "| 65 | Never Too Late to Learn - A compadre has been hard at work, practicing, learning, or otherwise bettering themselves. One of your compadres adds +2 to one ability, and +1 to two others. Agree which abilities with your GM, or roll randomly. |"),
        ("| 66 Jackpot! | - Roll again, but the Tens die is automatically 7. |",
         "| 66 | Jackpot! - Roll again, but the Tens die is automatically 7. |"),
        ("| 71 Talk of the Town points and your Reputation moves 3 steps in a direction of your choice | - Everyone is talking about you, and they are talking you up. Your Fame increases by 2 |",
         "| 71 | Talk of the Town - Everyone is talking about you, and they are talking you up. Your Fame increases by 2 points and your Reputation moves 3 steps in a direction of your choice. |"),
        ("| 72 The Perfect Horse your herd just stood out. Roll a random stallion or mare. This horse gains a bonus quality, THE PER- FECT HORSE. | - You have come into possession of a new horse, either by purchase, gift, or one from |",
         "| 72 | The Perfect Horse - You have come into possession of a new horse, either by purchase, gift, or one from your herd just stood out. Roll a random stallion or mare. This horse gains a bonus quality, THE PERFECT HORSE. |"),
        ("| 73 An Unexpected Windfall and why they\u2019ve gifted you this windfall is up to the GM. The amount is equal to 3D6 \u00d7 $25. | - Someone, somewhere, has given you, or left you, some money. Who they are |",
         "| 73 | An Unexpected Windfall - Someone, somewhere, has given you, or left you, some money. Who they are and why they\u2019ve gifted you this windfall is up to the GM. The amount is equal to 3D6 \u00d7 $25. |"),
        ("| 74 A Blessing | - A child is born into your family, or to one of your compadres. |",
         "| 74 | A Blessing - A child is born into your family, or to one of your compadres. |"),
        ("| 75 Long-lost Family existed. They are overjoyed to be reunited with you. Gain a new compadre. | - A member of your family appears, who you thought long dead or never even knew |",
         "| 75 | Long-lost Family - A member of your family appears, who you thought long dead or never even knew existed. They are overjoyed to be reunited with you. Gain a new compadre. |"),
        ("| 76 Home is Where the Heart Is During the next season, when you are at home with your family or in a family gathering, you regain 3 Faith Points instead of 1. | - Your home and family really are the comforting haven you always wanted. |",
         "| 76 | Home is Where the Heart Is - Your home and family really are the comforting haven you always wanted. During the next season, when you are at home with your family or in a family gathering, you regain 3 Faith Points instead of 1. |"),
    ]

    for old, new in pf_fixes:
        if old in c:
            c = c.replace(old, new)
            changes += 1
        # Don't print individual entry fixes to reduce noise

    print(f"  [OK] Personal Fortunes individual entries ({sum(1 for o,n in pf_fixes if n.split('|')[1].strip() and '|' in c)} checked)")

    # Remove duplicate section headers for Personal Fortunes (merge into one table)
    # Remove the 2nd, 3rd section headers (keep the first one)
    # Pattern: blank line + "| D66 Personal Fortunes |  |" + newline + "| --- | --- |" + newline
    # These appear between sections - we need to remove them to merge tables
    dup_pf_header = "\n| D66 | Personal Fortunes |\n| --- | --- |\n"
    # First instance stays, remove subsequent ones within the personal fortunes section
    # Actually, let's find the personal fortunes section and count headers
    pf_section_hdr = "| D66 Personal Fortunes |  |\n| --- | --- |"
    while pf_section_hdr in c:
        c = c.replace(pf_section_hdr, "| D66 | Personal Fortunes |\n| --- | --- |")
        changes += 1
    # Now remove duplicate headers (keep only the first one in the PF section)
    # Find all occurrences
    first_pf = c.find("| D66 | Personal Fortunes |")
    if first_pf >= 0:
        # Find subsequent occurrences and remove them (they appear as table breaks)
        search_start = first_pf + 50
        while True:
            next_pf = c.find("\n\n| D66 | Personal Fortunes |\n| --- | --- |\n", search_start)
            if next_pf < 0:
                break
            # Remove this header (the blank line + header + separator)
            remove_str = "\n\n| D66 | Personal Fortunes |\n| --- | --- |\n"
            c = c[:next_pf] + "\n" + c[next_pf + len(remove_str):]
            changes += 1
            print("  [OK] Removed duplicate Personal Fortunes section header")

    # === 4. Town Fortunes - Fix garbled entries ===
    # Town Fortunes has similar issues: garbled headers and merged entries
    # Fix the first header that has entry 01 in it
    old_tf01_hdr = (
        "| D66 Town Fortunes "
        "01 Fool\u2019s Gold - The resources around the town are nowhere near "
        "as good as everyone thought. The town\u2019s Natural Riches aspect\u2019s "
        "maximum possible rank is reduced by 2. |  |\n"
        "| --- | --- |"
    )
    new_tf01_hdr = (
        "| D66 | Town Fortunes |\n"
        "| --- | --- |\n"
        "| 01 | Fool\u2019s Gold - The resources around the town are nowhere near "
        "as good as everyone thought. The town\u2019s Natural Riches aspect\u2019s "
        "maximum possible rank is reduced by 2. |"
    )
    if old_tf01_hdr in c:
        c = c.replace(old_tf01_hdr, new_tf01_hdr)
        changes += 1
        print("  [OK] Town Fortunes header/01")
    else:
        print("  [SKIP] Town Fortunes header/01 - not found")

    # Fix entry 02
    old_tf02 = (
        "| 02 Farmer\u2019s Folly "
        "keep g aspect\u2019s maximum possible rank is reduced by 2. "
        ". The town\u2019s Farmin "
        "| - Farming at this place is a fool\u2019s errand, as the land is poor "
        "and livestock impossible to |"
    )
    new_tf02 = (
        "| 02 | Farmer\u2019s Folly - Farming at this place is a fool\u2019s errand, "
        "as the land is poor and livestock impossible to keep. The town\u2019s "
        "Farming aspect\u2019s maximum possible rank is reduced by 2. |"
    )
    if old_tf02 in c:
        c = c.replace(old_tf02, new_tf02)
        changes += 1
        print("  [OK] Town Fortunes 02")
    else:
        print("  [SKIP] Town Fortunes 02 - not found")

    # Fix entry 03
    old_tf03 = (
        "| 03 No Boom, Just Bust "
        "pect\u2019s maximum possible rank is reduced by 2. "
        "here. The town\u2019s Mercantile as "
        "| - The town is poorly placed, trade passes you by and businesses "
        "struggle to grow |"
    )
    new_tf03 = (
        "| 03 | No Boom, Just Bust - The town is poorly placed, trade passes "
        "you by and businesses struggle to grow here. The town\u2019s Mercantile "
        "aspect\u2019s maximum possible rank is reduced by 2. |"
    )
    if old_tf03 in c:
        c = c.replace(old_tf03, new_tf03)
        changes += 1
        print("  [OK] Town Fortunes 03")
    else:
        print("  [SKIP] Town Fortunes 03 - not found")

    # Fix entry 04/05 merger
    old_tf0405 = (
        "| 04 Danger Town "
        "with deadly "
        "pect\u2019s maximum possible rank is reduced by 2. "
        "creatures. The town\u2019s Welfare as "
        "05 Terminal Decline - One of the town\u2019s aspects has gone into "
        "terminal and fatal decline. The aspect loses 1 tally point immediately "
        "and a further 1 tally point during each of the following three seasons. "
        "Roll D6: "
        "1\u20132 : Farming\u2014running a Farming outfit here just doesn\u2019t work "
        "anymore. There\u2019s better farming land else- where and people aren\u2019t "
        "buying what little you\u2019re managing to produce. "
        "3\u20134 : Mercantile\u2014the town has been bypassed or the goods traded "
        "here just aren\u2019t any good. Business here will come to an end soon "
        "enough. "
        "5\u20136 : Natural Riches\u2014this place is tapped out, the mines are empty, "
        "the timber is poor, there\u2019s no point "
        "gging a dead horse. flo "
        "| - The town is more dangerous than you thought\u2014disease abounds "
        "or the ground swarms |"
    )
    new_tf0405 = (
        "| 04 | Danger Town - The town is more dangerous than you thought\u2014"
        "disease abounds or the ground swarms with deadly creatures. The "
        "town\u2019s Welfare aspect\u2019s maximum possible rank is reduced by 2. |\n"
        "| 05 | Terminal Decline - One of the town\u2019s aspects has gone into "
        "terminal and fatal decline. The aspect loses 1 tally point immediately "
        "and a further 1 tally point during each of the following three seasons. "
        "Roll D6: "
        "1\u20132: Farming\u2014running a Farming outfit here just doesn\u2019t work "
        "anymore. There\u2019s better farming land elsewhere and people aren\u2019t "
        "buying what little you\u2019re managing to produce. "
        "3\u20134: Mercantile\u2014the town has been bypassed or the goods traded "
        "here just aren\u2019t any good. Business here will come to an end soon "
        "enough. "
        "5\u20136: Natural Riches\u2014this place is tapped out, the mines are empty, "
        "the timber is poor, there\u2019s no point flogging a dead horse. |"
    )
    if old_tf0405 in c:
        c = c.replace(old_tf0405, new_tf0405)
        changes += 1
        print("  [OK] Town Fortunes 04/05")
    else:
        print("  [SKIP] Town Fortunes 04/05 - not found")

    # Fix entry 06
    old_tf06 = (
        "| 06 Terrible Disaster "
        "1 : Farming\u2014the climate has shifted and farming here is becoming "
        "impossible. The Farming aspect is immediately reduced by 4 tally "
        "points. "
        "2 : Mercantile\u2014business is suddenly passing your town by, and trade "
        "has dried up. The Mercantile aspect is immediately reduced by 4 "
        "tally points. "
        "3 : Natural Riches\u2014those mines have tapped out, or the claims have "
        "been seen to be false. The Natural Riches aspect is immediately "
        "reduced by 4 tally points. "
        "4 : Law\u2014the town has been flooded with bad men and troublemakers. "
        "The Law aspect is immediately reduced by 4 tally points. "
        "5 : Civic\u2014the community spirit has been shattered by strife and "
        "feuds. The Civic aspect is immediately reduced by 4 tally points. "
        "6 : Welfare\u2014the dangers of the town have become terrible. It may "
        "be a landslide or earthquake or a plague, but this place is not "
        "safe any "
        "pect is immediately reduced by 4 tally points. "
        "more. The Welfare as "
        "| - Roll D6 |"
    )
    new_tf06 = (
        "| 06 | Terrible Disaster - Roll D6: "
        "1: Farming\u2014the climate has shifted and farming here is becoming "
        "impossible. The Farming aspect is immediately reduced by 4 tally "
        "points. "
        "2: Mercantile\u2014business is suddenly passing your town by, and trade "
        "has dried up. The Mercantile aspect is immediately reduced by 4 "
        "tally points. "
        "3: Natural Riches\u2014those mines have tapped out, or the claims have "
        "been seen to be false. The Natural Riches aspect is immediately "
        "reduced by 4 tally points. "
        "4: Law\u2014the town has been flooded with bad men and troublemakers. "
        "The Law aspect is immediately reduced by 4 tally points. "
        "5: Civic\u2014the community spirit has been shattered by strife and "
        "feuds. The Civic aspect is immediately reduced by 4 tally points. "
        "6: Welfare\u2014the dangers of the town have become terrible. It may "
        "be a landslide or earthquake or a plague, but this place is not "
        "safe anymore. The Welfare aspect is immediately reduced by 4 tally "
        "points. |"
    )
    if old_tf06 in c:
        c = c.replace(old_tf06, new_tf06)
        changes += 1
        print("  [OK] Town Fortunes 06")
    else:
        print("  [SKIP] Town Fortunes 06 - not found")

    # Fix entry 11
    old_tf11 = "| 11 Calamity! | - Roll D66 again, but the Tens die result is automatically 0. |"
    new_tf11 = "| 11 | Calamity! - Roll D66 again, but the Tens die result is automatically 0. |"
    if old_tf11 in c:
        c = c.replace(old_tf11, new_tf11)
        changes += 1

    # Fix entry 12/13 merger
    old_tf1213 = (
        "| 12 Disease Outbreak "
        "The settlement loses 2 tally points from a random aspect. "
        "13 Town Fires! - There have been a couple of close calls, but if "
        "we ain\u2019t careful fire could spell disaster! But why are there so "
        "many fires right now? Lose 1 tally point from both Mercantile & "
        "Welfare. "
        "| - Some terrible disease is sweeping the county. Hope the Lord "
        "don\u2019t let it come here. |"
    )
    new_tf1213 = (
        "| 12 | Disease Outbreak - Some terrible disease is sweeping the county. "
        "Hope the Lord don\u2019t let it come here. The settlement loses 2 tally "
        "points from a random aspect. |\n"
        "| 13 | Town Fires! - There have been a couple of close calls, but if "
        "we ain\u2019t careful fire could spell disaster! But why are there so "
        "many fires right now? Lose 1 tally point from both Mercantile & "
        "Welfare. |"
    )
    if old_tf1213 in c:
        c = c.replace(old_tf1213, new_tf1213)
        changes += 1
        print("  [OK] Town Fortunes 12/13")
    else:
        print("  [SKIP] Town Fortunes 12/13 - not found")

    # Fix entry 14
    old_tf14 = (
        "| 14 Torrential Rains and flooding "
        "nights. Lose 1 tally point from both Farming & Natural Riches. "
        "| - It\u2019s been raining a lot, and some are talking about forty days "
        "and forty |"
    )
    new_tf14 = (
        "| 14 | Torrential Rains - It\u2019s been raining a lot, and some are "
        "talking about forty days and forty nights. Lose 1 tally point from "
        "both Farming & Natural Riches. |"
    )
    if old_tf14 in c:
        c = c.replace(old_tf14, new_tf14)
        changes += 1
        print("  [OK] Town Fortunes 14")
    else:
        print("  [SKIP] Town Fortunes 14 - not found")

    # Fix entry 15
    old_tf15 = (
        "| 15 Lawlessness in Town "
        "making the town a dangerous place to be. Lose 1 tally point from "
        "both Law & Civic. "
        "| - It seems to be getting worse\u2014more and more drunken cowboys "
        "and outlaws are |"
    )
    new_tf15 = (
        "| 15 | Lawlessness in Town - It seems to be getting worse\u2014more and "
        "more drunken cowboys and outlaws are making the town a dangerous "
        "place to be. Lose 1 tally point from both Law & Civic. |"
    )
    if old_tf15 in c:
        c = c.replace(old_tf15, new_tf15)
        changes += 1
        print("  [OK] Town Fortunes 15")
    else:
        print("  [SKIP] Town Fortunes 15 - not found")

    # Fix entry 16/Drought merger
    old_tf16 = (
        "| 16 Deep Freeze (Winter or Spring) "
        "| - Will this terrible winter ever end? |\n"
        "| Drought (Summer or Autumn) "
        "animals, and then the people, will die of thirst. The town loses "
        "1D3 Settlement Points to a minimum of 0. "
        "21 Terrible Storms - The weather is angry, and the old-timers say "
        "it\u2019s set to get worse. Lose 1 tally point from either Mercantile "
        "or Welfare. "
        "22 Insect Infestations - From insect swarms eating the fields, to "
        "midges and mites spoiling the crops in the barns, to roaches "
        "spreading disease and them poisonous spiders\u2014it\u2019s almost a "
        "biblical disaster. The town cannot start any amenities this season. "
        "| - It looks set to be hot as hell. If it gets bad nothing will grow "
        "and the |"
    )
    new_tf16 = (
        "| 16 | Deep Freeze (Winter or Spring) / Drought (Summer or Autumn) - "
        "Will this terrible winter ever end? / It looks set to be hot as hell. "
        "If it gets bad nothing will grow and the animals, and then the people, "
        "will die of thirst. The town loses 1D3 Settlement Points to a "
        "minimum of 0. |\n"
        "| 21 | Terrible Storms - The weather is angry, and the old-timers say "
        "it\u2019s set to get worse. Lose 1 tally point from either Mercantile "
        "or Welfare. |\n"
        "| 22 | Insect Infestations - From insect swarms eating the fields, to "
        "midges and mites spoiling the crops in the barns, to roaches "
        "spreading disease and them poisonous spiders\u2014it\u2019s almost a "
        "biblical disaster. The town cannot start any amenities this season. |"
    )
    if old_tf16 in c:
        c = c.replace(old_tf16, new_tf16)
        changes += 1
        print("  [OK] Town Fortunes 16/21/22")
    else:
        print("  [SKIP] Town Fortunes 16/21/22 - not found")

    # Fix section 2 header and entries 23-36
    old_tf_s2_hdr = "| D66 Town Fortunes |  |\n| --- | --- |"
    if old_tf_s2_hdr in c:
        c = c.replace(old_tf_s2_hdr, "| D66 | Town Fortunes |\n| --- | --- |", 1)
        changes += 1
        print("  [OK] Town Fortunes section 2 header")

    # Fix entry 23/24/25 merger
    old_tf2325 = (
        "| 23 Wolves "
        "they work. Lose 1 tally point from either Farming or Natural Riches. "
        "24 Outlaws Abound - There are outlaws roaming the land, trying to "
        "survive. Maybe a famous gang is ru- mored to have entered this here "
        "territory. Lose 1 tally point from either Law or Civic. 25 "
        "| - Starving wolf packs have been roaming nearby, attacking livestock "
        "and bothering people while |"
    )
    new_tf2325 = (
        "| 23 | Wolves - Starving wolf packs have been roaming nearby, "
        "attacking livestock and bothering people while they work. Lose 1 "
        "tally point from either Farming or Natural Riches. |\n"
        "| 24 | Outlaws Abound - There are outlaws roaming the land, trying "
        "to survive. Maybe a famous gang is rumored to have entered this "
        "here territory. Lose 1 tally point from either Law or Civic. |"
    )
    if old_tf2325 in c:
        c = c.replace(old_tf2325, new_tf2325)
        changes += 1
        print("  [OK] Town Fortunes 23/24")
    else:
        print("  [SKIP] Town Fortunes 23/24 - not found")

    # Fix entry 25
    old_tf25 = (
        "Wildfires "
        "threaten the whole community. Lose 1 tally point from either "
        "Farming, Natural Riches or Welfare. "
        "| - Wildfires have been breaking out. Let\u2019s hope the weather keeps "
        "them in check as these can |"
    )
    new_tf25 = (
        "| 25 | Wildfires - Wildfires have been breaking out. Let\u2019s hope "
        "the weather keeps them in check as these can threaten the whole "
        "community. Lose 1 tally point from either Farming, Natural Riches "
        "or Welfare. |"
    )
    if old_tf25 in c:
        c = c.replace(old_tf25, new_tf25)
        changes += 1
        print("  [OK] Town Fortunes 25")
    else:
        print("  [SKIP] Town Fortunes 25 - not found")

    # Fix entry 26/31/32 merger
    old_tf2632 = (
        "| 26 Religious Trouble "
        "no sign of it in the town\u2014yet. Lose 1 tally point from either "
        "Law, Civic or Mercantile. "
        "31 Vermin Infestation - They have been getting worse all over the "
        "town, and you doubt the ratters can cope. The place could be "
        "overrun and if it\u2019s not dealt with soon disease will start to "
        "spread. Characters running a Merchant or Trading outfit suffer "
        "a \u22121 penalty to their Business roll at the end of the season. "
        "32 Cattle Rustlers - Darned outlaws turned rustlers, driving stolen "
        "herds through plowed fields and crops. Characters running a Farming "
        "business suffer a \u22121 penalty to their Business roll at the end of "
        "the season. "
        "| - There are rumors of religious intolerance breaking out into "
        "violence, but there\u2019s been |"
    )
    new_tf2632 = (
        "| 26 | Religious Trouble - There are rumors of religious intolerance "
        "breaking out into violence, but there\u2019s been no sign of it in the "
        "town\u2014yet. Lose 1 tally point from either Law, Civic or "
        "Mercantile. |\n"
        "| 31 | Vermin Infestation - They have been getting worse all over "
        "the town, and you doubt the ratters can cope. The place could be "
        "overrun and if it\u2019s not dealt with soon disease will start to "
        "spread. Characters running a Merchant or Trading outfit suffer "
        "a \u22121 penalty to their Business roll at the end of the season. |\n"
        "| 32 | Cattle Rustlers - Darned outlaws turned rustlers, driving "
        "stolen herds through plowed fields and crops. Characters running "
        "a Farming business suffer a \u22121 penalty to their Business roll at "
        "the end of the season. |"
    )
    if old_tf2632 in c:
        c = c.replace(old_tf2632, new_tf2632)
        changes += 1
        print("  [OK] Town Fortunes 26/31/32")
    else:
        print("  [SKIP] Town Fortunes 26/31/32 - not found")

    # Fix entry 33
    old_tf33 = (
        "| 33 Border Disputes "
        "wanting to draw the line around your fine natural riches. It ain\u2019t "
        "come to blows yet, but who knows. Char- acters running "
        "penalty to their Business roll at the end of the season. "
        "a Resources outfit suffer a \u20131 "
        "| - You hear stories of trouble over the state or territorial border, "
        "with your neighbors |"
    )
    new_tf33 = (
        "| 33 | Border Disputes - You hear stories of trouble over the state "
        "or territorial border, with your neighbors wanting to draw the line "
        "around your fine natural riches. It ain\u2019t come to blows yet, but "
        "who knows. Characters running a Resources outfit suffer a \u22121 "
        "penalty to their Business roll at the end of the season. |"
    )
    if old_tf33 in c:
        c = c.replace(old_tf33, new_tf33)
        changes += 1
        print("  [OK] Town Fortunes 33")
    else:
        print("  [SKIP] Town Fortunes 33 - not found")

    # Fix entry 34
    old_tf34 = (
        "| 34 Native Anger "
        "to raid some goods, or riding against the cavalry out of fear or "
        "vengeance. "
        "| - A local nation has been rumored to be gathering, maybe driven "
        "by cold and hunger, out |"
    )
    new_tf34 = (
        "| 34 | Native Anger - A local nation has been rumored to be "
        "gathering, maybe driven by cold and hunger, out to raid some goods, "
        "or riding against the cavalry out of fear or vengeance. |"
    )
    if old_tf34 in c:
        c = c.replace(old_tf34, new_tf34)
        changes += 1
        print("  [OK] Town Fortunes 34")
    else:
        print("  [SKIP] Town Fortunes 34 - not found")

    # Fix entry 35/36 merger
    old_tf3536 = (
        "| 35 An Important Official is coming "
        "should get busy making itself look good for the visit. "
        "36 Homestead Claims - There\u2019s been a lot of friction, and some "
        "say the local Homestead Claims officials are corrupt. It seems "
        "like trouble may be brewing. "
        "41 Pinkertons in Town - They ain\u2019t causing no trouble, and have "
        "money to spend, but there\u2019s gotta be a reason why the Pinkerton "
        "investigators have stopped here. "
        "| - Rumor has it some big-wig from the east is coming. Maybe the town |"
    )
    new_tf3536 = (
        "| 35 | An Important Official is coming - Rumor has it some big-wig "
        "from the east is coming. Maybe the town should get busy making "
        "itself look good for the visit. |\n"
        "| 36 | Homestead Claims - There\u2019s been a lot of friction, and some "
        "say the local Homestead Claims officials are corrupt. It seems "
        "like trouble may be brewing. |\n"
        "| 41 | Pinkertons in Town - They ain\u2019t causing no trouble, and have "
        "money to spend, but there\u2019s gotta be a reason why the Pinkerton "
        "investigators have stopped here. |"
    )
    if old_tf3536 in c:
        c = c.replace(old_tf3536, new_tf3536)
        changes += 1
        print("  [OK] Town Fortunes 35/36/41")
    else:
        print("  [SKIP] Town Fortunes 35/36/41 - not found")

    # Fix entry 42
    old_tf42 = (
        "| 42 Deadly Feud "
        "true but fear it could spread and end up here. "
        "| - You\u2019ve heard stories of a deadly feud in a town or county "
        "nearby. You don\u2019t know if it\u2019s |"
    )
    new_tf42 = (
        "| 42 | Deadly Feud - You\u2019ve heard stories of a deadly feud in a "
        "town or county nearby. You don\u2019t know if it\u2019s true but fear it "
        "could spread and end up here. |"
    )
    if old_tf42 in c:
        c = c.replace(old_tf42, new_tf42)
        changes += 1
        print("  [OK] Town Fortunes 42")
    else:
        print("  [SKIP] Town Fortunes 42 - not found")

    # Fix entry 43/44/45 merger
    old_tf4345 = (
        "| 43 The Traveling Theatre Troupe "
        "break from it all. But what else will these traveling folk bring? "
        "44 Perfect Conditions - The winds are good, the rains are just "
        "right, the sun is shining, and the pests and vermin are nowhere "
        "to be seen. It\u2019s great being a farmer when the Lord sends "
        "conditions like these! Char- acters running a Farming business "
        "get a +1 bonus to their Business roll at the end of the season. 45 "
        "| - Entertainment is the salve of a hardworking heart, and it\u2019s "
        "good to take a |"
    )
    new_tf4345 = (
        "| 43 | The Traveling Theatre Troupe - Entertainment is the salve of "
        "a hardworking heart, and it\u2019s good to take a break from it all. "
        "But what else will these traveling folk bring? |\n"
        "| 44 | Perfect Conditions - The winds are good, the rains are just "
        "right, the sun is shining, and the pests and vermin are nowhere "
        "to be seen. It\u2019s great being a farmer when the Lord sends "
        "conditions like these! Characters running a Farming business "
        "get a +1 bonus to their Business roll at the end of the season. |"
    )
    if old_tf4345 in c:
        c = c.replace(old_tf4345, new_tf4345)
        changes += 1
        print("  [OK] Town Fortunes 43/44")
    else:
        print("  [SKIP] Town Fortunes 43/44 - not found")

    # Fix entry 45/46/51/52 merger
    old_tf4552 = (
        "The Army is Coming "
        "Whatever the reason, the army brings money\u2014both an opportunity "
        "and a threat to the local town. Char- acters running a Merchant "
        "or Trading "
        "get a +1 bonus to their Business roll at the end of the season. "
        "outfit "
        "| - There\u2019s rumors that the army is heading this way, but no one "
        "knows for why. |\n"
        "| 46 Big Claims "
        "big claims cheap to anyone that can pay. Sounds too good to be "
        "true... Characters running a Resources "
        "get a +1 bonus to their Business roll at the end of the next season. "
        "outfit "
        "51 New Preacher in Town - There\u2019s always more space for God in the "
        "life of the town, so maybe this new preacher man is a good thing! "
        "The town can buy the Church amenity for 3 Settlement Points, but "
        "only if they buy it this season. "
        "52 Cattle Drive - There\u2019s rumors of a cattle drive coming this way. "
        "Maybe a chance for some work, or an opportunity to take possession "
        "of a nice steer or two. Add 1 tally point to either Farming, "
        "Mercantile or Natural Riches. "
        "| - Rumors abound that this place is onto something big. New folks "
        "are in town selling these |"
    )
    new_tf4552 = (
        "| 45 | The Army is Coming - There\u2019s rumors that the army is heading "
        "this way, but no one knows for why. Whatever the reason, the army "
        "brings money\u2014both an opportunity and a threat to the local town. "
        "Characters running a Merchant or Trading outfit get a +1 bonus to "
        "their Business roll at the end of the season. |\n"
        "| 46 | Big Claims - Rumors abound that this place is onto something "
        "big. New folks are in town selling these big claims cheap to anyone "
        "that can pay. Sounds too good to be true... Characters running a "
        "Resources outfit get a +1 bonus to their Business roll at the end "
        "of the next season. |\n"
        "| 51 | New Preacher in Town - There\u2019s always more space for God in "
        "the life of the town, so maybe this new preacher man is a good "
        "thing! The town can buy the Church amenity for 3 Settlement Points, "
        "but only if they buy it this season. |\n"
        "| 52 | Cattle Drive - There\u2019s rumors of a cattle drive coming this "
        "way. Maybe a chance for some work, or an opportunity to take "
        "possession of a nice steer or two. Add 1 tally point to either "
        "Farming, Mercantile or Natural Riches. |"
    )
    if old_tf4552 in c:
        c = c.replace(old_tf4552, new_tf4552)
        changes += 1
        print("  [OK] Town Fortunes 45/46/51/52")
    else:
        print("  [SKIP] Town Fortunes 45/46/51/52 - not found")

    # Fix entry 53
    old_tf53 = (
        "| 53 Doctors and Apothecaries in Town "
        "to have new medicines and remedies to try, if he ain\u2019t no quack. "
        "Add 1 tally point to either Law, Civic or Welfare. "
        "| - There\u2019s a fella gone to calling himself Doctor, but it\u2019s "
        "always good |"
    )
    new_tf53 = (
        "| 53 | Doctors and Apothecaries in Town - There\u2019s a fella gone to "
        "calling himself Doctor, but it\u2019s always good to have new medicines "
        "and remedies to try, if he ain\u2019t no quack. Add 1 tally point to "
        "either Law, Civic or Welfare. |"
    )
    if old_tf53 in c:
        c = c.replace(old_tf53, new_tf53)
        changes += 1
        print("  [OK] Town Fortunes 53")
    else:
        print("  [SKIP] Town Fortunes 53 - not found")

    # Fix section 3 header with entry 54
    old_tf_s3_hdr = (
        "| D66 Town Fortunes "
        "54 Unseasonal Rains - The weather is wet. It\u2019s good for the crops "
        "but everyone gets sick of the damp, and worries about what all "
        "this downpour is doing to the headwaters of the local rivers. "
        "Add 1 tally point to either Farming or Natural Riches. |  |\n"
        "| --- | --- |"
    )
    new_tf_s3_hdr = (
        "| D66 | Town Fortunes |\n"
        "| --- | --- |\n"
        "| 54 | Unseasonal Rains - The weather is wet. It\u2019s good for the "
        "crops but everyone gets sick of the damp, and worries about what "
        "all this downpour is doing to the headwaters of the local rivers. "
        "Add 1 tally point to either Farming or Natural Riches. |"
    )
    if old_tf_s3_hdr in c:
        c = c.replace(old_tf_s3_hdr, new_tf_s3_hdr)
        changes += 1
        print("  [OK] Town Fortunes section 3 header/54")
    else:
        print("  [SKIP] Town Fortunes section 3 header/54 - not found")

    # Fix entry 55/56/61 merger
    old_tf5561 = (
        "| 55 Federal Marshal in Town "
        "them bad guys, but why does the marshal keep coming by this way? "
        "Add 1 tally point to either Law or Welfare. "
        "56 Festivals! - The town has been bustling with talk of the upcoming "
        "excitement and debauchery of this season\u2019s festivals. Add 1 tally "
        "point to either Mercantile or Civic. "
        "61 Native Trade - Many might distrust the Native Americans but they "
        "have some fine things for trade. And when you deal fair with them "
        "they are darned fair back to y\u2019all too. Add 1 tally point to both "
        "Mercantile and Welfare. "
        "| - It\u2019s always good to have a tough man of the law in town keeping "
        "a lid on all |"
    )
    new_tf5561 = (
        "| 55 | Federal Marshal in Town - It\u2019s always good to have a tough "
        "man of the law in town keeping a lid on all them bad guys, but "
        "why does the marshal keep coming by this way? Add 1 tally point "
        "to either Law or Welfare. |\n"
        "| 56 | Festivals! - The town has been bustling with talk of the "
        "upcoming excitement and debauchery of this season\u2019s festivals. "
        "Add 1 tally point to either Mercantile or Civic. |\n"
        "| 61 | Native Trade - Many might distrust the Native Americans but "
        "they have some fine things for trade. And when you deal fair with "
        "them they are darned fair back to y\u2019all too. Add 1 tally point "
        "to both Mercantile and Welfare. |"
    )
    if old_tf5561 in c:
        c = c.replace(old_tf5561, new_tf5561)
        changes += 1
        print("  [OK] Town Fortunes 55/56/61")
    else:
        print("  [SKIP] Town Fortunes 55/56/61 - not found")

    # Fix entry 62
    old_tf62 = (
        "| 62 Population Boom "
        "good for business! The town gains an extra 1D3 Settlement Points. "
        "| - It started as a trickle and where they all came from you don\u2019t "
        "know, but it\u2019s damn |"
    )
    new_tf62 = (
        "| 62 | Population Boom - It started as a trickle and where they all "
        "came from you don\u2019t know, but it\u2019s damn good for business! The "
        "town gains an extra 1D3 Settlement Points. |"
    )
    if old_tf62 in c:
        c = c.replace(old_tf62, new_tf62)
        changes += 1
        print("  [OK] Town Fortunes 62")
    else:
        print("  [SKIP] Town Fortunes 62 - not found")

    # Fix entry 63
    old_tf63 = (
        "| 63 Booming Market Days in Town "
        "everyone up and is good for business. Add 1 tally point to both "
        "Civic and Law. "
        "| - It\u2019s always good to have a market and festival day in town. "
        "It cheers |"
    )
    new_tf63 = (
        "| 63 | Booming Market Days in Town - It\u2019s always good to have a "
        "market and festival day in town. It cheers everyone up and is good "
        "for business. Add 1 tally point to both Civic and Law. |"
    )
    if old_tf63 in c:
        c = c.replace(old_tf63, new_tf63)
        changes += 1
        print("  [OK] Town Fortunes 63")
    else:
        print("  [SKIP] Town Fortunes 63 - not found")

    # Fix entry 64/65 merger
    old_tf6465 = (
        "| 64 Nature\u2019s Bounty "
        "hunters and the destitute who rely on forage to get by, but not "
        "so good for careless travelers. Add 1 tally point to both Farming "
        "and Natural Riches. "
        "65 Perfect Weather - The weather\u2019s set to be as good as it gets "
        "for the time of year\u2014it\u2019s good to be alive. Add 2 tally points "
        "to a random aspect. "
        "| - There are more berries, fruits and wild animals than anyone "
        "can remember, great for |"
    )
    new_tf6465 = (
        "| 64 | Nature\u2019s Bounty - There are more berries, fruits and wild "
        "animals than anyone can remember, great for hunters and the "
        "destitute who rely on forage to get by, but not so good for "
        "careless travelers. Add 1 tally point to both Farming and Natural "
        "Riches. |\n"
        "| 65 | Perfect Weather - The weather\u2019s set to be as good as it gets "
        "for the time of year\u2014it\u2019s good to be alive. Add 2 tally points "
        "to a random aspect. |"
    )
    if old_tf6465 in c:
        c = c.replace(old_tf6465, new_tf6465)
        changes += 1
        print("  [OK] Town Fortunes 64/65")
    else:
        print("  [SKIP] Town Fortunes 64/65 - not found")

    # Fix entry 66
    old_tf66 = "| 66 Jackpot! | - Roll D66 again but the Tens die result is automatically 7. |"
    new_tf66 = "| 66 | Jackpot! - Roll D66 again but the Tens die result is automatically 7. |"
    if old_tf66 in c:
        c = c.replace(old_tf66, new_tf66)
        changes += 1

    # Fix entry 71
    old_tf71 = (
        "| 71 Pay Dirt! "
        "ing about the find come flocking to seek their fortunes. Roll D6: "
        "1\u20134 : A rich new seam of silver has been found. "
        "5\u20136 : A panner has come into town with huge nuggets of gold! "
        "| - Rumors abound that someone\u2019s made it big and there\u2019s a new "
        "claim in the area. People hear- |"
    )
    new_tf71 = (
        "| 71 | Pay Dirt! - Rumors abound that someone\u2019s made it big and "
        "there\u2019s a new claim in the area. People hearing about the find "
        "come flocking to seek their fortunes. Roll D6: "
        "1\u20134: A rich new seam of silver has been found. "
        "5\u20136: A panner has come into town with huge nuggets of gold! |"
    )
    if old_tf71 in c:
        c = c.replace(old_tf71, new_tf71)
        changes += 1
        print("  [OK] Town Fortunes 71")
    else:
        print("  [SKIP] Town Fortunes 71 - not found")

    # Fix entry 72
    old_tf72 = (
        "| 72 Town is Growing Like a Weed "
        "the most of it! One aspect immediately gains 1 tally point and will "
        "automatically gain another tally point during each of the next three "
        "seasons. Roll D6: "
        "1\u20132 : Farming\u2014running a farming outfit here just got easy! The "
        "land is fertile and animals thrive. "
        "3\u20134 : Mercantile\u2014the town\u2019s economy has gone mad, with traders "
        "and businesses coming here in droves to make money. "
        "5\u20136 : Natural Riches\u2014this place is rich in natural resources, "
        "and new seams are found almost every day. "
        "| - One aspect of the town is thriving so well that people flock "
        "to make |"
    )
    new_tf72 = (
        "| 72 | Town is Growing Like a Weed - One aspect of the town is "
        "thriving so well that people flock to make the most of it! One "
        "aspect immediately gains 1 tally point and will automatically "
        "gain another tally point during each of the next three seasons. "
        "Roll D6: "
        "1\u20132: Farming\u2014running a farming outfit here just got easy! The "
        "land is fertile and animals thrive. "
        "3\u20134: Mercantile\u2014the town\u2019s economy has gone mad, with traders "
        "and businesses coming here in droves to make money. "
        "5\u20136: Natural Riches\u2014this place is rich in natural resources, "
        "and new seams are found almost every day. |"
    )
    if old_tf72 in c:
        c = c.replace(old_tf72, new_tf72)
        changes += 1
        print("  [OK] Town Fortunes 72")
    else:
        print("  [SKIP] Town Fortunes 72 - not found")

    # Fix entry 73/74/75/76 merger
    old_tf7376 = (
        "| 73 By God\u2019s Grace "
        "has changed, or the water level in the nearby creek washes away "
        "all the dirt of the town. The Welfare aspect immediately gains "
        "2 tally points. "
        "74 Boom Time - People flock to the town for the strength of its "
        "trading and businesses. The Mercantile aspect immediately gains "
        "2 tally points. 75 "
        "| - Something has shifted that makes this place a safer place to "
        "live. Maybe the climate |\n"
        "| The Lord\u2019s Fertility "
        "success is assured for a hardworking farmer. The Farming aspect "
        "immediately gains 2 tally points. 76 "
        "| - The farming and grazing land around town is found to be so "
        "rich and fertile that |\n"
        "| The One in a Million Find "
        "be set forever! The Natural Riches aspect immediately gains "
        "2 tally points. "
        "| - A prospector has found a huge bounty of natural resources. "
        "The town must |"
    )
    new_tf7376 = (
        "| 73 | By God\u2019s Grace - Something has shifted that makes this "
        "place a safer place to live. Maybe the climate has changed, or "
        "the water level in the nearby creek washes away all the dirt of "
        "the town. The Welfare aspect immediately gains 2 tally points. |\n"
        "| 74 | Boom Time - People flock to the town for the strength of "
        "its trading and businesses. The Mercantile aspect immediately "
        "gains 2 tally points. |\n"
        "| 75 | The Lord\u2019s Fertility - The farming and grazing land around "
        "town is found to be so rich and fertile that success is assured "
        "for a hardworking farmer. The Farming aspect immediately gains "
        "2 tally points. |\n"
        "| 76 | The One in a Million Find - A prospector has found a huge "
        "bounty of natural resources. The town must be set forever! The "
        "Natural Riches aspect immediately gains 2 tally points. |"
    )
    if old_tf7376 in c:
        c = c.replace(old_tf7376, new_tf7376)
        changes += 1
        print("  [OK] Town Fortunes 73/74/75/76")
    else:
        print("  [SKIP] Town Fortunes 73/74/75/76 - not found")

    # Remove duplicate Town Fortunes section headers
    first_tf = c.find("| D66 | Town Fortunes |")
    if first_tf >= 0:
        search_start = first_tf + 50
        while True:
            next_tf = c.find("\n\n| D66 | Town Fortunes |\n| --- | --- |\n", search_start)
            if next_tf < 0:
                break
            remove_str = "\n\n| D66 | Town Fortunes |\n| --- | --- |\n"
            c = c[:next_tf] + "\n" + c[next_tf + len(remove_str):]
            changes += 1
            print("  [OK] Removed duplicate Town Fortunes section header")

    write("08-campaigns-in-the-old-west.md", c)
    print(f"\nCh08: {changes} changes applied and saved.")
    return changes


def fix_ch10():
    c = read("10-patience-is-a-virtue.md")
    changes = 0

    # === 1. Where Were You Born table ===
    # Currently entries 2-6 are a garbled table, entries 7-12 are plain text
    # Replace the entire section

    old_born_table = """| Roll Region Heritage |  |
| --- | --- |
| 2 The Ottoman Empire, | Turkey, the Ottoman Empire including Serbia, Wallachia and Moldavia, the |
| the Middle East and North Africa Likely to be of Native or colonial heritage (colonial powers in the region includ- ed Britain, France, Turkey and Spain). 3 British North America Provinces of Canada (including Quebec), New Brunswick, Nova Scotia, Prince Edward Island, Rupert\u2019s Land. You will likely be of British, French or Native American heritage. | Levant, Persia, Arabia, Syria, Egypt, Libya, Morocco, Tunisia, and Algeria. |
| 4 Continental Northwest | British Columbia, North Western Territory, or Dakota, Idaho, Wyoming, Mon- |
| and Northern Great Plains heritage. | tana, and Washington territories. Can be of European, Canadian, US, or Native |
| 5 The Great lakes and | Including Michigan, Wisconsin, Ohio, Indiana, and Illinois. Likely to be of |
| Midwest, including \u201cIndian Territory\u201d 6 Europe United Kingdom, Ireland, the Netherlands, Germany, Poland, France, Italy, Spain, Portugal, Greece, Norway, Denmark (including Iceland and Greenland), Sweden, Finland, and the Russian Empire. | European heritage or Native. |

7 The Northeast Including New England, New York, New Jersey, and Pennsylvania. Can be of European, African or Native heritage.
8 Southeast Florida, Louisiana, Virginia, the Carolinas, Kentucky, Tennessee, Georgia, Ala- bama, Mississippi. Likely to be of European or African descent, or from Native American remnant communities.
9 The South, Southern  Including Texas, New Mexico, Arizona, Colorado and Kansas. Likely to be of Great Plains,  Mexico  US, Mexican or Native heritage, or you may have traveled through Mexico from and South America further south.
10 West Coast and Great  California, Oregon, Nevada and Utah. Likely to be of European, American, Basin Mexican, Chinese or Native heritage.
11 East Asia and the Pacific Most likely Asian heritage, for example Chinese, Korean, and Japanese, but  also possibly , Australian, or New Zealander.
Pacific islander 12 India, and Equatorial  West Africa, Nigeria, Niger, Angola, German East Africa, Mozambique, and Southern Africa Rhodesia, or South African Republic. Likely to be of Native or colonial heritage (colonial powers including Britain, Portugal and Germany)."""

    new_born_table = """| Roll | Region | Heritage |
| --- | --- | --- |
| 2 | The Ottoman Empire, the Middle East and North Africa | Turkey, the Ottoman Empire including Serbia, Wallachia and Moldavia, the Levant, Persia, Arabia, Syria, Egypt, Libya, Morocco, Tunisia, and Algeria. Likely to be of Native or colonial heritage (colonial powers in the region included Britain, France, Turkey and Spain). |
| 3 | British North America | Provinces of Canada (including Quebec), New Brunswick, Nova Scotia, Prince Edward Island, Rupert\u2019s Land. You will likely be of British, French or Native American heritage. |
| 4 | Continental Northwest and Northern Great Plains | British Columbia, North Western Territory, or Dakota, Idaho, Wyoming, Montana, and Washington territories. Can be of European, Canadian, US, or Native heritage. |
| 5 | The Great Lakes and Midwest, including \u201cIndian Territory\u201d | Including Michigan, Wisconsin, Ohio, Indiana, and Illinois. Likely to be of European heritage or Native. |
| 6 | Europe | United Kingdom, Ireland, the Netherlands, Germany, Poland, France, Italy, Spain, Portugal, Greece, Norway, Denmark (including Iceland and Greenland), Sweden, Finland, and the Russian Empire. |
| 7 | The Northeast | Including New England, New York, New Jersey, and Pennsylvania. Can be of European, African or Native heritage. |
| 8 | Southeast | Florida, Louisiana, Virginia, the Carolinas, Kentucky, Tennessee, Georgia, Alabama, Mississippi. Likely to be of European or African descent, or from Native American remnant communities. |
| 9 | The South, Southern Great Plains, Mexico and South America | Including Texas, New Mexico, Arizona, Colorado and Kansas. Likely to be of US, Mexican or Native heritage, or you may have traveled through Mexico from further south. |
| 10 | West Coast and Great Basin | California, Oregon, Nevada and Utah. Likely to be of European, American, Mexican, Chinese or Native heritage. |
| 11 | East Asia and the Pacific | Most likely Asian heritage, for example Chinese, Korean, and Japanese, but also possibly Pacific islander, Australian, or New Zealander. |
| 12 | India, and Equatorial and Southern Africa | West Africa, Nigeria, Niger, Angola, German East Africa, Mozambique, Rhodesia, or South African Republic. Likely to be of Native or colonial heritage (colonial powers including Britain, Portugal and Germany). |"""

    if old_born_table in c:
        c = c.replace(old_born_table, new_born_table)
        changes += 1
        print("  [OK] Where Were You Born table")
    else:
        print("  [SKIP] Where Were You Born table - not found")

    # === 2. Family Background table (plain text -> table) ===
    old_family = """2D6 Family Background 2 you. Everyone you loved is long lost, dead, or far, far away.
There is no one left but 3 Your family was big until the curse. Death, madness and foolishness reduced them all to ruins, and you had no choice but to leave those who still survived behind.
4 You have lived alone as long as you can remember. Your family lies somewhere in your past and you don\u2019t really miss them.
5 Your family ain\u2019t big\u2014just you and a few scattered relatives. You don\u2019t always see eye to eye but for the most part you get on. Blood is blood, after all.
6 There\u2019s only you and one surviving relative left. Why you stick together neither of you knows, but everyone else is gone and you only have each other, even if you can\u2019t stand them (you gain a compadre).
7 You come from a huge extended family. But they hate you and cast you out. They may be local or far away, but they will chase you away if they ever see you again. Except for one sibling.
8 Your family is small but your folks are alive and maybe there\u2019s a younger sibling who lives with them. You don\u2019t always get on but that\u2019s family, ain\u2019t it?
9 You have a decent family, and feel part of a clan. One of your parents is still alive and your siblings have families of their own.
10 Your family is large but since Grandma died your Pa and your uncles have been at each other\u2019s throats over who heads the family.
11 Your family is tiny\u2014just you and one parent who has come to live with you (gain a compadre).
12 Your folks are dead and you\u2019re the eldest. The others look up to you to lead the family: maybe you want to, maybe you don\u2019t (you gain 1D2 compadres)."""

    new_family = """| 2D6 | Family Background |
| --- | --- |
| 2 | There is no one left but you. Everyone you loved is long lost, dead, or far, far away. |
| 3 | Your family was big until the curse. Death, madness and foolishness reduced them all to ruins, and you had no choice but to leave those who still survived behind. |
| 4 | You have lived alone as long as you can remember. Your family lies somewhere in your past and you don\u2019t really miss them. |
| 5 | Your family ain\u2019t big\u2014just you and a few scattered relatives. You don\u2019t always see eye to eye but for the most part you get on. Blood is blood, after all. |
| 6 | There\u2019s only you and one surviving relative left. Why you stick together neither of you knows, but everyone else is gone and you only have each other, even if you can\u2019t stand them (you gain a compadre). |
| 7 | You come from a huge extended family. But they hate you and cast you out. They may be local or far away, but they will chase you away if they ever see you again. Except for one sibling. |
| 8 | Your family is small but your folks are alive and maybe there\u2019s a younger sibling who lives with them. You don\u2019t always get on but that\u2019s family, ain\u2019t it? |
| 9 | You have a decent family, and feel part of a clan. One of your parents is still alive and your siblings have families of their own. |
| 10 | Your family is large but since Grandma died your Pa and your uncles have been at each other\u2019s throats over who heads the family. |
| 11 | Your family is tiny\u2014just you and one parent who has come to live with you (gain a compadre). |
| 12 | Your folks are dead and you\u2019re the eldest. The others look up to you to lead the family: maybe you want to, maybe you don\u2019t (you gain 1D2 compadres). |"""

    if old_family in c:
        c = c.replace(old_family, new_family)
        changes += 1
        print("  [OK] Family Background table")
    else:
        print("  [SKIP] Family Background table - not found")

    # === 3. Outlaw Living Outcome Table (plain text -> table) ===
    old_outlaw = """LIVING OUTCOME TABLE - OUTLAW Roll Formative event Abilities Talents Gear 1 You shoot a bank clerk in the back  SHOOTIN\u2019 1 cold blooded  or  Colt 45 Peacemaker & when you don\u2019t need to. You are not  MOVE 1  fast shooter 2D6 rounds only a killer, but a coward. Thrown  3D6 \u00d7 $1 out of the gang, your next roll on the  +1 Fame Living -2 Reputation s table has a -1 modifier.
2 You kill a man in a fair fight, you  FIGHTIN\u2019 1  brawler  or   Colt 1860 New Army have the respect of your peers. SHOOTIN\u2019 1 pugilist & 3D6 rounds 4D6 x $1 +1 Fame
-1 Reputation
3 You fight the gang leader and take  FIGHTIN\u2019 1 warcry  or   Colt Walker pistol & him down, you are the leader now. PRESENCE 1 authority 2D6 rounds 2D6 x $1 +2 compadres +1 Fame +1 Reputation 4 PRESENCE 1  lockpicker  or  Pair of Smith and You rob the union train. They will write up your short life in a dime  ANIMAL   sneak Wesson Model 3 pis- novel. HANDLIN\u2019 1 tols & 4D6 rounds 3D6 x $25 + 1 compadre +1 Fame
-1 Reputation
5 Set a thief to catch a thief. A law- HAWKEYE 1 two gun  or  A pair of Cooper pis- man from the nearby town turns you  INSIGHT 1 light-footed tols & 3D6 rounds against your gang, and you betray  American Quarter them. If you choose to progress to  Horse another Living, make your next roll  2D6 \u00d7 $1 on the Ranch Hand Living Out- come Table.
6+ After shooting down a rival who was  PRESENCE 1  quick draw  or  Sheriff badge terrorizing a local town , the towns- PERFORMIN\u2019 1 lightning fast Manhattan Navy & folk elect you as their sheriff. Make  2D6 rounds your next Living roll on the Trader  Hartford Coach Gun or Gentlefolk Table. & D6 Cartridges American Saddlebred Horse 3D6 \u00d7 $1"""

    new_outlaw = """**LIVING OUTCOME TABLE - OUTLAW**

| Roll | Formative event | Abilities | Talents | Gear |
| --- | --- | --- | --- | --- |
| 1 | You shoot a bank clerk in the back when you don\u2019t need to. You are not only a killer, but a coward. Thrown out of the gang, your next roll on the Livings table has a \u22121 modifier. +1 Fame, \u22122 Reputation | SHOOTIN\u2019 1, MOVE 1 | cold blooded or fast shooter | Colt 45 Peacemaker & 2D6 rounds, 3D6 \u00d7 $1 |
| 2 | You kill a man in a fair fight, you have the respect of your peers. +1 Fame, \u22121 Reputation | FIGHTIN\u2019 1, SHOOTIN\u2019 1 | brawler or pugilist | Colt 1860 New Army & 3D6 rounds, 4D6 \u00d7 $1 |
| 3 | You fight the gang leader and take him down, you are the leader now. +2 compadres, +1 Fame, +1 Reputation | FIGHTIN\u2019 1, PRESENCE 1 | warcry or authority | Colt Walker pistol & 2D6 rounds, 2D6 \u00d7 $1 |
| 4 | You rob the union train. They will write up your short life in a dime novel. +1 compadre, +1 Fame, \u22121 Reputation | PRESENCE 1, ANIMAL HANDLIN\u2019 1 | lockpicker or sneak | Pair of Smith and Wesson Model 3 pistols & 4D6 rounds, 3D6 \u00d7 $25 |
| 5 | Set a thief to catch a thief. A lawman from the nearby town turns you against your gang, and you betray them. If you choose to progress to another Living, make your next roll on the Ranch Hand Living Outcome Table. | HAWKEYE 1, INSIGHT 1 | two gun or light-footed | A pair of Cooper pistols & 3D6 rounds, American Quarter Horse, 2D6 \u00d7 $1 |
| 6+ | After shooting down a rival who was terrorizing a local town, the townsfolk elect you as their sheriff. Make your next Living roll on the Trader or Gentlefolk Table. | PRESENCE 1, PERFORMIN\u2019 1 | quick draw or lightning fast | Sheriff badge, Manhattan Navy & 2D6 rounds, Hartford Coach Gun & D6 Cartridges, American Saddlebred Horse, 3D6 \u00d7 $1 |"""

    if old_outlaw in c:
        c = c.replace(old_outlaw, new_outlaw)
        changes += 1
        print("  [OK] Outlaw Living Outcome Table")
    else:
        print("  [SKIP] Outlaw Living Outcome Table - not found")

    # === 4. Frontier Folk Living Outcome Table ===
    old_frontier = """### LIVING OUTCOME TABLE - FRONTIER FOLK

| Roll Formative event Abilities Talents Gear |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 Attacked by a bear you fight like a | NATURE 1 lucky | or | Spencer Carbine & |  |
| lion but are inevitably left for dead, | RESILIENCE 1 hard to hit 2D6 rounds |  |  |  |
| only to be found and saved by local Natives. Wild rations D6 \u00d7 $1 | Knife |  |  |  |
| 2 Your journeys across lakes and up | HAWKEYE 1 survivor | or | Canoe |  |
| rivers and taking meals with Native tribes has given you a broad knowl- 1868 & 3D6 rounds | NATURE 1 bow master Winchester Model |  |  |  |
| edge that you doubt any east coast university student can match. | 3D6 \u00d7 $1 |  |  |  |
| 3 You become a scout with the US Army. HAWKEYE 1 light-footed 1873 & 2D6 rounds Morgan Horse Sleeping roll Tobacco 6D6 \u00d7 $1 | SHOOTIN\u2019 1 tracker | or | Winchester Model |  |
| 4 You have spent so long wandering the trails and exploring the wilder- HANDLIN\u2019 1 born in the saddle Small tent | ANIMAL | companion | or | Astrolabe |
| ness that your horse has become | MAKIN\u2019 1 Survey equipment |  |  |  |
| your best friend and your maps of | Missouri Fox Trotter |  |  |  |
| the area are well regarded. 2D6 \u00d7 $10 | horse |  |  |  |
| 5 One particularly cold winter you are | FIGHTIN\u2019 1 man\u2019s best friend | or | Spencer Carbine & |  |
| attacked by a pack of wolves. Your | ANIMAL | guard dog 4D6 rounds |  |  |
| loyal dog saves you and together you | HANDLIN\u2019 1 Dog |  |  |  |
| drive the wolves away. 3D6 \u00d7 $1 | Sleeping roll |  |  |  |
| 6+ You used to come into town just to | MAKIN\u2019 1 animal hunter | or | Knife |  |"""

    new_frontier = """**LIVING OUTCOME TABLE - FRONTIER FOLK**

| Roll | Formative event | Abilities | Talents | Gear |
| --- | --- | --- | --- | --- |
| 1 | Attacked by a bear you fight like a lion but are inevitably left for dead, only to be found and saved by local Natives. | NATURE 1, RESILIENCE 1 | lucky or hard to hit | Spencer Carbine & 2D6 rounds, Knife, Wild rations, D6 \u00d7 $1 |
| 2 | Your journeys across lakes and up rivers and taking meals with Native tribes has given you a broad knowledge that you doubt any east coast university student can match. | HAWKEYE 1, NATURE 1 | survivor or bow master | Canoe, Winchester Model 1868 & 3D6 rounds, 3D6 \u00d7 $1 |
| 3 | You become a scout with the US Army. | SHOOTIN\u2019 1, HAWKEYE 1 | light-footed or tracker | Winchester Model 1873 & 2D6 rounds, Morgan Horse, Sleeping roll, Tobacco, 6D6 \u00d7 $1 |
| 4 | You have spent so long wandering the trails and exploring the wilderness that your horse has become your best friend and your maps of the area are well regarded. | ANIMAL HANDLIN\u2019 1, MAKIN\u2019 1 | companion or born in the saddle | Astrolabe, Small tent, Survey equipment, Missouri Fox Trotter horse, 2D6 \u00d7 $10 |
| 5 | One particularly cold winter you are attacked by a pack of wolves. Your loyal dog saves you and together you drive the wolves away. | FIGHTIN\u2019 1, ANIMAL HANDLIN\u2019 1 | man\u2019s best friend or guard dog | Spencer Carbine & 4D6 rounds, Dog, Sleeping roll, 3D6 \u00d7 $1 |
| 6+ | You used to come into town just to sell your furs. But it\u2019s warmer to sit and sew those furs. So now you sell clothes for the discerning outdoorsman. Make your next Living roll on the Trader Living Outcome Table. | MAKIN\u2019 1, HAWKEYE 1 | animal hunter or knife fighter | Knife, Outfit: Store with 1 Capital, 3D6 \u00d7 $1 |"""

    if old_frontier in c:
        c = c.replace(old_frontier, new_frontier)
        changes += 1
        print("  [OK] Frontier Folk Living Outcome Table")
    else:
        print("  [SKIP] Frontier Folk Living Outcome Table - not found")

    # === 5. Ranch Hand Living Outcome Table ===
    old_ranch = """### LIVING OUTCOME TABLE - RANCH HAND

| Roll Formative event Abilities Talents Gear |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1 One drunken night at the end of | ANIMAL | hay-maker | or | Webley British Bull- |
| cattle drive, you get into a violent | HANDLIN\u2019 | 1 brawler dog & 2D6 rounds |  |  |
| argument and kill a man with your | FIGHTIN\u2019 1 Club |  |  |  |
| bare hands. Make your next roll on the Outlaw Living Outcome Table. +1 Fame \u22121 Reputation | 3D6 \u00d7 $1 |  |  |  |
| 2 You get involved in a range war, | FIGHTIN\u2019 1 | sharpshooter | or | Winchester Model |
| and your boss is killed. If you want another Living you\u2019ll have to get an- Pistol & 3D6 rounds | SHOOTIN\u2019 1 expert fanning 1868 & D6 rounds |  |  |  |
| other job: roll again on the Livings table with a \u22121 modifier. +1 Fame | 6D6 \u00d7 $1 |  |  |  |
| 3 You become a wrangler looking after | ANIMAL | bronc buster | or | Lasso |
| the spare horses on the trail and learn to bust the broncos. NATURE 1 2D6 rounds Sleeping roll Mustang horse 4D6 \u00d7 $1 | HANDLIN\u2019 1 horse warrior Colt Peacemaker & |  |  |  |
| 4 You are put in charge of the chuck | MAKIN\u2019 1 charming | or | Wagon & Missouri |  |
| wagon, a well-respected role which | DOCTORIN\u2019 1 authority Fox Trotter |  |  |  |
| feeds and cares for the other hands | Sleeping roll |  |  |  |
| on the long cattle drives to the | 6D6 \u00d7 $1 |  |  |  |
| railway. The boys listen out for your booming voice calling them to chow down. | +1 compadre |  |  |  |
| 5 You bring a big herd to the railhead, | RESILIENCE 1 born in the saddle | or | Lasso |  |
| earning a decent reward and a few nights on the town. HANDLIN\u2019 1 Horse Sleeping roll 2D6 \u00d7 $10 | ANIMAL | roper American Quarter |  |  |
| 6+ It\u2019s time to strike out, set up your | LABOR 1 horse warrior | or | Lasso |  |
| own ranch and make the money | NATURE 1 defender Winchester Model |  |  |  |
| rather than work for them others. If | 1873 & 2d6 rounds |  |  |  |
| you have another Living make your | Outfit: Ranch with 1 |  |  |  |
| next roll on the Homesteader Living | Capital |  |  |  |
| Outcome Table. horse +1 compadre | American Saddlebred |  |  |  |"""

    new_ranch = """**LIVING OUTCOME TABLE - RANCH HAND**

| Roll | Formative event | Abilities | Talents | Gear |
| --- | --- | --- | --- | --- |
| 1 | One drunken night at the end of cattle drive, you get into a violent argument and kill a man with your bare hands. Make your next roll on the Outlaw Living Outcome Table. +1 Fame, \u22121 Reputation | ANIMAL HANDLIN\u2019 1, FIGHTIN\u2019 1 | hay-maker or brawler | Webley British Bulldog & 2D6 rounds, Club, 3D6 \u00d7 $1 |
| 2 | You get involved in a range war, and your boss is killed. If you want another Living you\u2019ll have to get another job: roll again on the Livings table with a \u22121 modifier. +1 Fame | FIGHTIN\u2019 1, SHOOTIN\u2019 1 | sharpshooter or expert fanning | Winchester Model 1868 & D6 rounds, Pistol & 3D6 rounds, 6D6 \u00d7 $1 |
| 3 | You become a wrangler looking after the spare horses on the trail and learn to bust the broncos. | ANIMAL HANDLIN\u2019 1, NATURE 1 | bronc buster or horse warrior | Lasso, Colt Peacemaker & 2D6 rounds, Sleeping roll, Mustang horse, 4D6 \u00d7 $1 |
| 4 | You are put in charge of the chuck wagon, a well-respected role which feeds and cares for the other hands on the long cattle drives to the railway. The boys listen out for your booming voice calling them to chow down. +1 compadre | MAKIN\u2019 1, DOCTORIN\u2019 1 | charming or authority | Wagon & Missouri Fox Trotter, Sleeping roll, 6D6 \u00d7 $1 |
| 5 | You bring a big herd to the railhead, earning a decent reward and a few nights on the town. | RESILIENCE 1, ANIMAL HANDLIN\u2019 1 | born in the saddle or roper | Lasso, American Quarter Horse, Sleeping roll, 2D6 \u00d7 $10 |
| 6+ | It\u2019s time to strike out, set up your own ranch and make the money rather than work for them others. If you have another Living make your next roll on the Homesteader Living Outcome Table. +1 compadre | LABOR 1, NATURE 1 | horse warrior or defender | Lasso, Winchester Model 1873 & 2D6 rounds, Outfit: Ranch with 1 Capital, American Saddlebred horse |"""

    if old_ranch in c:
        c = c.replace(old_ranch, new_ranch)
        changes += 1
        print("  [OK] Ranch Hand Living Outcome Table")
    else:
        print("  [SKIP] Ranch Hand Living Outcome Table - not found")

    # === 6. Frontier Folk tail (entry 6+ continued) ===
    # The entry 6+ text continues after the table we replaced above
    old_ff_tail = (
        "| sell your furs. But it\u2019s warmer to sit "
        "| HAWKEYE 1 knife fighter Outfit: Store with 1 |  |  |  |\n"
        "| and sew those furs. So now you sell "
        "clothes for the discerning outdoors- 3D6 \u00d7 $1 "
        "man. Make your next Living roll on the Trader Living Outcome Table "
        "| Capital |  |  |  |"
    )
    if old_ff_tail in c:
        c = c.replace(old_ff_tail, "")
        changes += 1
        print("  [OK] Removed Frontier Folk tail remnant")

    # === 7. Your Acquisitions table ===
    old_acq = """| Cash Roll the relevant number of dice to see how much cash you have in your pocket at the start of the game. Capital Total your Capital to see how much, if any, Capital you have. You must either immediately invest it in an outfit or property, or liquidate it into cold, hard cash (page 88). Fame Total up any Fame bonuses and add them to your base Fame score (page 101-102). Reputation Total up any negative and positive Reputation bonuses, and apply them to your place on the Reputation Table on page 102. Weapons If you have acquired a weapon go to page 110 to find its details. Roll the number of dice speci- you have on your belt. fied to see how much ammo Horse If you gain a horse go to page 120 to determine its stats, qualities and flaws. It comes with all the necessary equipment needed to ride it. If y g y page 92. Outfit ou have an Outfit refer to the rules on buildin our Outfits on |  |
| --- | --- |
| NPC Compadres pag e 103 to find out more about them. Other Gear Write anything else on your equipment list. | Your backstory will help you work out who your compadres are, and then follow the rules on |"""

    new_acq = """| Item | Details |
| --- | --- |
| Cash | Roll the relevant number of dice to see how much cash you have in your pocket at the start of the game. |
| Capital | Total your Capital to see how much, if any, Capital you have. You must either immediately invest it in an outfit or property, or liquidate it into cold, hard cash (page 88). |
| Fame | Total up any Fame bonuses and add them to your base Fame score (page 101\u2013102). |
| Reputation | Total up any negative and positive Reputation bonuses, and apply them to your place on the Reputation Table on page 102. |
| Weapons | If you have acquired a weapon go to page 110 to find its details. Roll the number of dice specified to see how much ammo you have on your belt. |
| Horse | If you gain a horse go to page 120 to determine its stats, qualities and flaws. It comes with all the necessary equipment needed to ride it. |
| Outfit | If you have an Outfit refer to the rules on building your Outfits on page 92. |
| NPC Compadres | Your backstory will help you work out who your compadres are, and then follow the rules on page 103 to find out more about them. |
| Other Gear | Write anything else on your equipment list. |"""

    if old_acq in c:
        c = c.replace(old_acq, new_acq)
        changes += 1
        print("  [OK] Your Acquisitions table")
    else:
        print("  [SKIP] Your Acquisitions table - not found")

    write("10-patience-is-a-virtue.md", c)
    print(f"\nCh10: {changes} changes applied and saved.")
    return changes


if __name__ == "__main__":
    print("=== Fixing Ch08 ===")
    ch08_count = fix_ch08()
    print("\n=== Fixing Ch10 ===")
    ch10_count = fix_ch10()
    print(f"\n=== TOTAL: {ch08_count + ch10_count} changes ===")
