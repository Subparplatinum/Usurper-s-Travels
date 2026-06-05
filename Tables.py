import Armoury
import random
from HelperFunctions import allLore

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
mageKnight = [Armoury.KotFFStats,None,None,Armoury.sunAttune,None,None,"Knight of the First Flame","enemy",True,allLore["mageKnight"]]
                                                                                                                 
fireball = [Armoury.fireballStats,None,Armoury.fireballExplode,None,None,Armoury.spellBoots,"Fireball","enemy",True]                                                                                                                                                                                                                             

winter = [Armoury.silentNight,None,None,Armoury.frostPlate,Armoury.elfLeggings,Armoury.spellBoots,"The King of Winter","enemy",True,allLore["winter"]]
winterguard = [Armoury.winterguard,None,None,None,None,None,"Winterguard","enemy",True]
friendWinterguard = [Armoury.winterguard,None,None,None,None,None,"Winterguard","ally",True]

mass = [Armoury.longsword,None,None,Armoury.core,Armoury.endlessGrowths,None,"Ooglesh, the Primordial Ooze","enemy",False,allLore["mass"]]

lethe = [Armoury.LetheStats,None,Armoury.LetheStats2,None,None,None,"Lethe, Lord of Dusk","enemy",False,allLore["lethe"]]

umbralLegate = [Armoury.legateStats,None,None,None,None,None,"Umbral Legate","enemy",False]

prideDaughter = [Armoury.corruptStats,Armoury.prideStats,None,None,None,None,"Daughter of Pride","enemy",False,allLore["DoC"]]
slothDaughter = [None,Armoury.slothStats,None,None,None,None,"Daughter of Sloth","enemy",False]
envyDaughter = [Armoury.corruptStats,Armoury.envyStats,None,None,None,None,"Daughter of Envy","enemy",False]

#super bosses (has extra field for title card)                                                                  
raah = [Armoury.severingblade,None,Armoury.starScar,Armoury.raahAttire,Armoury.raahTrousers,Armoury.starWalker,"Raah, the Pretender ","enemy",True,allLore["raah"]]
                                                                                                                                                     
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

usurper = [random.choice(weapons),random.choice(weapons),random.choice(helmets),random.choice(breastplates),random.choice(leggings),random.choice(boots),"False Usurper ","enemy",False,allLore["usurper"]]
                                                                                                                                                                                   
                                                                                                                                                   


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
lifeBoss = [[prideDaughter,slothDaughter,envyDaughter],"sprites/greattree/","music/Daughter of Corruption.mp3","Guijao's Curse",5,Armoury.daughterLootTable]

#superbosstables
mageSuperBoss = [[raah],"sprites/throne/","music/Heolstor 1.mp3","'Burning Vengeance'",6,None]
usurperSuperBoss = [[usurper],"sprites/throne/","music/Heolstor 1.mp3","'Burning Vengeance'",6,None]

#all spawntables
spawnTables = [solarKnights,solarKnights,darkness,darkness,newNorth,newNorth2]

bossTables = [solarBoss,darkBoss,northBoss,darkBoss2,lifeBoss]

superBossTables = [mageSuperBoss,usurperSuperBoss]


#debug
#bossTables = [lifeBoss,lifeBoss,lifeBoss]
#spawnTables = [newNorth2]
#superBossTables = [usurperSuperBoss]