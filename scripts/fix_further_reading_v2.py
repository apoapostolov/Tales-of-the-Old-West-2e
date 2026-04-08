"""
Replace the Further Reading bullet list with annotated entries.
Also fixes the split "And Still The Waters Run" entry.
"""

import re

filepath = r'c:\git-public\Tales-of-the-Old-West-2e\corebook\07-the-west-in-the-1870s.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

OLD_BLOCK = """### Further Reading

- _The Cheyenne Indians_ by George Bird Grinnell
- _Bury My Heart at Wounded Knee_ by Dee Brown
- _Blood and Thunder_ by Hampton Sides
- _Empire of the Summer Moon_ by S.C. Gwynne
- _The Real Deadwood_ by John Edward Ames
- _Dodge City_ by Tom Clavin
- _Gunfighters, Highwaymen and Vigilantes_ by Roger D. McGrath
- _The Worst Hard Time_ by Timothy Egan
- _Lonesome Dove_ by Larry McMurtry _(fiction, but more honest about cowboy life than most history books)_
- _Roughing It_ by Mark Twain
- _Killers of the Flower Moon_ by David Grann
- _The Indifferent Stars Above_ by Daniel James Brown _(on the Donner Party)_
- _Massacre at Mountain Meadows_ by Walker, Turley, and Leonard
- _One Vast Winter Count_ by Colin G. Calloway
- _Driven Out_ by Jean Pfaelzer _(on anti-Chinese violence)_
- _The Devil in the White City_ by Erik Larson _(Gilded Age context)_
- _Slavery by Another Name_ by Douglas A. Blackmon _(on convict leasing)_
- _1491_ by Charles C. Mann
- _Impressions of an Indian Childhood_ by Zitkala Sa
- _The Earth is Weeping_ by Peter Cozzens
- _Black Elk Speaks_ as told through John Neihardt by Nicholas Black Elk
- _The Rediscovery of America_ by Ned Blackhawk
- And Still The Waters Run by Angie Debo
- _The Mammoth Book of Native Americans_ edited by Jon E. Lewis
- _New Mexico, A History_ by Sanchez, Spude and Gomez
- _The Historical Atlas of Native Americans_ by Dr. Ian Barnes
- _River of Blood_ edited by Richard Cahan & Michael Williams
- _American Slavery_ by Peter Kolchin
- _Uncle Tom's Story of His Life_ \u2014An Autobiography of Reverend Josiah Henson by Josiah Henson
- _Black Cowboys in the American West_ edited by Glasrud and Searles
- _The Wild West_ by Frederick Nolan
- _Cult of Glory\u2014the Bold and Brutal History of the Texas Rangers_ by Doug J. Swanson
- _Mexicanos_ by Manuel G Gonzalez
- The Cherokee Nation Youtube: https://www. youtube.com/channel/UCRX-8MCNvhzPMejv4oi_FRA"""

NEW_BLOCK = """### Further Reading

- _The Cheyenne Indians_ by George Bird Grinnell \u2014 A dense ethnographic study of Cheyenne culture, kinship, warfare, ceremony, and daily life by a man who lived among them. Essential for GMs portraying Cheyenne characters or running campaigns in Cheyenne territory.
- _Bury My Heart at Wounded Knee_ by Dee Brown \u2014 The defining account of the systematic destruction of Native American civilisations from the Native perspective. Every GM running any story involving Native peoples should read this first.
- _Blood and Thunder_ by Hampton Sides \u2014 Kit Carson, the conquest of the Southwest, and the collision between the US Army and the Navajo and Apache nations. Vivid, balanced, and essential for New Mexico campaigns.
- _Empire of the Summer Moon_ by S.C. Gwynne \u2014 The rise and fall of the Comanche Empire, told through the story of Quanah Parker. The most readable account of Comanche power, raiding culture, and the brutal end of their dominance of the southern plains.
- _The Real Deadwood_ by John Edward Ames \u2014 The actual history behind the legends of Deadwood: the mining camp, the characters, the violence, and the economics that drove it. Good grounding before any Black Hills campaign.
- _Dodge City_ by Tom Clavin \u2014 The cattle town at its wildest, following Wyatt Earp, Bat Masterson, Doc Holliday, and the full cast of Dodge's glory years. Useful for players and GMs wanting to understand what a trail-end cow town actually felt and operated like.
- _Gunfighters, Highwaymen and Vigilantes_ by Roger D. McGrath \u2014 A scholarly examination of violence in frontier California mining towns that challenges popular myths. GMs will find its data on actual crime rates, vigilante behaviour, and frontier justice mechanics invaluable.
- _The Worst Hard Time_ by Timothy Egan \u2014 The Great Plains through drought and the Dust Bowl. Though set in the 1930s, it is the best account of what the land does to the people who try to farm it \u2014 essential for understanding homesteader campaigns.
- _Lonesome Dove_ by Larry McMurtry \u2014 Fiction, and the finest novel ever written about the West. A cattle drive from Texas to Montana that captures cowboy life, friendship, violence, and the cost of the frontier dream with more honesty than most history books. Read it for tone.
- _Roughing It_ by Mark Twain \u2014 Twain\u2019s autobiographical account of his time in Nevada and the West in the 1860s \u2014 funny, sharp, and revelatory about mining camps, stagecoaches, con men, and the texture of frontier society. Excellent for capturing the era\u2019s voice.
- _Killers of the Flower Moon_ by David Grann \u2014 The Osage murders of the 1920s and the systematic theft of Osage oil wealth through a campaign of assassination. Reveals how legal and extralegal systems combined to dispossess a people who had done everything right.
- _The Indifferent Stars Above_ by Daniel James Brown \u2014 The Donner Party in forensic, harrowing detail. Essential reading for any GM running a trail west scenario or wanting to understand what true frontier survival looked like at its worst.
- _Massacre at Mountain Meadows_ by Walker, Turley, and Leonard \u2014 The definitive scholarly account of the 1857 massacre of a wagon train by Mormon militiamen. Important for understanding religious violence, frontier justice, and the Mormon question in territorial America.
- _One Vast Winter Count_ by Colin G. Calloway \u2014 A comprehensive history of the Native American West from pre-contact through the nineteenth century, covering dozens of nations. The broadest and most balanced single-volume scholarship on the subject.
- _Driven Out_ by Jean Pfaelzer \u2014 The systematic expulsion of Chinese communities from Western towns and cities through organised violence, arson, and legislation. Essential for GMs running any story involving Chinese characters or anti-Chinese conflict.
- _The Devil in the White City_ by Erik Larson \u2014 Chicago\u2019s 1893 World\u2019s Fair alongside a serial killer operating within it. Gilded Age America rendered in extraordinary detail \u2014 useful context for the economic ambition and social rot of the era.
- _Slavery by Another Name_ by Douglas A. Blackmon \u2014 How convict leasing and the Black Codes recreated slavery in everything but name after the Civil War. Required reading for any campaign involving Black characters navigating life in the post-war South or West.
- _1491_ by Charles C. Mann \u2014 What the Americas were like before European contact \u2014 complex, populous, sophisticated civilisations largely erased from popular understanding. Reframes Native American history from the ground up.
- _Impressions of an Indian Childhood_ by Zitkala Sa \u2014 A memoir by a Yankton Sioux woman about growing up on a reservation and being taken to a boarding school. First-hand, literary, devastating. The only voice in this list that is both primary source and literature.
- _The Earth is Weeping_ by Peter Cozzens \u2014 The most comprehensive single-volume history of the Indian Wars from both sides, covering every major campaign. GMs running military or Native resistance scenarios will find it indispensable.
- _Black Elk Speaks_ as told through John Neihardt by Nicholas Black Elk \u2014 The spiritual autobiography of an Oglala Lakota holy man. Essential for understanding Lakota cosmology, the Ghost Dance, and the inner life of a people facing the destruction of their world.
- _The Rediscovery of America_ by Ned Blackhawk \u2014 An award-winning retelling of Native American history from the Native perspective, spanning centuries and challenging the standard colonial narrative at every turn.
- _And Still The Waters Run_ by Angie Debo \u2014 The dispossession of the Five Civilised Tribes in Oklahoma through the allotment process \u2014 a meticulous account of legal fraud on a massive scale. Essential for Indian Territory campaigns.
- _The Mammoth Book of Native Americans_ edited by Jon E. Lewis \u2014 A wide-ranging anthology of primary sources, first-hand accounts, and essays covering many tribes and periods. Good for dipping into specific nations or events without committing to a single scholarly work.
- _New Mexico, A History_ by Sanchez, Spude and Gomez \u2014 Regional history of New Mexico from Spanish colonial times through US territorial period and statehood. Essential for the New Mexico Campaign chapter and any Nuevomexicano storylines.
- _The Historical Atlas of Native Americans_ by Dr. Ian Barnes \u2014 Maps, timelines, and visual reference for tribal territories, migration patterns, and historical events across North America. Invaluable for GMs who think spatially.
- _River of Blood_ edited by Richard Cahan & Michael Williams \u2014 A photographic and documentary record of racial violence in America. Confronting and necessary context for any campaign that deals honestly with this history.
- _American Slavery_ by Peter Kolchin \u2014 A comprehensive scholarly overview of American slavery from colonial origins through the Civil War. Provides the economic, legal, and human framework that explains much of what drives conflict in the post-war West.
- _Uncle Tom\u2019s Story of His Life_ by Josiah Henson \u2014 The autobiography that partly inspired _Uncle Tom\u2019s Cabin_. A first-hand account of slavery, escape, and survival that grounds the history in a single life lived through it.
- _Black Cowboys in the American West_ edited by Glasrud and Searles \u2014 Essays on the history of Black cowboys, who made up roughly a quarter of all trail hands. Challenges the whitewashed mythology and gives players and GMs a richer picture of who actually rode the range.
- _The Wild West_ by Frederick Nolan \u2014 A broad, well-illustrated overview of the Wild West era covering outlaws, lawmen, range wars, and key events. A good general reference and starting point.
- _Cult of Glory \u2014 the Bold and Brutal History of the Texas Rangers_ by Doug J. Swanson \u2014 A forensic account of the Texas Rangers\u2019 actual history, including their systematic violence against Mexican Americans and Native peoples. Essential for any Texas campaign that wants to use the Rangers as more than cardboard heroes.
- _Mexicanos_ by Manuel G. Gonzalez \u2014 A history of Mexican Americans from the colonial era through the twentieth century. Required reading for campaigns involving Tejano, Nuevomexicano, or California vaquero characters and communities.
- The Cherokee Nation YouTube channel (https://www.youtube.com/channel/UCRX-8MCNvhzPMejv4oi_FRA) \u2014 Primary source videos produced by the Cherokee Nation covering their history, culture, and ongoing sovereignty. Accessible, authoritative, and free."""

start = content.find('### Further Reading\n')
end   = content.find('### States of the West\n')
if start == -1 or end == -1:
    raise ValueError('Markers not found')

content_new = content[:start] + NEW_BLOCK + '\n\n' + content[end:]
content_new = re.sub(r'\n{3,}', '\n\n', content_new)

with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content_new)

print(f"Done. {len(content):,} -> {len(content_new):,} chars")
