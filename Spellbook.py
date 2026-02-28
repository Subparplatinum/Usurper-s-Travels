class Enchantment:
    def __init__(self,effectType,statDepend,magnitude,trigger,target,cost,name,desc):
        self.effectType = effectType
        self.statDepend = statDepend
        self.magnitude = magnitude
        self.trigger = trigger
        self.target = target
        self.cost = cost
        self.name = name
        self.desc = desc

#stat manipulation
thorns = Enchantment(["hp"],[None],[5],"selfHit","attacker",50,"Thorns","")

freeze = Enchantment(["frost"],[None],[1],"selfHit","attacker",0,"Freeze",["On being attacked, apply {} stacks of Frost to the attacker."])

stupid = Enchantment(["hp"],[None],[500],"selfHit","self",0,"incredible levels of incompetance","")

voidBlade = Enchantment(["hp"],[None],[50],"attack","target",0,"Hungering Darkness",["On attacking a target, reduce their HP by {}."])

cosmicFocus = Enchantment(["mp"],[None],[-20],"selfHit","self",0,"Cosmic Surge",["On being attacked, increase your MP by {}."])

apBreak = Enchantment(["ap"],[None],[10],"attack","target",20,"Rending Strike",["On attacking a target, reduce their AP by {}. Costs 20 MP."])

apPierce = Enchantment(["hp"],[None],[10],"attack","target",10,"Piercing Knives",["On attacking a target, reduce their HP by {}. Costs 10 MP."])

trap = Enchantment(["sp"],[None],[1],"move","adjAll",10,"Traps","")

wildMagic = Enchantment(["hp"],[None],[50],"ability","adjAll",25,"Wild Magic",["Deal {} damage (ignoring AP) to ALL adjacent entities.","Costs 25 MP per entity hit."])

starstrike = Enchantment(["hp"],[None],[30],"ability","nearestEnemy",50,"Crystal Rain",["Reduce the nearest enemy's hp by {}. Costs 50 MP."])

crystal = Enchantment(["mp"],[None],[-80],"endTurn","self",0,"Crystal Binge",["When your turn ends, increase your MP by {}."])

tremor = Enchantment(["hp"],[None],[15],"action","adjAll",0,"Glacial Tremors",["Whenever you take an action (move, attack or skip turn) deal {} damage","(ignoring AP) to ALL adjacent units."])

regen = Enchantment(["hp"],[None],[-50],"endTurn","self",10,"Regeneration",["When your turn ends, increase your HP by {}. Costs 10 MP."])

greatThaw = Enchantment(["hp"],[None],[9999999],"death","allAllies",0,"The Great Thaw",["Powerful frost magic dwells within the throne","Destroying it will destroy its subjects"])

noWalls = Enchantment(["hp"],[None],[9999999],"spawn","allWalls",0,"End of Disparity",["On spawn, destroy all walls on the map."])

counter = Enchantment(["attack"],[None],[1],"block","attacker",10,"Counter",["On blocking an attack (reduce its damage below 0 using your AP),","attack the attacker {} times. Costs 10 MP."])

frenzy = Enchantment(["hp"],[None],[10],"action","adjEnemies",5,"Frenzy",["Whenever you take an action (move, attack or skip turn) deal {} damage","(ignoring AP) to all adjacent enemies. Costs 5 MP per adjacent enemy."])

bloodDrink = Enchantment(["dmg"],[None],[-10],"kill","self",0,"Blood Drink",["On killing an entity, increase your AT bonus by {}%."])

reload = Enchantment(["sp"],[None],[1],"attack","self",0,"Reload",["On attack, reduce your SP by {}."])

prepare = Enchantment(["sp"],[None],[1],"spawn","self",0,"Prepare",["On spawn, reduce your SP by {}."])

heal = Enchantment(["hp"],[None],[-10],"ability","allAllies",40,"Healing Light",["Increase all allies' HP by {}. Costs 40 MP per ally."])

atBuff = Enchantment(["dmg"],[None],[-5],"endTurn","allAllies",10,"Strengthening Light",["When your turn ends, increase all allies' AT bonus by {}%.","Costs 10 MP per ally."])

charge = Enchantment(["tempDmg"],[None],[-25],"move","self",0,"Charge",["Increase your AT bonus by {}% for every tile you move this turn.","Resets on end turn."])

frente = Enchantment(["sp"],[None],[3],"riderBoots","self",0,"Mounted",["Mounts can only be ridden with Rider's Boots."])
    
attackFreeze = Enchantment(["frost"],[None],[2],"attack","target",25,"Silence Heart",["On attack, apply {} stacks of Frost to the target. Costs 25 MP."])

attackFreeze2 = Enchantment(["frost"],[None],[1],"attack","target",25,"Like the Blizzard",["On attack, apply {} stacks of Frost to the target. Costs 25 MP."])

inspire = Enchantment(["dmg"],[None],[-10],"death","allAllies",0,"Inspiration",["On death, increase all allies' AT bonus by {}%."])

prepared = Enchantment(["sp"],[None],[-2],"spawn","self",0,"Prepared",["On spawn, increase your SP by {}."])

aim = Enchantment(["tempDmg"],[None],[25],"move","self",0,"Aim",["Decrease your AT bonus by {} for every tile you move this turn.","Resets on end turn."])

rage = Enchantment(["sp"],[None],[-1],"selfHit","self",50,"Rage",["On being hit, increase your SP by {}. Costs 50 MP per hit."])

objection = Enchantment(["hp"],[None],[50],"selfHit","attacker",50,"Objection",["On being hit, reduce your attacker's HP by {}. Costs 20 MP."])

lifesteal = Enchantment(["hp"],[None],[-20],"attack","self",50,"Lifesteal",["On attack, increase your HP by {}. Costs 50 MP."])

manasteal = Enchantment(["mp"],[None],[25],"attack","target",-25,"Manasteal",["On attack, decrease the target's MP by {} and increase your MP by 25."])

lessmanasteal = Enchantment(["mp"],[None],[-10],"attack","self",0,"Manapinch",["On attack, increase your MP by {}."])

rally = Enchantment(["dmg"],[None],[-10],"endTurn","allAllies",0,"Rally",["On end turn, increase all allies' AT bonus by {}%."])

zodiac = Enchantment(["mp"],[None],[-20],"endTurn","allAllies",10,"Read the Stars",["On end turn, increase all allies' MP by {}. Costs 10 MP per ally."])

fear = Enchantment(["dmg"],[None],[10],"spawn","allEnemies",10,"Fearmongerer",["On spawn, decrease all enemies' AT bonus by {}. Costs 5 MP per enemy."])

healthy = Enchantment(["hp"],[None],[-10],"move","self",10,"One with Nature",["On move, increase your hp by {}. Costs 10 MP."])

focus = Enchantment(["mp"],[None],[20],"move","self",0,"Focus",["Decrease your MP by {} for every tile you move."])

apAmmo = Enchantment(["ap"],[None],[10],"rangedAttack","target",20,"Rending Ammo",["On attacking a target with a ranged attack, reduce their AP by {}.","Costs 20 MP."])
                     
mpSp = Enchantment(["sp"],["mp"],[-1/100],"startTurn","self",20,"Fly",["On end turn, increase your SP by 1 per 100 MP.","Costs 20 MP per turn."])

poison = Enchantment(["hp"],[None],[10],"endTurn","self",0,"Poison",["On end turn, reduce your HP by {}. Reduces by 1 stack per turn."])

frost = Enchantment(["sp"],[None],[0.5],"endTurn","self",0,"Frost",["On end turn, reduce your SP by {} for every 2 stacks of Frost.","Reduces by 4 stacks per turn."])

frostImmune = Enchantment(["frost"],[None],[-999],"endTurn","self",0,"Frost Immune",["On end turn, remove {} stacks of Frost on self."])
burnImmune = Enchantment(["burn"],[None],[-999],"endTurn","self",20,"Refreshing Waters",["On end turn, remove {} stacks of Burn on self. Costs 20 MP per turn."])



poisoner = Enchantment(["poison"],[None],[1],"attack","target",20,"Poisoner",["On attack, apply {} stacks of Poison to the target.","Costs 20 MP."])

starSeed = Enchantment(["hp"],[None],[10],"death","allAllies",0,"Crystal Buds",["On death, deal {} damage to all allies per stack."])

starBirth = Enchantment(["starSeed"],[None],[1],"attack","target",50,"Crystal Seed",["On attack, apply {} stacks of Crystal Buds to the target. When the target dies,","these will shatter and damage their allies in a storm of wild magic. Costs 50 MP."])

fate = Enchantment(["multRemove"],[None],[10],"attack","target",50,"Sever Fate",["On attack, weaken the Bloody Star's guidance, reducing Sacrifice by {}%","Costs 50 MP."])

wrath = Enchantment(["burn"],[None,None],[2],"endTurn","all",0,"Solei's Wrath",["On end turn, give all entities {} stacks of Burn."])

brace = Enchantment(["tempAp"],[None],[10],"move","self",0,"Brace",["Temporarily decrease your AP by {} for every tile you move this turn."])

amalgamation = Enchantment(["hp"],[None],[-20],"kill","allAllies",0,"Amalgamation",["On kill, increase all allies HP by {}"])

collapse = Enchantment(["hp"],[None],[9999999],"death","allAllies",0,"Collapse",["The collapse of the core precedes the collapse of the mass"])

projection = Enchantment(["rangedAttack"],["mp"],[-1/100],"ability","nearestEnemy",50,"Projection",["Perform 1 attack against the nearest enemy","regardless of range per 100 MP. Costs 50 MP."])

massAbsorb = Enchantment(["mp"],[None],[50],"spawn","allEnemies",-50,"Mass Manasteal",["On spawn, reduce all enemies MP by 50 and increase your MP","by 50 per enemy."])

swagger = Enchantment(["sp"],[None],[2],"endTurn","nearestEnemy",50,"Swagger",["On end turn, reduce the nearest enemy's sp by {}. Costs 50 MP."])

spellShield = Enchantment(["tempAp"],["mp"],[-1/10],"startTurn","self",20,"Spell Shield",["On start turn, increase your AP by 1 for every 10 points of MP.","Costs 20 MP per turn."])

evasion = Enchantment(["tempAp"],["maxSp"],[-5],"startTurn","self",0,"Evasion",["On end turn, increase your AP by {} for every 1 point of max SP."])

zornhau = Enchantment(["tempDmg"],[None],[25],"move","self",0,"Zornhau",["Decrease your AT bonus by {}% for every tile you move this turn.","Resets on end turn."])

reTrigger = Enchantment(["dmg"],[None],[-5],"otherAbility","self",0,"Astral Mastery",["Gain a {}% AT bonus after using an ability."])

dragonchild = Enchantment(["dmg"],[None],[-50],"transform","self",0,"Wyvern's Child",["Gain a {}% AT bonus while transformed."])

retaliation = Enchantment(["rangedAttack"],[None],[1],"selfHit","attacker",0,"Omnipresence",["On being attacked, attack the attacker {} time/s."])

burn = Enchantment(["tempDmg"],[None],[5],"endTurn","self",0,"Burn",["On end turn, reduce your AT bonus by {}% per stack","for next turn. Reduces by 1 stack per turn."])
burningWeapon = Enchantment(["burn"],[None],[1],"attack","target",0,"Burning Weapon",["On attacking an enemy, apply {} stacks of Burn."])
burnEnchant = Enchantment(["burnEnchant"],[None],[1],"ability","allAllies",20,"Solei's Blessing",["Apply Burning Weapon to all allies.","Costs 20 MP per ally."])

fireballHitSelf = Enchantment(["hp"],[None],[9999],"attack","self",0,"Unstable",["On attack, deal {} damage to self"])
fireballExplode = Enchantment(["hp","burn"],[None,None],[50,2],"death","adjAll",0,"Explode",["Deal {} damage and apply {} stacks of Burn to all adjacent entities on death."])
fireballSummon = Enchantment(["fireball"],[None],[1],"ability","self",100,"Wrath of Solei",["Summon {} fireball/s in adjacent tiles. Costs 100 MP."])

bigWildMagic = Enchantment(["hp"],[None],[10],"endTurn","allEnemies",100,"Wild Magic Storm",["On end turn, deal {} damage to all enemies."])                 
  
teleport = Enchantment(["teleport"],[None],[1],"ability","nearestEnemy",0,"Darkstep",["Teleport to the nearest enemy"])     

burningRays = Enchantment(["burn"], [None],[1],"ability","nearestEnemy",50,"Burning Rays",["Apply {} stack/s of Burn to the nearest enemy. Costs 50 MP."])

thunderbrand = Enchantment(["sp"],[None],[-1],"ability","nearestAlly",100,"Thunderbrand",["Increase your nearest ally's SP by {}. Costs 100 MP."])

stormSeeker = Enchantment(["sp"],[None],[-1],"startTurn","self",20,"Seeker of the Storm",["Increase your SP by {}. Costs 20 MP per turn."])

automaton = Enchantment(["hp"],[None],[30],"attack","nearestEnemy",10,"Hunting Automaton",["On attack, reduce the nearest enemy's HP by {}. Costs 10 MP."])

bloodloss = Enchantment(["hp"],[None],[5],"move","self",0,"Bloodloss",["On move, reduce your HP by {}.","Reduces by 1 stack per turn."])
inflictBlood = Enchantment(["bloodloss"],[None],[1],"attack","target",0,"Blood for our God!", ["Apply {} stack/s of Bloodloss to target on hit."])
caltrops = Enchantment(["caltrops"],[None],[1],"ability","self",25,"Caltrop Pouch", ["Drop {} caltrop/s on your tile."])
rangedCaltrops = Enchantment(["caltrops"],[None],[1],"attack","target",0,"Caltrop Launcher", ["Drop {} caltrop/s on your target's tile."])

weakenAllies = Enchantment(["ap"],[None],[150],"death","allAllies",0,"Dispel Delusion",["On death, reduce all allies' AP by {}."])

hammerTremor = Enchantment(["hp"],[None],[50],"attack","targetAdjEnemies",0,"Shockwave Strike",["On attack, deal {} damage to your target's adjacent allies."])

#------------------------------------------------------------------------------------------------------------------------------------------


#ratkin stuff
disease = Enchantment(["hp","dmg"],[None,None],[5,5],"endTurn","self",0,"Disease",["On end turn, reduce your HP by {} and your AT bonus by {}.","Reduces by 1 stack per turn."])
filthBlessing = Enchantment(["disease"],[None],[1],"ability","adjEnemies",25,"Blessing of Filth",["Apply {} stack/s of Disease to all adjacent enemies. Costs 25 MP per","adjacent enemy."])


#human
lessRegen = Enchantment(["hp"],[None],[-10],"endTurn","self",0,"Lesser Regen",["When your turn ends, increase your HP by {}."])

#elf
attune = Enchantment(["mp"],[None],[-20],"endTurn","self",0,"Astra's Chosen",["When your turn ends, increase your MP by {}."])

sunAttune = Enchantment(["mp"],[None],[-100],"endTurn","self",0,"Chosen of Solei",["When your turn ends, increase your MP by {}."])

#dwarf
stalwart = Enchantment(["ap"],[None],[-10],"spawn","self",0,"Stalwart",["On spawn, increase your AP by {}."])

#lizardfolk
poisonous = Enchantment(["poison"],[None],[1],"attack","target",0,"Poisonous",["On attack, apply {} stacks of Poison to the target."])

#harpy
quick = Enchantment(["sp"],[None],[-3],"spawn","self",0,"Quick",["On spawn, increase your SP by {}."])

#summoning
frosthound = Enchantment(["frosthound"],[None],[1],"ability","self",100,"Frost Call",["Summon {} Direwolves/s in an adjacent tile. Costs 100 MP."])

throne = Enchantment(["throne"],[None],[1],"spawn","self",0,"Winter's King",["On spawn, summon The Throne of Winter in an adjacent tile."])

idealist = Enchantment(["idealist"],[None],[4],"ability","self",150,"Hero's Call",["Summon {} Warriors in adjacent tiles. Costs 50 MP."])

phalanx = Enchantment(["phalanx"],[None],[8],"ability","self",50,"Phalanx Growths",["Summon {} Phalanx Growths in adjacent tiles. Costs 50 MP."])
ballista = Enchantment(["ballista"],[None],[8],"ability","self",50,"Ballista Growths",["Summon {} Ballista Growths in adjacent tiles. Costs 50 MP."])

raahTwo = Enchantment(["raahTwo"],[None],[1],"death","self",50,"Resurgence",["This boss has a second phase"])

crystalLump = Enchantment(["crystalLump"],[None],[1],"ability","self",150,"Crystal Growth",["Summon {} Crystal Growth/s in adjacent tiles. Costs 150 MP."])



#transformation
wyvern = Enchantment(["wyvern"],[None],[1],"ability","self",200,"Wyvern Download",["Succumb to Drakkak's rage, and become an avatar of his fury.","Grants {} turns of Wyvernform per use. Costs 200 MP"])
