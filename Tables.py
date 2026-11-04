import Armoury
import random
from HelperFunctions import allLore

#all enemies now have a NEW FIELD which dictates if theyre a light source or not
#added another new field for sprite paths

#Northern Tribes
direWolf = [Armoury.iceClaw,Armoury.iceClaw,Armoury.beastFangs,None,None,None,"Direwolf","enemy",False,None]
beserker = [Armoury.bloodyAxe,Armoury.bloodyAxe,Armoury.warMask,None,None,None,"Beserker","enemy",False,None]
kralBreeder = [Armoury.iceWhistle,None,None,Armoury.iceHide,Armoury.fur,Armoury.frostHooves,"Hunter","enemy",False,None]

#Solar Knights
swordsman = [Armoury.swordsmanStats,None,None,None,None,None,"Inquisitor","enemy",True,None]
crossbowman = [Armoury.crossbowmanStats,None,None,None,None,None,"Assassin","enemy",True,None]
solarPriest = [Armoury.solarPriestStats,None,None,None,None,None,"Solar Priest","enemy",True,None]

#Children of the Dark
darkwalker = [Armoury.darkwalkerStats,None,None,None,None,None,"Darkwalker","enemy",False,None]
pit = [Armoury.pitStats,None,None,None,None,None,"Deep Frigid Hole","enemy",False,None]
phalanxGrowth = [Armoury.phalanxGrowthStats,None,None,None,None,None,"Chitinous Sludge","enemy",False,None]
ballistaGrowth = [Armoury.BallistaGrowthStats,None,None,None,None,None,"Spiked Sludge","enemy",False,None]

#New North
peasant = [Armoury.peasantStats,None,Armoury.peasantStats2,None,None,None,"Feral Peasant","enemy",True,"feralPeasant.png"]
razorKnight = [Armoury.razorKnightStats,None,Armoury.razorKnightStats2,None,None,None,"Razor Knight","enemy",True,"razorKnight.png"]
cultist = [Armoury.cultistStats,None,None,None,None,None,"Blood Star Cultist","enemy",True,None]

#bosses (has extra field for title card)
mageKnight = [Armoury.KotFFStats,None,None,Armoury.sunAttune,None,None,"Solar Knight","enemy",True,None,allLore["mageKnight"]]
                                                                                                                 
fireball = [Armoury.fireballStats,None,Armoury.fireballExplode,None,None,Armoury.spellBoots,"Fireball","enemy",True,None]                                                                                                                                                                                                                             

winter = [Armoury.silentNight,None,None,Armoury.frostPlate,Armoury.elfLeggings,Armoury.spellBoots,"The King of Winter","enemy",True,None,allLore["winter"]]
winterguard = [Armoury.winterguard,None,None,None,None,None,"Winterguard","enemy",True,None]
friendWinterguard = [Armoury.winterguard,None,None,None,None,None,"Winterguard","ally",True,None]

mass = [Armoury.longsword,None,None,Armoury.core,Armoury.endlessGrowths,None,"Ooglesh, the Primordial Ooze","enemy",False,None,allLore["mass"]]

lethe = [Armoury.LetheStats,None,Armoury.LetheStats2,None,None,None,"Lethe, Lord of Dusk","enemy",False,None,allLore["lethe"]]

umbralDaemon = [Armoury.daemonStats,None,None,None,None,None,"Umbral Daemon","enemy",False,None]

prideDaughter = [Armoury.corruptStats,Armoury.prideStats,None,None,None,None,"Daughter of Pride","enemy",False,None,allLore["DoC"]]
slothDaughter = [None,Armoury.slothStats,None,None,None,None,"Daughter of Sloth","enemy",False,None]
envyDaughter = [Armoury.corruptStats,Armoury.envyStats,None,None,None,None,"Daughter of Envy","enemy",False,None]

glassKnight = [Armoury.glassKnightStats,None,Armoury.glassKnightStats2,Armoury.glassKnightStats3,None,None,"Glass Knight","enemy",True,None,allLore["glass"]]

#super bosses (has extra field for title card)                                                                  
raah = [Armoury.severingblade,None,Armoury.starScar,Armoury.raahAttire,Armoury.raahTrousers,Armoury.starWalker,"Sun-King Ra'ah","enemy",True,None,allLore["raah"]]
                                                                                                                                                     
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

usurper = [random.choice(weapons),random.choice(weapons),random.choice(helmets),random.choice(breastplates),random.choice(leggings),random.choice(boots),"False Usurper ","enemy",False,allLore["usurper"],None]
                                                                                                                                                                                   
                                                                                                                                                   


#spawntables - split into the actual spawn table and the sprites for the map
solarKnights = [[swordsman,crossbowman,solarPriest],"sprites/hrocharad/","The Radiant City"]

#north = [[direWolf,beserker,kralBreeder],"sprites/north/","The North"]
newNorth = [[peasant,razorKnight,cultist],"sprites/north/","The North"]
newNorth2 = [[peasant,razorKnight,cultist,friendWinterguard],"sprites/north/","The North"]

darkness = [[darkwalker,pit],"sprites/forest/","Cave"]

#bosstables
#all enemies after the first will be ads
# I have no idea what the number in the second to last field does, but im scared to take it out so it stays in
solarBoss = [[mageKnight,swordsman,swordsman,solarPriest],"sprites/throne/","music/Radiant Thousand.mp3","Crusader Fortress",1,Armoury.mageknightLootTable]
northBoss = [[winter,winterguard,winterguard,winterguard],"sprites/north/","music/Frozen Monarch.mp3","The Starless Citadel",0,Armoury.winterLootTable]
darkBoss = [[mass,ballistaGrowth,ballistaGrowth,ballistaGrowth],"sprites/forest/","music/Creature of Darkness.mp3","Impact Site",4,Armoury.massLootTable]
darkBoss2 = [[lethe,umbralDaemon,umbralDaemon,umbralDaemon],"sprites/darkness/","music/Deluded Old Man.mp3","The Umbral Wood",5,Armoury.letheLootTable]
lifeBoss = [[prideDaughter,slothDaughter,envyDaughter],"sprites/greattree/","music/Daughter of Corruption.mp3","Cursed Great-Tree",5,Armoury.daughterLootTable]
knightBoss = [[glassKnight],"sprites/palmor/","music/Look Into My Mirror.mp3","Sinking City",5,Armoury.glassLootTable]

#superbosstables
mageSuperBoss = [[raah],"sprites/throne/","music/Starslayer.mp3","Ra'ah's Inner Sanctum",6,None]
usurperSuperBoss = [[usurper,razorKnight],"sprites/throne/","music/Usurper's Travels.mp3","Ra'ah's Inner Sanctum",6,None]

#all spawntables
spawnTables = [solarKnights,solarKnights,darkness,darkness,newNorth,newNorth2]

FullBossTables = [solarBoss,darkBoss,northBoss,darkBoss2,lifeBoss,knightBoss]
bossTables = FullBossTables

superBossTables = [mageSuperBoss,usurperSuperBoss]


#debug
#bossTables = [knightBoss,knightBoss,knightBoss]
#spawnTables = [newNorth2]
#superBossTables = [usurperSuperBoss]