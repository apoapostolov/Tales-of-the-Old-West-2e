"""Apply all remaining Section B and C edits to chapter 07."""
import re

filepath = r"c:\git-public\Tales-of-the-Old-West-2e\corebook\07-the-west-in-the-1870s.md"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

changes = 0

# ============================================================
# 1. After "provided for them." paragraph, add Scalp Bounties,
#    Boarding Schools, and Slavery Among Tribes sections
# ============================================================
old_end = 'provided for them.\n\n### Native American Naming Conventions'
new_end = '''provided for them.

### Scalp Bounties

The depth of violence directed at Native peoples went beyond warfare. Multiple states, territories, and the Mexican government offered cash bounties for Native American scalps. California, Texas, and several Mexican states all ran scalp bounty programs at various points. Professional scalp hunters\u2014men like James Kirker and John Joel Glanton\u2014made careers of it, leading gangs across the borderlands. They were not always particular about whose scalps they collected: Mexican civilians, including women and children, were also murdered and scalped for bounty payment. In some places the going rate was $25 for a warrior\u2019s scalp, $50 for a woman or child. These were not secret atrocities\u2014they were government-funded, publicly known, and carried out in broad daylight.

### The Boarding Schools

Beginning in the late 1870s, the US government pursued a policy of cultural annihilation through education. Native American children were forcibly removed from their families and sent to off-reservation boarding schools. The first and most infamous, the Carlisle Indian Industrial School, was founded in 1879 by Captain Richard Henry Pratt under the explicit philosophy: \u201cKill the Indian in him, and save the man.\u201d Children had their hair cut, their clothes burned, their names replaced with English ones. They were forbidden to speak their own languages or practice their religions, and were subjected to military-style discipline. Physical and sexual abuse was rampant. Disease spread through overcrowded dormitories. Many children simply died\u2014of tuberculosis, influenza, malnourishment, or despair. Mass graves have been discovered at former school sites across the country. Dozens of similar institutions followed Carlisle\u2019s model. The boarding school system operated for decades, severing generations from their languages, families, spiritual practices, and identities. Its wounds are still felt today.

### Slavery Among Native American Tribes

Historical honesty demands the uncomfortable acknowledgment that some Native American tribes practiced chattel slavery of African Americans, modeled on the same system used by white Southerners. This was particularly true among the Cherokee, Chickasaw, Choctaw, Creek, and Seminole\u2014the so-called \u201cFive Civilized Tribes\u201d\u2014some of whose wealthier members owned plantations and enslaved people. Some tribal members brought enslaved people with them on the Trail of Tears. The Cherokee Nation did not emancipate its enslaved people until 1863, and the integration of Black freedmen into tribal nations remained contentious for generations. The existence of Native slaveholding does not diminish or excuse the genocide inflicted upon Native peoples\u2014but it does complicate the narrative, and historical honesty requires that it be told.

### Native American Naming Conventions'''

# Search using the curly quote version
old_end_curly = old_end.replace('"', '\u201c').replace('"', '\u201d')
# Try both straight and curly versions
if old_end_curly in content:
    content = content.replace(old_end_curly, new_end)
    changes += 1
    print("1. Added scalp bounties, boarding schools, slavery among tribes sections (curly quotes)")
elif old_end in content:
    content = content.replace(old_end, new_end)
    changes += 1
    print("1. Added scalp bounties, boarding schools, slavery among tribes sections (straight quotes)")
else:
    # Try finding just the key transition
    search = 'provided for them.'
    idx = content.find(search)
    if idx >= 0:
        # Find the next ### heading
        next_section = content.find('### Native American Naming', idx)
        if next_section >= 0:
            old_bit = content[idx:next_section + len('### Native American Naming Conventions')]
            content = content.replace(old_bit, new_end.replace('provided for them.\n\n', search + '\n\n'))
            # Actually let's just insert before the naming conventions heading
            print(f"1. Found via index search, inserting new sections")
            changes += 1

if changes == 0:
    # Last resort - find by partial match
    marker_idx = content.find("provided for them")
    if marker_idx >= 0:
        naming_idx = content.find("### Native American Naming", marker_idx)
        if naming_idx >= 0:
            insert_text = '''\n
### Scalp Bounties

The depth of violence directed at Native peoples went beyond warfare. Multiple states, territories, and the Mexican government offered cash bounties for Native American scalps. California, Texas, and several Mexican states all ran scalp bounty programs at various points. Professional scalp hunters\u2014men like James Kirker and John Joel Glanton\u2014made careers of it, leading gangs across the borderlands. They were not always particular about whose scalps they collected: Mexican civilians, including women and children, were also murdered and scalped for bounty payment. In some places the going rate was $25 for a warrior\u2019s scalp, $50 for a woman or child. These were not secret atrocities\u2014they were government-funded, publicly known, and carried out in broad daylight.

### The Boarding Schools

Beginning in the late 1870s, the US government pursued a policy of cultural annihilation through education. Native American children were forcibly removed from their families and sent to off-reservation boarding schools. The first and most infamous, the Carlisle Indian Industrial School, was founded in 1879 by Captain Richard Henry Pratt under the explicit philosophy: \u201cKill the Indian in him, and save the man.\u201d Children had their hair cut, their clothes burned, their names replaced with English ones. They were forbidden to speak their own languages or practice their religions, and were subjected to military-style discipline. Physical and sexual abuse was rampant. Disease spread through overcrowded dormitories. Many children simply died\u2014of tuberculosis, influenza, malnourishment, or despair. Mass graves have been discovered at former school sites across the country. Dozens of similar institutions followed Carlisle\u2019s model. The boarding school system operated for decades, severing generations from their languages, families, spiritual practices, and identities. Its wounds are still felt today.

### Slavery Among Native American Tribes

Historical honesty demands the uncomfortable acknowledgment that some Native American tribes practiced chattel slavery of African Americans, modeled on the same system used by white Southerners. This was particularly true among the Cherokee, Chickasaw, Choctaw, Creek, and Seminole\u2014the so-called \u201cFive Civilized Tribes\u201d\u2014some of whose wealthier members owned plantations and enslaved people. Some tribal members brought enslaved people with them on the Trail of Tears. The Cherokee Nation did not emancipate its enslaved people until 1863, and the integration of Black freedmen into tribal nations remained contentious for generations. The existence of Native slaveholding does not diminish or excuse the genocide inflicted upon Native peoples\u2014but it does complicate the narrative, and historical honesty requires that it be told.

'''
            content = content[:naming_idx] + insert_text + content[naming_idx:]
            changes += 1
            print("1. Inserted new sections via index-based insertion")

# ============================================================
# 2. Add Five Civilized Tribes context in the table intro
# ============================================================
old_fct = "One of the so-called Five Civilized Tribes forcibly moved"
new_fct = 'One of the so-called Five Civilized Tribes\u2014a colonial label that implied other tribes were \u201cuncivilized,\u201d used to justify differential treatment and forced removal\u2014forcibly moved'
if old_fct in content:
    content = content.replace(old_fct, new_fct, 1)
    changes += 1
    print("2. Added Five Civilized Tribes context")
else:
    print("2. SKIPPED - Five Civilized Tribes text not found")

# ============================================================
# 3. Expand the Josiah Henson framing
# ============================================================
old_henson = '''That said, the "jolly times", such as they were, didn\u2019t prevent Henson from running away to Canada and escaping slavery in 1830.'''
new_henson = '''These moments were not evidence that slavery had a pleasant side. They were acts of psychological resistance\u2014survival strategies through which enslaved people carved out fragments of humanity in a system designed to deny them any. Henson was clear about this: the small comforts existed *despite* slavery\u2019s relentless brutality, not alongside it. The \u201cjolly times,\u201d such as they were, didn\u2019t prevent Henson from running away to Canada and escaping slavery in 1830.'''
# Try with various quote styles
for old_str in [old_henson, old_henson.replace('\u2019', "'"), old_henson.replace('"', '\u201c').replace('"', '\u201d')]:
    if old_str in content:
        content = content.replace(old_str, new_henson, 1)
        changes += 1
        print("3. Expanded Henson framing")
        break
else:
    # Try to find it by unique substring
    marker = "prevent Henson from running away"
    idx = content.find(marker)
    if idx >= 0:
        # Find the start of this sentence
        para_start = content.rfind("That said,", max(0, idx - 200), idx)
        if para_start >= 0:
            para_end = content.find('\n', idx)
            old_para = content[para_start:para_end]
            content = content[:para_start] + new_henson + content[para_end:]
            changes += 1
            print("3. Expanded Henson framing (via index)")
    else:
        print("3. SKIPPED - Henson text not found")

# ============================================================
# 4. Add sexual violence section after "The Experience of the Enslaved" sidebar
# ============================================================
old_slavery_end = "captured runaways were sure to be punished, often brutally, sometimes fatally._"
new_slavery_end = '''captured runaways were sure to be punished, often brutally, sometimes fatally._

> _One of the most pervasive and least discussed realities of slavery was the epidemic of sexual violence against enslaved women. Rape by slaveholders was legal, routine, and economically incentivized\u2014children born of these assaults were themselves enslaved, increasing the owner\u2019s \u201cproperty.\u201d This was not a marginal phenomenon; it was structural to the institution. Enslaved women had no legal recourse and no right to refuse. The DNA record confirms what the historical record long made clear: sexual exploitation of enslaved women was systematic and pervasive. It must be named for what it was._'''

if old_slavery_end in content:
    content = content.replace(old_slavery_end, new_slavery_end, 1)
    changes += 1
    print("4. Added sexual violence section")
else:
    # Try finding via unique text
    marker = "sometimes fatally._"
    idx = content.find(marker)
    if idx >= 0:
        insert_at = idx + len(marker)
        insert_text = '''

> _One of the most pervasive and least discussed realities of slavery was the epidemic of sexual violence against enslaved women. Rape by slaveholders was legal, routine, and economically incentivized\u2014children born of these assaults were themselves enslaved, increasing the owner\u2019s \u201cproperty.\u201d This was not a marginal phenomenon; it was structural to the institution. Enslaved women had no legal recourse and no right to refuse. The DNA record confirms what the historical record long made clear: sexual exploitation of enslaved women was systematic and pervasive. It must be named for what it was._'''
        content = content[:insert_at] + insert_text + content[insert_at:]
        changes += 1
        print("4. Added sexual violence section (via index)")
    else:
        print("4. SKIPPED - slavery sidebar end not found")

# ============================================================
# 5. Add Convict Leasing section after the Buffalo Soldiers paragraph
# ============================================================
old_buffalo = "which were active across the Southwest and Great Plains."
new_buffalo = '''which were active across the Southwest and Great Plains.

### Convict Leasing and the Black Codes

Freedom, for many, was short-lived in practice. Almost immediately after emancipation, Southern and Western states passed \u201cBlack Codes\u201d\u2014laws specifically designed to criminalize Black life and funnel freed people back into forced labor. Offenses such as vagrancy, loitering, being unemployed, or breaking curfew carried heavy sentences. Under the convict leasing system, prisoners were leased to private businesses\u2014mines, railroads, plantations, turpentine camps\u2014under conditions frequently worse than antebellum slavery. Leased convicts had no value to their employers beyond the term of the lease; there was no incentive to keep them alive. Mortality rates were staggering, sometimes exceeding 30\u201340% per year. The system was made legal by the Thirteenth Amendment\u2019s exception clause\u2014\u201cexcept as punishment for crime\u201d\u2014and persisted in various forms for decades. It was slavery by another name, and everyone knew it.'''

if old_buffalo in content:
    content = content.replace(old_buffalo, new_buffalo, 1)
    changes += 1
    print("5. Added convict leasing and Black Codes section")
else:
    print("5. SKIPPED - Buffalo Soldiers text not found")

# ============================================================
# 6. Add anti-Mexican violence/land theft to Mexico section
# ============================================================
old_mexico = "They continued to live their lives, run their haciendas, herd their cattle, tend their farms and carry on all the other business of day-to-day life. This, along with the Mexican\u2019s long and expert experience of living and working the land, may well have contributed to the strong anti-Mexican prejudice exhibited by the white settlers."

new_mexico = '''They continued to live their lives, run their haciendas, herd their cattle, tend their farms and carry on all the other business of day-to-day life.

In reality, treaty guarantees were worth little. The vast majority of Mexican-American families lost their land in the decades following the war\u2014through legal manipulation, discriminatory taxation, lengthy and expensive court battles in English-language courts they couldn\u2019t navigate, and outright intimidation and violence. Anglo squatters simply occupied Mexican-owned land and dared the owners to challenge them in courts stacked against them. The California Land Act of 1851 forced Mexican landowners to prove their titles in an American legal system designed to make that as difficult and expensive as possible; even those who won their cases were often bankrupted by legal fees. The Mexican-American\u2019s long and expert experience of living and working the land\u2014their deep knowledge of the country, their established communities, their success\u2014may well have intensified rather than moderated white resentment.

Anti-Mexican violence was pervasive and brutal. Between 1848 and 1928, thousands of Mexicans and Mexican Americans were lynched across the Southwest\u2014hanged, shot, burned, or beaten to death by mobs, vigilantes, and the Texas Rangers alike. The violence was racialized and systematic: Mexicans were driven from mining claims, expelled from towns, and murdered for their land. The \u201cCart War\u201d of 1857, in which Anglo teamsters murdered Mexican freighters to eliminate business competition, is just one example among hundreds. This is not peripheral history\u2014it is central to understanding the West.'''

if old_mexico in content:
    content = content.replace(old_mexico, new_mexico, 1)
    changes += 1
    print("6. Added anti-Mexican violence and land theft")
else:
    # Try with straight apostrophe
    old_mexico_alt = old_mexico.replace('\u2019', "'")
    if old_mexico_alt in content:
        content = content.replace(old_mexico_alt, new_mexico, 1)
        changes += 1
        print("6. Added anti-Mexican violence and land theft (alt quotes)")
    else:
        print("6. SKIPPED - Mexico paragraph not found")

# ============================================================
# 7. Expand Chinese Immigrants section massively
# ============================================================
old_chinese = """### Chinese Immigrants

Chinese immigrants were often impoverished peasants. They provided a significant part of the workforce building the railroads up to the 1870s, and were prominent in the California Gold Rush before that. Many returned to China after the work dried up, but those that remained worked in a wide variety of roles. However, hostility to Chinese immigrants was high in the West, prejudices built on racism and the fear that Chinese workers were stealing jobs from the whites. This hostility often forced the Chinese community into self-sufficient ghettos, called "Chinatowns". It also led to anti-Chinese riots in Los Angeles in 1871, and culminated in the Rock Springs Massacre in 1885 (with the murder of at least 28 Chinese) and the Chinese Massacre Cove in 1887 (with 34 people murdered)."""

new_chinese = """### Chinese Immigrants

Chinese immigrants began arriving in significant numbers during the California Gold Rush of 1849, and by the 1860s they made up the majority of the workforce building the Central Pacific Railroad. They blasted tunnels through the Sierra Nevada in brutal winter conditions, handled unstable nitroglycerin, and were paid less than their white counterparts for the most dangerous work. Hundreds died in avalanches, explosions, and accidents. When the railroad was completed at Promontory Summit in 1869, Chinese workers were excluded from the celebratory photograph.

Many returned to China after the work dried up, but those who remained found work in mining, agriculture, fishing, laundry, cooking, and other trades. Chinese communities established businesses, temples, and social organizations. But hostility was fierce, constant, and violent. White workers saw Chinese laborers as economic competition; politicians exploited anti-Chinese sentiment for votes; and the wider culture viewed the Chinese as racially inferior and culturally alien.

This hostility was not merely social\u2014it was legal. California\u2019s Foreign Miners\u2019 Tax, first passed in 1850, specifically targeted Chinese and Mexican miners. The Page Act of 1875 effectively barred Chinese women from entering the country, leaving Chinese communities overwhelmingly male and isolated. The Chinese Exclusion Act of 1882 went further, banning Chinese laborers entirely from immigrating and barring Chinese residents from naturalized citizenship. It was the first US law to exclude an entire ethnic group and remained in force until 1943.

Violence against the Chinese was widespread and devastating. Queue-cutting\u2014forcibly cutting off a Chinese man\u2019s braided queue, a deeply personal and culturally significant violation\u2014was a common form of harassment and humiliation. But the violence went far beyond that. In Los Angeles in 1871, a mob of around 500 white and Hispanic men rampaged through the Chinese community, murdering at least 18 people. At Rock Springs, Wyoming in 1885, white miners attacked the Chinese quarter, murdering at least 28 people, wounding 15, and burning 79 homes. At Chinese Massacre Cove on the Snake River in Oregon in 1887, a gang murdered 34 Chinese gold miners; the killers were identified and tried but acquitted, the bodies left unburied. These were not isolated incidents. Anti-Chinese riots, expulsions, and murders occurred in communities across the West, from Tacoma to Denver to Tombstone.

Forced into self-sufficient enclaves\u2014\u201cChinatowns\u201d\u2014by exclusion, discrimination, and the constant threat of violence, Chinese communities survived through resilience and mutual support. But the legal and social framework of the West was openly designed to exploit their labor while denying them any place in American society.

### Prostitution and Trafficking

Prostitution was one of the largest industries in Western towns and mining camps. In boomtowns where men outnumbered women ten or twenty to one, brothels, dance halls, and \u201ccribs\u201d\u2014tiny shacks where women received customers\u2014operated openly and were often the most profitable businesses in town. Some women entered the trade voluntarily, seeing it as the most lucrative option available in a society that offered women few economic alternatives. Many others were trafficked, coerced, or sold into sexual slavery.

Chinese women were particularly targeted. Kidnapped or purchased in China, they were shipped to the West Coast and sold to brothel owners, often for hundreds of dollars. They worked in conditions of brutal captivity\u2014locked in rooms, beaten for disobedience, and discarded when they were no longer profitable, left to die of disease or starvation. The Page Act of 1875, ostensibly aimed at preventing this trafficking, was used in practice to bar virtually all Chinese women from immigration, while doing little to help those already enslaved in American brothels.

Working conditions for prostitutes of all backgrounds ranged from the relatively comfortable parlor houses, where madams enforced some standards, to the unspeakable horror of the cribs and mining camp tents. Venereal disease was rampant. Violence from customers was routine. Laudanum and opium were used both as painkillers and tools of control. Most prostitutes had short, brutal working lives. The mythology of the \u201cgold-hearted saloon girl\u201d bears no resemblance to the grim reality for most women in the trade."""

# Try with both curly and straight quotes around Chinatowns
if old_chinese in content:
    content = content.replace(old_chinese, new_chinese, 1)
    changes += 1
    print("7. Expanded Chinese section and added prostitution section")
else:
    old_chinese_curly = old_chinese.replace('"Chinatowns"', '\u201cChinatowns\u201d')
    if old_chinese_curly in content:
        content = content.replace(old_chinese_curly, new_chinese, 1)
        changes += 1
        print("7. Expanded Chinese section (curly quotes)")
    else:
        # Try finding by header
        idx = content.find("### Chinese Immigrants")
        if idx >= 0:
            # Find next ### heading
            next_heading = content.find("\n###", idx + 5)
            if next_heading >= 0:
                content = content[:idx] + new_chinese + "\n" + content[next_heading:]
                changes += 1
                print("7. Expanded Chinese section (via index)")
            else:
                print("7. SKIPPED - couldn't find next heading after Chinese section")
        else:
            print("7. SKIPPED - Chinese Immigrants header not found")

# ============================================================
# 8. Add prostitution to Women section - actually already covered in Chinese section above
#    But add a note in the Women section about the darker side
# ============================================================
old_women_end = "but there were unique opportunities in the West that many women were able to take advantage of."
new_women_end = '''but there were unique opportunities in the West that many women were able to take advantage of.

That said, the reality for many women in the West was far darker. Domestic violence was rampant and almost never prosecuted. Women who were widowed, abandoned, or destitute faced a society with virtually no safety net. For a great many, the only economic option was prostitution\u2014a trade that was one of the largest industries in Western boomtowns and mining camps, and one that was often less a choice than a trap. The experience of women in the West cannot be honestly told without acknowledging both the opportunities and the exploitation.'''

if old_women_end in content:
    content = content.replace(old_women_end, new_women_end, 1)
    changes += 1
    print("8. Added darker reality to Women section")
else:
    print("8. SKIPPED - Women section end text not found")

# ============================================================
# Write the result
# ============================================================
with open(filepath, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)

print(f"\nDone. {changes} changes applied.")
