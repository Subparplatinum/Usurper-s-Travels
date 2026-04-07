import Armoury
import random

#all enemies now have a NEW FIELD which dictates if theyre a light source or not

#Northern Tribes
direWolf = [Armoury.iceClaw,Armoury.iceClaw,Armoury.beastFangs,None,None,None,"Direwolf","enemy",False]
beserker = [Armoury.bloodyAxe,Armoury.bloodyAxe,Armoury.warMask,None,None,None,"Beserker","enemy",False]
kralBreeder = [Armoury.iceWhistle,None,None,Armoury.iceHide,Armoury.fur,Armoury.frostHooves,"Hunter","enemy",False]

#Solar Knights
swordsman = [Armoury.swordsmanStats,None,None,None,None,None,"Inquisitor","enemy",True]
crossbowman = [Armoury.crossbowmanStats,None,None,None,None,None,"Assassin","enemy",True]
solarPriest = [Armoury.solarPriestStats,None,None,None,None,None,"Solar Priest","enemy",True]

#Children of the Dark
darkwalker = [Armoury.darkwalkerStats,None,None,None,None,None,"Darkwalker","enemy",False]
pit = [Armoury.pitStats,None,None,None,None,None,"Deep Frigid Hole","enemy",False]
phalanxGrowth = [Armoury.phalanxGrowthStats,None,None,None,None,None,"Chitinous Sludge","enemy",False]
ballistaGrowth = [Armoury.BallistaGrowthStats,None,None,None,None,None,"Spiked Sludge","enemy",False]

#New North
peasant = [Armoury.peasantStats,None,Armoury.peasantStats2,None,None,None,"Feral Peasant","enemy",False]
razorKnight = [Armoury.razorKnightStats,None,Armoury.razorKnightStats2,None,None,None,"Razor Knight","enemy",True]
cultist = [Armoury.cultistStats,None,None,None,None,None,"Blood Star Cultist","enemy",True]

#bosses (has extra field for title card)
mageKnight = [Armoury.KotFFStats,None,None,Armoury.sunAttune,None,None,"Knight of the First Flame","enemy",True,["'Burning Vengeance' - the floating citadel-ship from which Raah coordinates his armies,",
                                                                                                                 "swarms with his finest soldiers. Some of them stand before you now - a knight and their",
                                                                                                                 "comrades. All of them are Sun-Elves, and their armour is decorated with ostentatious",
                                                                                                                 "golden ornamentation that glows with their inner radiance. Yet their looks are deceiving,",
                                                                                                                 "for they are servants of Solei, and their souls have been blackened by the ash of the",
                                                                                                                 "countless innocents consumed in the fires of Raah's crusade.",""]]
                                                                                                                 
fireball = [Armoury.fireballStats,None,Armoury.fireballExplode,None,None,Armoury.spellBoots,"Fireball","enemy",True]                                                                                                                                                                                                                             

winter = [Armoury.silentNight,None,None,Armoury.frostPlate,Armoury.elfLeggings,Armoury.spellBoots,"The King of Winter","enemy",True,["Here sits an empty vessel, a failed experiment, left to rule over a starless, bloodsoaked",
                                                                                                                                "realm, abandoned by their cold creator.",""]]
winterguard = [Armoury.winterguard,None,None,None,None,None,"Winterguard","enemy",True]
friendWinterguard = [Armoury.winterguard,None,None,None,None,None,"Winterguard","ally",True]

mass = [Armoury.longsword,None,None,Armoury.core,Armoury.endlessGrowths,None,"Ooglesh, the Primordial Ooze","enemy",False,["Here bubbles the First Child of Darkness, once kept at bay by a thousand divine star-fires.",""]]

lethe = [Armoury.LetheStats,None,Armoury.LetheStats2,None,None,None,"Lethe, Lord of Dusk","enemy",False,['Here sits a decrepit old man clad in tattered rags. "I am Lethe, Lord of the Dusk Age, and the', 
                                                                                                   'world is mine to drown in darkness!" he yells, as he rises and waves his rusted shortsword in',
                                                                                                   'the air. You conclude this man obviously poses no threat to you, so you turn to walk away.','','...then the world goes black...','']]

umbralLegate = [Armoury.legateStats,None,None,None,None,None,"Umbral Legate","enemy",False]

#super bosses (has extra field for title card)                                                                  
raah = [Armoury.severingblade,None,Armoury.starScar,Armoury.raahAttire,Armoury.raahTrousers,Armoury.starWalker,"Raah, the Pretender ","enemy",True,["Here sits the final obstacle of your travels",
                                                                                                                                                     "The Chosen of the First Flame,",
                                                                                                                                                     "The Starbane,",
                                                                                                                                                     "Pretender.",
                                                                                                                                                     "Strike him down, and take from him the throne he does not deserve",""]]
                                                                                                                                                     
weapons = []
helmets = []
breastplates = []
leggings = []
boots = []

def sort(equipment):
    if equipment != None:
        if equipment.equipType == "weapon":
            weapons.append(equipment)
        elif equipment.equipType == "helmet":
            helmets.append(equipment)
        elif equipment.equipType == "breastplate":
            breastplates.append(equipment)
        elif equipment.equipType == "leggings":
            leggings.append(equipment)
        elif equipment.equipType == "boots":
            boots.append(equipment)
        

                                         
for equipment in Armoury.lootTable:
    sort(equipment)

usurper = [random.choice(weapons),random.choice(weapons),random.choice(helmets),random.choice(breastplates),random.choice(leggings),random.choice(boots),"False Usurper ","enemy",False,["The final obstacle of your travels lies in a pool of his own burning blood. Raah is already",
                                                                                                                                                                                   "slain, and on his throne sits one of your kindred, basking in Solei's mournful dusk-glow.",
                                                                                                                                                                                   "As Solei shrinks in the sky, abandoning the dying world that has yet again slain their champion,",
                                                                                                                                                                                   "you step forward to confront this False Usurper, and claim the throne that is rightfully yours.",
                                                                                                                                                                                   "Khurgan cares not for who or what is sacrificed in his name, only that sacrifices are made.",""]]
                                                                                                                                                                                   
                                                                                                                                                   


#spawntables - split into the actual spawn table and the sprites for the map
solarKnights = [[swordsman,crossbowman,solarPriest],"sprites/hrocharad/","The Radiant City"]

#north = [[direWolf,beserker,kralBreeder],"sprites/north/","The North"]
newNorth = [[peasant,razorKnight,cultist],"sprites/north/","The North"]
newNorth2 = [[peasant,razorKnight,cultist,friendWinterguard],"sprites/north/","The North"]

darkness = [[darkwalker,pit],"sprites/forest/","Cave"]

#bosstables
#all enemies after the first will be ads
# I have no idea what the number in the second to last field does, but im scared to take it out so it stays in
solarBoss = [[mageKnight,swordsman,swordsman,solarPriest],"sprites/throne/","music/Servant of Jealous Fire.mp3","'Burning Vengeance'",1,Armoury.mageknightLootTable]
northBoss = [[winter,winterguard,winterguard,winterguard],"sprites/north/","music/Frozen Monarch.mp3","The Starless Citadel",0,Armoury.winterLootTable]
darkBoss = [[mass,ballistaGrowth,ballistaGrowth,ballistaGrowth],"sprites/forest/","music/Creature of Darkness.mp3","Impact Site",4,Armoury.massLootTable]
darkBoss2 = [[lethe,umbralLegate,umbralLegate,umbralLegate],"sprites/darkness/","music/Deluded Old Man.mp3","The Umbral Wood",5,Armoury.letheLootTable]

#superbosstables
mageSuperBoss = [[raah],"sprites/throne/","music/Heolstor 1.mp3","'Burning Vengeance'",6,None]
usurperSuperBoss = [[usurper],"sprites/throne/","music/Heolstor 1.mp3","'Burning Vengeance'",6,None]

#all spawntables
spawnTables = [solarKnights,solarKnights,darkness,darkness,newNorth,newNorth2]

bossTables = [solarBoss,darkBoss,northBoss,darkBoss2]

superBossTables = [mageSuperBoss,usurperSuperBoss]

#debug
#bossTables = [solarBoss,solarBoss,solarBoss]
#spawnTables = [newNorth2]
#superBossTables = [usurperSuperBoss]