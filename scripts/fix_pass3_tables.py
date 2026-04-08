#!/usr/bin/env python3
"""Pass 3: Replace garbled tables with proper markdown tables.

Tables reconstructed from PDF visual inspection.
"""
from pathlib import Path

COREBOOK = Path(__file__).parent.parent / "corebook"

TROUBLE_PHYSICAL_NEW = """**Trouble Outcome Table - Conflict / Physical**

| D6 | 1 | 2 | 3 | 4+ |
|----|---|---|---|-----|
| 1 | Your gun or weapon suffers a random Condition, or an important item breaks. | You are bashed and battered. Suffer 1 point of either Hurts or Shakes (GM decides). | You catch yourself on your stirrup or other sharp object or bash into something hard. You suffer a 4 dice attack (Damage 1, Crit 2). | You\u2019re so shaken and shocked by events that, for the next Shift, you suffer Trouble on a roll of 1 or 2. You may recover by taking a Turn to draw breath and spending 2 Faith Points. |
| 2 | You stumble, slip or trip. Lose your next slow action. | You trip and fall or are thrown from your horse, and are Prone. A fall from height may cause further damage. | Hang fire. Your gun doesn\u2019t go off but then discharges next Round, or your blow is too slow. You lose your next Round coping with this. | Your action has gone catastrophically wrong. A key item of great value is broken beyond repair, or your horse or dog is killed. |
| 3 | You drop your weapon, lose your reins or otherwise lose your grip on something important. If it was keeping you upright or on your feet you may need to make a MOVE roll to avoid a worse outcome. | Your bullet was a dud, or your deadly blow wasn\u2019t as good as you thought. An otherwise successful attack does no damage. | You\u2019re shaken and shocked. For the rest of the scene you suffer \u22122 to all rolls using the ability that suffered the Trouble. | You trip and fall or are thrown from your horse, and are Prone. Take falling damage if the fall is far enough. You are Stunned for 1D6 Rounds minus the number of successes on a RESILIENCE test. |
| 4 | Your attack is underpowered, or your action is weak. Lose one success from your total. | You\u2019re badly shaken by the turn of events. Until the end of the scene, you suffer Trouble on a roll of 1 or 2, but may recover from this by taking a slow action to draw breath, and spending a Faith Point. | Your attack or action affects a random bystander or unintended target. Either apply the effect of the attack to that target, or they suffer a 6 dice attack (Damage 1, Crit 1). | Your attack or action has terribly affected a random nearby bystander. They are immediately Broken on Grit and suffer a critical injury. |
| 5 | You are thrown off balance. Lose your next Round. | Your action results in an impact on a random bystander or unintended target. They suffer a 4 dice attack (Damage 1, Crit 2). | Your gun explodes, your weapon breaks and slices into you, or your blow catches something sharp. You suffer a 6 dice attack, either with Damage and Critical rating of your weapon or Damage 1, Crit 1. | You have bashed yourself terribly in some way and are immediately Broken on Grit. |
| 6 | Your Troubles are mounting\u2014reroll on the next column. | Your Troubles are mounting\u2014reroll on the next column. | Your Troubles are mounting\u2014reroll on the next column. | You have bashed yourself terribly in some way and are immediately Broken on Quick. |

"""

TROUBLE_MENTAL_NEW = """**Trouble Outcome Table - Mental / Social**

| D6 | 1 | 2 | 3 | 4+ |
|----|---|---|---|-----|
| 1 | You have upset someone with your words or actions: they react badly towards you, laugh at you or show you no respect. Suffer a \u22121 penalty to your next roll when dealing with this person. | Your confidence is badly shaken. Suffer 1 point of either Vexes or Doubts (GM decides). | You get so frustrated that you suffer 1 point of both Vexes and Doubts. | You\u2019re so shaken and shocked by events that, for the next Shift, you suffer Trouble on a roll of 1 or 2. You may recover by taking a Turn to draw breath and spending 2 Faith Points. |
| 2 | You get tongue-tied or lose your thread. Lose your next slow action. | You\u2019re tongue-tied. You suffer a \u22121 penalty on all ability rolls relating to social or mental tests for the rest of the scene. | You struggle to cope with the situation. Lose your next Round to compose yourself. | You have mortally offended someone with your words or actions. They will hold a grudge forever. |
| 3 | You\u2019re confused, your mind goes blank, or you lose your train of thought. You suffer a \u22121 penalty to rolls relating to the same issue for the rest of the scene. | Either directly or through the grapevine, people know of your bad showing. Your Reputation moves one point in a negative direction. | Your actions seem so disrespectful or disgraceful that a nearby NPC slaps or punches you to put you in your place. | Your confidence is gone. You stutter and stumble and are effectively Stunned for 1D6 Rounds minus the number of successes on a PERFORMIN\u2019 test. |
| 4 | They know you\u2019re faking it, and you know they know you\u2019re faking it. Lose one success from your total. | You\u2019re badly shaken by the turn of events. Until the end of the scene, you suffer Trouble on a roll of 1 or 2, but may recover by taking a slow action to draw breath and spending a Faith Point. | Things are going badly wrong, and you can\u2019t cope. You need a Turn to pull yourself together. | Your abject behavior gets around town in a flash. Your Fame increases by one, but your Reputation moves three points in a negative direction. |
| 5 | Your words or actions have gone down very badly, and you bluster to cover it up. Lose your next Round. | You\u2019ve made such a pig\u2019s ear of the situation that the object of your efforts dismisses you. You cannot try to influence them again for at least 24 hours. | The shameful experience scars you, and you suffer a 6 dice attack (Damage 1), the damage split between Doubts and Vexes. | Your efforts have gone so disastrously wrong you are immediately Broken on Cunning. This makes you upset, angry or in some other way distraught. Roleplay the outcome. |
| 6 | Your Troubles are mounting\u2014reroll on the next column. | Your Troubles are mounting\u2014reroll on the next column. | Your Troubles are mounting\u2014reroll on the next column. | Your efforts have gone so disastrously wrong you are immediately Broken on Docity. This makes you doubtful, confused, or distraught. Roleplay the outcome. |

"""


def main():
    ch03 = COREBOOK / "03-rolling-the-bones.md"
    text = ch03.read_text(encoding="utf-8")

    phys_start = text.find("**Trouble Outcome Table - Conflict / Physical**")
    mental_start = text.find("**Trouble Outcome Table - Mental / Social**")
    modifications = text.find("### Modifications", mental_start)

    if phys_start < 0 or mental_start < 0 or modifications < 0:
        print("ERROR: Could not find table markers")
        return

    new_text = (
        text[:phys_start]
        + TROUBLE_PHYSICAL_NEW
        + TROUBLE_MENTAL_NEW
        + text[modifications:]
    )

    ch03.write_text(new_text, encoding="utf-8")
    print(f"Reconstructed 2 Trouble Outcome Tables in {ch03.name}")
    print(f"  Physical: 6 rows x 4 columns")
    print(f"  Mental/Social: 6 rows x 4 columns")


if __name__ == "__main__":
    main()
