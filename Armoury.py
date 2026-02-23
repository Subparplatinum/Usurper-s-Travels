import Spellbook

class Equipment:
    def __init__(self,speedBonus,healthBonus,armourBonus,manaBonus,attackBonus,enchantment,name,equipType,lootTable):
        self.speedBonus = speedBonus
        self.healthBonus = healthBonus
        self.armourBonus = armourBonus
        self.manaBonus = manaBonus
        self.attackBonus = attackBonus
        self.enchantment = enchantment

        self.name = name
        self.equipType = equipType

        self.lootTable = lootTable

        #WIP levelling mechanic
        self.level = 1

        if self.lootTable != None:
            self.lootTable.append(self)

class Weapon(Equipment):
    def __init__(self,speedBonus,healthBonus,armourBonus,manaBonus,attackBonus,enchantment,name,attackRange,twoHanded,lootTable):
        super().__init__(speedBonus,healthBonus,armourBonus,manaBonus,attackBonus,enchantment,name,"weapon",lootTable)
        self.attackRange = attackRange
        self.twoHanded = twoHanded


#lootTable
lootTable = []

winterLootTable = []

mageknightLootTable = []

massLootTable = []

voidLootTable = []


"""
Lawyer Witch
"""
#weapons
lawBook = Weapon(0,0,0,100,20,Spellbook.objection,"Law Book",1,False,lootTable)
magicBroom = Weapon(3,0,0,0,1,None,"Magic Broom",1,False,lootTable)

#helmets
mageHat = Equipment(0,0,0,100,0,None,"Mage Hat","helmet",lootTable)

#breasplates
mageCloak = Equipment(0,20,0,100,0,None,"Mage Cloak","breastplate",lootTable)

#leggings
mageRobe = Equipment(0,0,0,100,0,None,"Mage Robes","leggings",lootTable)

#boots
mageBoots = Equipment(1,0,0,100,0,None,"Mage Boots","boots",lootTable)


"""
Wall
"""
#breastplates
bricks = Equipment(-1,200,0,-100,0,None,"Bricks","breastplate",None)

"""
Sword Monk
"""
#weapons
swordsmanStats = Weapon(1,20,20,0,35,None,"",1,True,None)

"""
Crossbow Monk
"""
#weapons
crossbowmanStats = Weapon(0,0,0,0,75,Spellbook.reload,"",5,True,None)

#weapon for player
crossbow2 = Weapon(0,0,0,0,100,Spellbook.reload,"Crossbow",5,True,lootTable)

#add item that gives a large amount of damage but decreases it on move
hunterLens = Equipment(0,0,0,0,50,Spellbook.aim,"Hunter's Lens","helmet",lootTable)

"""
Solar Priest
"""
#weapons
solarPriestStats = Weapon(0,-100,0,200,0,Spellbook.burnEnchant,"",5,False,None)


#leggings
atRobe = Equipment(0,0,-20,100,0,Spellbook.atBuff,"Bone Robe","leggings",lootTable)

"""
Knight of the First Flame
"""

#stats
KotFFStats = Weapon(1,300,40,400,60,Spellbook.fireballSummon,"",1,False,None)


#breastplates
sunAttune = Equipment(0,0,0,0,0,Spellbook.sunAttune,"","breastplate",None)

#for player
solarPlate = Equipment(0,100,10,-160,0,Spellbook.sunAttune,"Solar Plate","breastplate",mageknightLootTable)
enchantedGreatsword = Weapon(0,0,0,200,60,Spellbook.fireballSummon,"Burning Greatsword",1,True,mageknightLootTable)

#stats for fireball
fireballStats = Weapon(2,-199,0,0,0,Spellbook.fireballHitSelf,"",1,False,None)
fireballExplode= Equipment(0,0,0,0,0,Spellbook.fireballExplode,"","breastplate",None)

"""
Frosthound
"""
#weapons
iceClaw = Weapon(1,0,0,0,30,None,"Ice Claw",1,False,None)

#equippable ice claw
iceClaw2 = Weapon(1,0,0,0,30,None,"Ice Claw",1,False,lootTable)

#breastplates
iceHide = Equipment(1,-60,0,0,0,None,"Ice Hide","breastplate",None)

#equippable ice hide
iceHide2 = Equipment(0,20,10,0,0,Spellbook.freeze,"Ice Hide","breastplate",lootTable)


"""
Wolf/Direwolf
"""
beastFangs = Equipment(0,0,0,0,20,Spellbook.lifesteal,"Beast Fangs","helmet",None)
#breastplates
hide = Equipment(0,-60,0,0,0,None,"Hide","breastplate",None)

"""
Beserker
"""
#weapons
bloodyAxe = Weapon(0,0,5,0,20,Spellbook.bloodDrink,"Bloody Axe",1,False,lootTable)

#helmet
warMask = Equipment(1,0,0,0,0,Spellbook.frenzy,"War Mask","helmet",lootTable)

"""
Rogue
"""
#weapons
throwingKnife = Weapon(1,0,0,0,5,None,"Throwing Knife",3,False,lootTable)

#tunic
tunic = Equipment(0,5,0,0,0,None,"Tunic","breastplate",lootTable)

#boots
boots = Equipment(1,5,0,0,0,None,"Boots","boots",lootTable)

"""
Thug
"""
#weapons
ironClub = Weapon(0,0,5,0,60,Spellbook.apBreak,"Iron Club",1,True,lootTable)

#helmet
banditMask = Equipment(0,0,0,0,0,Spellbook.rage,"Bandit Mask","helmet",lootTable)

#leggings
trapLeggings = Equipment(0,10,0,50,0,Spellbook.trap,"Trapper's Leggings","leggings",None)

"""
Assassin
"""
#weapons
greatbow = Weapon(-1,0,0,0,75,Spellbook.prepare,"Greatbow",10,True,lootTable)

hasteBoots = Equipment(2,0,-10,0,0,Spellbook.prepared,"Haste boots","boots",lootTable)

lessHp = Equipment(0,-40,-10,0,0,None,"","helmet",None)

"""
Skyla Crystalmouth
"""
#weapons
crystalbreaker = Weapon(0,0,10,100,60,None,"Crystalbreaker",1,True,None)

#breastplates

"""
Kral Breeder
"""
#weapons
iceWhistle = Weapon(0,0,0,50,0,Spellbook.frosthound,"Ice Whistle",5,False,lootTable)

#leggings
fur = Equipment(0,40,0,0,0,None,"Fur","leggings",lootTable)

#boots
frostHooves = Equipment(1,0,0,0,0,Spellbook.bloodDrink,"Frost Hooves","boots",None)


"""
The Throne of Winter
"""
#breastplate
winterCore = Equipment(-1,400,0,0,0,Spellbook.greatThaw,"Heart of Winter","breastplate",None)

"""
King of Winter
"""
#weapons
silentNight = Weapon(0,0,10,0,75,Spellbook.attackFreeze,"Silent Night",1,True,winterLootTable)
#breastplate
frostPlate = Equipment(0,1000,0,0,0,Spellbook.throne,"Winter's Plate","breastplate",winterLootTable)

elfLeggings = Equipment(0,0,5,50,0,Spellbook.sunAttune,"Spell Leggings","leggings",None)

"""
Winterguard
"""
winterguard = Weapon(0,100,20,0,70,Spellbook.attackFreeze,"",1,True,None)


"""
Donkey Oaty
"""
#weapon
oatLance = Weapon(0,0,0,0,50,None,"Meteoric Lance",1,True,None)

#helmet
bascinet = Equipment(0,20,10,0,0,None,"Bascinet Helm","helmet",lootTable)

#leggings
frenteguerra = Equipment(3,0,0,0,0,Spellbook.frente,"Frenteguerra","leggings",None)

#boots
riderBoots = Equipment(0,0,0,0,0,None,"Rider's Boots","boots",lootTable)


"""
Raah the Pretender/Raah the Starbane
"""

#weapon
severingblade = Weapon(0,0,10,60,80,Spellbook.fate,"Blade of Severing",1,True,None)

#helmet
starScar = Equipment(0,50,0,200,10,Spellbook.sunAttune,"Celestial Scar","helmet",None)

#breastplate
raahAttire = Equipment(0,150,20,50,0,Spellbook.raahTwo,"Raah' Shoulder Jacket","breastplate",None)
raahAttire2 = Equipment(2,150,20,50,0,None,"Raah' Shoulder Jacket","breastplate",None)

#leggings
raahTrousers = Equipment(0,0,5,100,0,None,"Raah' Trousers","leggings",None)

#boots
starWalker = Equipment(1,0,0,100,0,None,"Starwalker Boots","boots",None)


"""
Ooglesh, the Primordial Ooze
"""

#breastplate
core = Equipment(0,275,0,400,0,None,"Ooglesh's Core","breastplate",None)
#leggings
endlessGrowths = Equipment(0,50,0,0,0,Spellbook.phalanx,"Formless Sludge","leggings",massLootTable)

#add a weapon that does area damage, perfect for dealing with the mass


"""
Abyssal Pit
"""
pitStats = Weapon(-1,-100,10,0,0,Spellbook.ballista,"",0,None,None)

"""
Phalanx Growth
"""
phalanxGrowthStats = Weapon(0,-100,0,0,25,Spellbook.amalgamation,"",1,None,None)

"""
Ballista Growth
"""
BallistaGrowthStats = Weapon(0,-150,0,0,20,None,"",11,None,None)


"""
Darkwalker
"""
darkwalkerStats = Weapon(1,0,0,0,120,Spellbook.teleport,"",1,False,None)



"""
Valiant Knight
"""
#weapon
lance = Weapon(0,0,0,0,20,Spellbook.charge,"Valiant Lance",1,True,None)

"""
Wyvern Download stuff
"""
#weapons
stoneTotem = Weapon(0,0,0,0,80,Spellbook.wyvern,"Stone Totem",1,True,None)

stoneTotemTwo = Weapon(3,900,0,-100,100,None,"Stone Totem",1,True,None)


"""
Talonblade
"""
wingbladeStats = Weapon(1,0,0,0,20,None,"",1,False,None)
harpyStats = Equipment(1,0,0,0,0,Spellbook.quick,"","breastplate",None)

"""
Wingbow
"""
hurricaneStats = Weapon(0,0,0,0,60,Spellbook.reload,"",2,True,None)

stormBow = Weapon(0,0,0,0,60,Spellbook.stormSeeker,"Storm Bow",2,True,lootTable)

"""
Thunderchief
"""
thunderStaff = Weapon(-1,0,0,100,20,Spellbook.thunderbrand,"Thunderstaff",11,False,lootTable)   

#########################################################
"""
New North


Feral Peasant
"""
peasantStats = Weapon(3,-120,0,0,50,Spellbook.inflictBlood,"",1,False,None)
peasantStats2 = Equipment(0,0,0,0,0,Spellbook.bloodDrink,"","helmet",None)


"""
Razor Knight
"""
razorKnightStats = Weapon(1,100,20,100,80,Spellbook.caltrops,"",1,False,None)
razorKnightStats2 = Equipment(0,0,0,0,0,Spellbook.inflictBlood,"","helmet",None)

"""
Blood Star Cultist
"""
cultistStats = Weapon(0,-120,0,0,20,Spellbook.rangedCaltrops,"",11,False,None)



"""
Player only
"""

#weapons
bloodlust = Weapon(1,0,0,0,30,Spellbook.lifesteal,"Bloody Dagger",1,False,lootTable)
nebula = Weapon(1,0,0,0,30,Spellbook.manasteal,"Starsteel Dagger",1,False,lootTable)
viperTooth = Weapon(1,0,0,0,30,Spellbook.poisoner,"Viper's Tooth",1,False,lootTable)
buckler = Weapon(0,10,10,0,10,Spellbook.counter,"Buckler Shield",1,False,lootTable)
spellShield = Weapon(0,0,0,0,5,Spellbook.spellShield,"Starsteel Shield",1,False,lootTable)
tower = Weapon(0,20,20,0,5,Spellbook.brace,"Tower Shield",1,False,lootTable)
bow = Weapon(0,0,0,0,50,None,"Bow",5,True,lootTable)
starStaff = Weapon(-1,0,0,100,20,Spellbook.starstrike,"Celestial Staff",11,False,lootTable)
holyStaff = Weapon(-1,0,0,100,20,Spellbook.heal,"Golden Staff",11,False,lootTable)
forgehammer = Weapon(0,5,0,0,80,Spellbook.zornhau,"Forgehammer",1,False,lootTable)
greatsword = Weapon(0,0,0,0,80,None,"Greatsword",1,True,lootTable)
stonePillar = Weapon(-1,0,0,0,100,None,"Stone Pillar",1,True,lootTable)
longsword = Weapon(0,0,0,0,40,None,"Longsword",1,False,lootTable)

#helmets
commissarHat = Equipment(0,10,0,0,5,Spellbook.rally,"General's Hat","helmet",lootTable)
zodiacHat = Equipment(0,0,0,80,0,Spellbook.zodiac,"Zodiac's Hat","helmet",lootTable)
fearVisage = Equipment(1,0,0,0,10,Spellbook.fear,"Horrifying Visage","helmet",lootTable)
iceFangs = Equipment(0,0,0,0,10,Spellbook.attackFreeze2,"Ice Fangs","helmet",lootTable)
fangs = Equipment(0,0,0,0,20,None,"Fangs","helmet",lootTable)
ghostFedora = Equipment(0,0,0,100,0,Spellbook.massAbsorb,"Ghosthand's Fedora","helmet",lootTable)
potHelm = Equipment(0,0,5,0,0,None,"Helmet","helmet",lootTable)

#breastplates
hunterCloak = Equipment(0,0,5,50,10,Spellbook.apAmmo,"Hunter's Cloak","breastplate",lootTable)
cloakOfKnives = Equipment(0,0,5,50,10,Spellbook.apPierce,"Cloak of Knives","breastplate",lootTable)
crystalcloak = Equipment(0,0,0,100,0,Spellbook.starBirth,"Crystal Cloak","breastplate",lootTable)
ghostSuit = Equipment(0,20,0,50,0,Spellbook.projection,"Ghosthand's Cloak","breastplate",lootTable)
breastplate = Equipment(0,20,10,0,0,None,"Breastplate","breastplate",lootTable)
spellPlate = Equipment(0,0,10,20,0,Spellbook.cosmicFocus,"Starsteel Plate","breastplate",lootTable)

#leggings
calfWings = Equipment(0,0,5,0,0,Spellbook.mpSp,"Calf Wings","leggings",lootTable)
legplate = Equipment(0,10,10,0,0,None,"Legplate","leggings",lootTable)
ghostTrousers = Equipment(0,20,0,50,0,Spellbook.swagger,"Ghosthand's Trousers","leggings",lootTable)
horse = Equipment(3,0,0,0,0,Spellbook.frente,"Warhorse","leggings",lootTable)
breeches = Equipment(0,5,0,0,0,None,"Breeches","leggings",lootTable)
spellLeggings = Equipment(0,0,5,50,0,None,"Starsteel Leggings","leggings",lootTable)

#boots
grassBoots = Equipment(1,40,0,0,0,Spellbook.healthy,"Druid Boots","boots",lootTable)
zodiacBoots = Equipment(1,10,0,200,0,Spellbook.focus,"Zodiac's Boots","boots",lootTable)
deserterBoots = Equipment(1,0,0,0,0,Spellbook.evasion,"Deserter's Boots","boots",lootTable)
metalBoots = Equipment(1,5,5,0,0,None,"Metal Boots","boots",lootTable)
spellBoots = Equipment(1,0,5,50,0,None,"Starsteel Boots","boots",lootTable)
