import Armoury

#Northern Tribes
direWolf = [Armoury.iceClaw,Armoury.iceClaw,Armoury.beastFangs,None,None,None,"Direwolf","enemy"]
beserker = [Armoury.bloodyAxe,Armoury.bloodyAxe,Armoury.warMask,None,None,None,"Beserker","enemy"]
kralBreeder = [Armoury.iceWhistle,None,None,Armoury.iceHide,Armoury.fur,Armoury.frostHooves,"Hunter","enemy"]

#Solar Knights
swordsman = [Armoury.swordsmanStats,None,None,None,None,None,"Inquisitor","enemy"]
crossbowman = [Armoury.crossbowmanStats,None,None,None,None,None,"Inquisitor","enemy"]
solarPriest = [Armoury.solarPriestStats,None,None,None,None,None,"Solar Priest","enemy"]

#Children of the Dark
darkwalker = [Armoury.darkwalkerStats,None,None,None,None,None,"Darkwalker","enemy"]
pit = [Armoury.pitStats,None,None,None,None,None,"Deep Frigid Hole","enemy"]
phalanxGrowth = [Armoury.phalanxGrowthStats,None,None,None,None,None,"Armoured Sludge","enemy"]
ballistaGrowth = [Armoury.BallistaGrowthStats,None,None,None,None,None,"Ballista Sludge","enemy"]

#New North
peasant = [Armoury.peasantStats,None,Armoury.peasantStats2,None,None,None,"Feral Peasant","enemy"]
razorKnight = [Armoury.razorKnightStats,None,Armoury.razorKnightStats2,None,None,None,"Razor Knight","enemy"]
cultist = [Armoury.cultistStats,None,None,None,None,None,"Blood Star Cultist","enemy"]

#bosses (has extra field for title card)
mageKnight = [Armoury.KotFFStats,None,None,Armoury.sunAttune,None,None,"Knight of the First Flame","enemy",["Here stands a servant of jealous fire. With unwavering loyalty to the sun-god Solei, known as the First Flame,","they are one of the Pretender's most loyal subjects.",""]]
fireball = [Armoury.fireballStats,None,Armoury.fireballExplode,None,None,Armoury.spellBoots,"Fireball","enemy"]                                                                                                                                                                                                                             

winter = [Armoury.silentNight,None,None,Armoury.frostPlate,Armoury.elfLeggings,Armoury.spellBoots,"The King of Winter","enemy",["Here sits an empty vessel, a failed experiment, left to rule over a starless, bloodsoaked",
                                                                                                                                "realm, abandoned by their cold creator",""]]
winterguard = [Armoury.winterguard,None,None,None,None,None,"Winterguard","enemy"]
friendWinterguard = [Armoury.winterguard,None,None,None,None,None,"Winterguard","ally"]

mass = [Armoury.longsword,None,None,Armoury.core,Armoury.endlessGrowths,None,"Ooglesh, the Primordial Ooze","enemy",["Here bubbles the First Child of Darkness, once kept at bay by a thousand divine star-fires",""]]

lethe = [Armoury.LetheStats,None,Armoury.LetheStats2,None,None,None,"Lethe, Lord of Dusk","enemy",['Here sits a decrepit old man clad in tattered rags. "I am Lethe, Lord of the Dusk Age, and the', 
                                                                                                   'world is mine to drown in darkness!" he yells, as he waves his rusted shortsword in the air.',
                                                                                                   'You conclude this man obviously poses no threat to you, so you turn to walk away.','','...then the world goes black...','']]

umbralLegate = [Armoury.legateStats,None,None,None,None,None,"Umbral Legate","enemy"]

#super bosses (has extra field for title card)                                                                  
raah = [Armoury.severingblade,None,Armoury.starScar,Armoury.raahAttire,Armoury.raahTrousers,Armoury.starWalker,"Raah, the Pretender ","enemy",["Here sits the final obstacle of your travels",
                                                                                                                                                     "The Chosen of the First Flame,",
                                                                                                                                                     "The Starbane,",
                                                                                                                                                     "Pretender.",
                                                                                                                                                     "Strike him down, and take from him the throne he does not deserve",""]]
                                                                                                                                                     



#spawntables - split into the actual spawn table and the sprites for the map
solarKnights = [[swordsman,crossbowman,solarPriest],"sprites/hrocharad/","The Radiant City"]

#north = [[direWolf,beserker,kralBreeder],"sprites/north/","The North"]
newNorth = [[direWolf,peasant,razorKnight,cultist],"sprites/north/","The North"]
newNorth2 = [[direWolf,peasant,razorKnight,cultist,friendWinterguard],"sprites/north/","The North"]

darkness = [[darkwalker,pit],"sprites/cave/","Cave"]

#bosstables
#all enemies after the first will be ads
# I have no idea what the number in the second to last field does, but im scared to take it out so it stays in
solarBoss = [[mageKnight,swordsman,swordsman,solarPriest],"sprites/throne/","music/Servant of Jealous Fire.mp3","Outer Sanctum",1,Armoury.mageknightLootTable]
northBoss = [[winter,winterguard,winterguard,winterguard],"sprites/north/","music/Frozen Monarch.mp3","The Starless Citadel",0,Armoury.winterLootTable]
darkBoss = [[mass,ballistaGrowth,ballistaGrowth,ballistaGrowth],"sprites/cave/","music/Creature of Darkness.mp3","The Depths",4,Armoury.massLootTable]
darkBoss2 = [[lethe,umbralLegate,umbralLegate,umbralLegate],"sprites/darkness/","music/Deluded Old Man.flac","The Umbral Wood",5,Armoury.letheLootTable]

#superbosstables
mageSuperBoss = [[raah],"sprites/throne/","music/Heolstor 1.mp3","Inner Sanctum",6,None]


#all spawntables
spawnTables = [solarKnights,darkness,newNorth]

bossTables = [solarBoss,darkBoss,northBoss,darkBoss2]

superBossTables = [mageSuperBoss]

#debug
#bossTables = [solarBoss,solarBoss,solarBoss]
#spawnTables = [newNorth2]