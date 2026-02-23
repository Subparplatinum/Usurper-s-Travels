import pygame
import random
import Armoury
import Menus
import Spellbook
import Tables

import sys #to get rid of one STUPID ERROR

class Entity:
    def __init__(self,window,level,startTile,weapon1,weapon2,helmet,breastplate,leggings,boots,name,entityType,mult,sigEnchant = None,spritePath = None):
        #entity types include: player,ally,enemy,wall
        self.entityType = entityType
        self.x = startTile.x
        self.y = startTile.y
        #this is the actual tile object for once
        self.tile = startTile
        self.tile.occupant = self

        #define sprite
        if spritePath != None:
            self.image = pygame.image.load(spritePath)
        else:
            self.image = None

        #when entity is killed, store killer
        self.killer = None
        
        #store mult
        self.mult = mult

        #used to identify targets for NPCs
        self.level = level

        #the player and their companion will have signature enchantments
        self.sigEnchant = sigEnchant
            
        self.window = window
        
        #equipment
        self.weapon1 = weapon1
        self.weapon2 = weapon2
        self.helmet = helmet
        self.breastplate = breastplate
        self.leggings = leggings
        self.boots = boots

        #name
        self.name = name

        #end turn effects were being called every frame
        self.endTurnActions = 0

        self.startTurnActions = 0
        
        #as a turn happens as soon as the game starts, this will be set to false
        self.endTurn = True
        #define tile to be selected when moving
        self.tileSelected = None

        #register with level
        self.level.entities.append(self)

        #how long an entity is remaining transformed for
        self.transformTurns = 0



        #create list of all equipment
        self.equipment = [self.weapon1,self.weapon2,self.helmet,self.breastplate,self.leggings,self.boots]

        #store it again so it can be retrieved for transformation
        self.equipStack = self.equipment

        self.updateStats()
        
        #needed for temporary effects
        self.tempAttack = 0
        self.tempArmour = 0
            
        #yucky text stuff
        self.font = pygame.font.SysFont(None,40)
        self.smolFont = pygame.font.SysFont(None,20)
        self.text = ""
        
        #colours (will be replaced with sprites)
        if self.entityType == "enemy":
            self.colour = (255,0,0)
            #let player have first turn
            self.speed -= self.maxSpeed

        elif self.entityType == "player":
            self.colour = (0,100,0)
            self.crosshair = pygame.image.load("sprites/crosshair.png")

        elif self.entityType == "ally":
            self.colour = (0,0,255)
            
        elif self.entityType == "wall":
            self.colour = (50,50,50)

        #Check if riderBoots are equipped
        if len(self.enchantments) > 0:
            for enchantment in self.enchantments:
                if enchantment.trigger == "riderBoots":
                    if self.equipment[5] == None:
                        self.triggerEnchant(enchantment)
                    elif self.equipment[5].name != "Rider's Boots":
                        self.triggerEnchant(enchantment)

    def updateStats(self):
        #base stats
        self.maxSpeed = 1.0 #actions per turn
        self.speed = 0.0
        
        self.maxHealth = 200 #increasing it to make fights last longer
        
        self.maxArmour = 0 #reduce damage on hit by 0
        
        self.maxMana = 100 #enchantments consume this

        self.maxAttack = 0 #damage done on hit
        
        #update stats to factor in equipment
        for i in range(len(self.equipment)):
            if self.equipment[i] != None:
                self.maxSpeed += self.equipment[i].speedBonus
                
                self.maxHealth += self.equipment[i].healthBonus
                
                self.maxArmour += self.equipment[i].armourBonus
                
                self.maxMana += self.equipment[i].manaBonus

                #weapons have an attack stat, but other equipment can have an attack bonus which is added onto each weapon attack
                if i > 1:
                    #weapons are at i = 0 and i = 1
                    self.maxAttack += self.equipment[i].attackBonus

        #take level into account (except for speed to prevent one sided matchups)
        self.maxHealth = round(self.maxHealth*self.mult)
        if self.maxHealth <= 0:
            self.maxHealth = 1
        self.maxArmour = round(self.maxArmour*self.mult)
        if self.maxArmour < 0:
            self.maxArmour = 0
        self.maxMana = round(self.maxMana*self.mult)
        self.maxAttack = round(self.maxAttack*self.mult)

        self.health = self.maxHealth
        self.armour = self.maxArmour
        self.mana = self.maxMana
        self.attack = self.maxAttack

        #create a list of all enchantments
        self.enchantments = []
        for equipment in self.equipment:
            if equipment != None:
                if equipment.enchantment != None:
                    self.enchantments.append(equipment.enchantment)
                    #print(self.enchantments)

        #the player and their companion will have signature enchantments
        if self.sigEnchant != None:
            self.enchantments.append(self.sigEnchant)

        #create a list of all abilites:
        #no duplicate abilities
        self.abilities = set()
        for enchantment in self.enchantments:
            if enchantment.trigger == "ability":
                self.abilities.add(enchantment)
                
        #convert back to a list for easy access
        self.abilities = list(self.abilities)


        
    #CALLED WHEN ENVIRONMENT.UPDATE IS CALLED
    def update(self):
        #end turn
        if self.speed <= 0:
            #for multiplayer stuff (designate whos turn it is by darkening whos turn it isnt)
            if self.entityType == "player":
                self.colour = (0,100,0)
            self.endTurn = True

        #since you can now increase the speed of someone whos turn has ended, they should unend their turn (from Harpy Update)
        else:
            self.endTurn = False
            if self.entityType == "player":
                self.colour = (0,255,0)
            
        #mouse position
        self.mousePos = pygame.mouse.get_pos()

        #reset temp armour on start turn so it can actually be exploited by the other team
        if self.startTurnActions == 1:
            self.armour -= self.tempArmour
            self.tempArmour = 0
            self.startTurnActions = 0

            #trigger start turn enchantments
            if len(self.enchantments) > 0:
                for enchantment in self.enchantments:
                    if enchantment.trigger == "startTurn":
                        self.triggerEnchant(enchantment)
        
        #carry out actions if applicable
        self.action()


        #end turn effects
        if self.endTurn == True and self.endTurnActions == 1:

            #remove self as selected player to stop the game freezing
            if self.level.selectedPlayer == self:
                self.level.selectedPlayer = None
                
            #remove status effects

            #remove 1 stack of poison
            if Spellbook.poison in self.enchantments:
                self.enchantments.remove(Spellbook.poison)
            #remove 1 stack of disease
            if Spellbook.disease in self.enchantments:
                self.enchantments.remove(Spellbook.disease)
            #remove 4 stacks of frost
            for i in range(4):
                if Spellbook.frost in self.enchantments:
                    self.enchantments.remove(Spellbook.frost)
            #remove 1 stack of burn
            if Spellbook.burn in self.enchantments:
                self.enchantments.remove(Spellbook.burn)
            #remove burning weapon
            if Spellbook.burningWeapon in self.enchantments:
                self.enchantments.remove(Spellbook.burningWeapon)

            #remove temporary attack bonuses
            self.attack -= self.tempAttack
            self.tempAttack = 0

            #trigger end turn enchantments
            if len(self.enchantments) > 0:
                for enchantment in self.enchantments:
                    if enchantment.trigger == "endTurn":
                        self.triggerEnchant(enchantment)

            #trigger all abilities once if not player
            if self.entityType != "player":
                for i in range(len(self.abilities)):
                    self.triggerEnchant(self.abilities[i])

            #Check if riderBoots are equipped
            if len(self.enchantments) > 0:
                for enchantment in self.enchantments:
                    if enchantment.trigger == "riderBoots":
                        if self.equipment[5] == None:
                            self.triggerEnchant(enchantment)
                        elif self.equipment[5].name != "Rider's Boots":
                            self.triggerEnchant(enchantment)

            #if 1 turn of transformation left
            if self.transformTurns == 1:
                #get normal equipment back
                self.equipment = self.equipStack
                #update stats
                self.updateStats()

                #remove cost of transformation
                self.mana -= 400 

                #fade out music over a second
                pygame.mixer.music.fadeout(1000)
                pygame.mixer.music.load('music/battle'+str(random.randint(1,4))+'.mp3')
                #fade music in over 1 second
                pygame.mixer.music.play(-1,0,1000)

                self.transformTurns = 0

                
            if self.transformTurns > 0:
                #tick down 1 turn
                self.transformTurns -=1

            self.endTurnActions = 0


        


    def move(self,newTile):
        self.tile.occupant = None
        self.tile = newTile
        self.tile.occupant = self

        self.x = self.tile.x
        self.y = self.tile.y
        self.speed -= 1

        #trigger action enchantments
        if len(self.enchantments) > 0:
            for enchantment in self.enchantments:
                if enchantment.trigger == "action":
                    self.triggerEnchant(enchantment)

        #trigger move enchantments
        if len(self.enchantments) > 0:
            for enchantment in self.enchantments:
                if enchantment.trigger == "move":
                    self.triggerEnchant(enchantment)

        

    #show stats of an entity by hovering over them
    def showStats(self):

        #only show hp and name for walls
        self.window.blit(self.font.render(self.name,True,self.colour),(0,0))
        self.window.blit(self.font.render("HP: "+str(self.health)+"/"+str(self.maxHealth),True,self.colour),(0,50))
        
        if self.entityType != "wall":
            if self.tile.x < self.mousePos[0] < self.tile.x1 and self.tile.y < self.mousePos[1] < self.tile.y1:
                for i in range (0,2):
                    if self.equipment[i] != None:
                        pygame.draw.rect(self.window, (100,100,100), (self.x - (self.equipment[i].attackRange)*self.level.tileSize, self.y - (self.equipment[i].attackRange)*self.level.tileSize, (self.equipment[i].attackRange*2)*self.level.tileSize+self.level.tileSize, (self.equipment[i].attackRange*2)*self.level.tileSize+self.level.tileSize), 5)

            self.window.blit(self.font.render(f"AP: {str(self.armour)}%/{str(self.maxArmour)}%",True,self.colour),(0,100))
            #speed now rounded to 1 d.p
            self.window.blit(self.font.render("SP: "+str(round(self.speed,2))+"/"+str(self.maxSpeed),True,self.colour),(0,150))
            self.window.blit(self.font.render("MP: "+str(self.mana)+"/"+str(self.maxMana),True,self.colour),(0,200))
            for i in range(0,2):
                if self.equipment[i] != None:
                    if i == 0:
                        self.window.blit(self.font.render("LH AT: "+str(round(self.equipment[i].attackBonus*self.mult*(1+self.attack/100))),True,self.colour),(0,250))
                        self.window.blit(self.font.render("LH Range: "+str(self.equipment[i].attackRange),True,self.colour),(0,300))
                    elif i == 1:
                        self.window.blit(self.font.render("RH AT: "+str(round(self.equipment[i].attackBonus*self.mult*(1+self.attack/100))),True,self.colour),(0,350))
                        self.window.blit(self.font.render("RH Range: "+str(self.equipment[i].attackRange),True,self.colour),(0,400))
                        
            self.window.blit(self.font.render("AT Bonus: "+str(self.attack)+"%",True,self.colour),(0,450))

        space = 0
        abilitySpace = 0
        uniqueEnchantments = set(self.enchantments)
        #renders enchantments
        for uniqueEnchantment in uniqueEnchantments:
            #renders enchantments
            if uniqueEnchantment.trigger != "ability":
                numDuplicates = 0
                for enchantment in self.enchantments:
                    if enchantment == uniqueEnchantment:
                        numDuplicates +=1
                pygame.draw.rect(self.window,(100,100,100),[0,490+space*50,280,45])
            
                #if hovering over an enchantment then show it
                if 0 < self.mousePos[0] < 280 and (490+space*50) < self.mousePos[1] < (535+space*50):
                    pygame.draw.rect(self.window,(100,0,0),[0,490+space*50,280,45])
                    #format description to include correct magnitude data
                    self.level.enchantInfo = []

                    #get values to format
                    values = []
                    for magnitude in uniqueEnchantment.magnitude:
                        values.append(str(round(abs(magnitude*self.mult))))
                    
                    #format values
                    for line in uniqueEnchantment.desc:
                        self.level.enchantInfo.append(line.format(*values))

                if numDuplicates > 1:
                    self.window.blit(self.font.render(str(numDuplicates)+"x "+uniqueEnchantment.name,True,(0,255,255)),(0,500 + space*50))
                else:
                    self.window.blit(self.font.render(uniqueEnchantment.name,True,(0,255,255)),(0,500 + space*50))
                        
                space += 1

        #renders abilities
        for ability in self.abilities:
            pygame.draw.rect(self.window,(100,100,100),[980,20+abilitySpace*100,280,95])
            
            #if hovering over an ability then show it
            if 980 < self.mousePos[0] < 1260 and (20+abilitySpace*100) < self.mousePos[1] < (115+abilitySpace*100):
                pygame.draw.rect(self.window,(100,0,0),[980,20+abilitySpace*100,280,95])
                #format description to include correct magnitude data
                self.level.enchantInfo = []

                #get values to format
                values = []
                for magnitude in ability.magnitude:
                    values.append(str(round(abs(magnitude*self.mult))))
                
                #format values
                for line in ability.desc:
                    self.level.enchantInfo.append(line.format(*values))

            self.window.blit(self.font.render("[{}]".format(abilitySpace+1),True,(0,255,255)),(1100,30+abilitySpace*100))
            self.window.blit(self.font.render(ability.name,True,(0,255,255)),(1000,70+abilitySpace*100))

            abilitySpace += 1
            

        #render turns of transformation left
        if self.transformTurns > 0:
            self.window.blit(self.smolFont.render("Turns of Transformation: "+str(self.transformTurns),True,self.colour),(1060,660))
                        
                        

    def attackEntity(self,target,weapon):
        #needed for enchantment stuff
        self.target = target
        
        #damage enemy
        damage = (round(weapon.attackBonus*self.mult*(1+self.attack/100)))

        #armour has a 1 in 10 chance to fail
        if random.random() > 0.1:
             damage = round(damage / 1+(target.armour / 100)) #armour is now a percentage
             
        if damage <= 0:
            damage = 0
            if len(target.enchantments) > 0:
                for enchantment in target.enchantments:
                    if enchantment.trigger == "block":
                        self.triggerEnchant(enchantment)
                        #print("blocked")
                        
        if target.entityType == "player" and damage >= target.maxHealth:
            #if the attack will oneshot then keep the player on 1 hp if theyre on full health
            target.health -= target.maxHealth - 1
        else:
            target.health -= damage

        
        #draw a line to the target
        self.level.attackToRender.append([(self.x+self.level.tileSize//2,self.y+self.level.tileSize//2),(target.x+self.level.tileSize//2,target.y+self.level.tileSize//2)])

        if target.health <= 0:
            target.killer = self

        #trigger enemy enchantments (they get hit)
        if len(target.enchantments) > 0:
            for enchantment in target.enchantments:
                if enchantment.trigger == "selfHit":
                    self.triggerEnchant(enchantment)
                    
        #trigger own enchantments
        if len(self.enchantments) > 0:
            for enchantment in self.enchantments:
                if enchantment.trigger == "attack":
                    self.triggerEnchant(enchantment)

        #trigger action enchantments
        if len(self.enchantments) > 0:
            for enchantment in self.enchantments:
                if enchantment.trigger == "action":
                    self.triggerEnchant(enchantment)

        if target == self:
            self.text = (self.name+" hit themselves for "+str(damage)+" HP. ")
        else:
            self.text = (self.name+" hit "+target.name+" for "+str(damage)+" HP. ")
        self.level.text.append(self.text)

    def lastWords(self):

        #trigger death enchantments
        if len(self.enchantments) > 0:
            for enchantment in self.enchantments:
                if enchantment.trigger == "death":
                    self.triggerEnchant(enchantment)

        #trigger enemy's kill enchantments
        if self.killer != None:
            if len(self.killer.enchantments) > 0:
                for enchantment in self.killer.enchantments:
                    if enchantment.trigger == "kill":
                        self.killer.triggerEnchant(enchantment)
                        
        #remove all trace of entity on death
        self.tile.occupant = None

        #RIP entity item drop code

    def findTarget(self,targetTeam): #better threat detecion
        lowestDistance = [10000,10000]
        target = None
        for entity in self.level.entities:
            if self.entityType == "ally" or self.entityType == "player":
                if (entity.entityType == "enemy" and targetTeam == "enemy") or ((entity.entityType == "ally" or entity.entityType == "player") and targetTeam == "ally" and entity != self):
                    #calculate distance
                    xDistance = abs(entity.x - self.x)
                    yDistance = abs(entity.y - self.y)
                    #find lowest xDistance and YDistance
                    if xDistance < lowestDistance[0] or yDistance < lowestDistance[1]:
                        lowestDistance = [xDistance,yDistance]
                        target = entity
                    
                 
            elif self.entityType == "enemy":
                if (entity.entityType == "enemy" and targetTeam == "ally") or ((entity.entityType == "ally" or entity.entityType == "player") and targetTeam == "enemy" and entity != self ):
                    #calculate distance
                    xDistance = abs(entity.x - self.x)
                    yDistance = abs(entity.y - self.y)
                    #find lowest xDistance and YDistance
                    if xDistance < lowestDistance[0] or yDistance < lowestDistance[1]:
                        lowestDistance = [xDistance,yDistance]
                        target = entity
        return target
    
    def rangedAttack(self,target,weapon):
        dx = (target.x - self.x)
        dy = (target.y - self.y)
        self.target = target
        #checks if npc is in range
        if abs(dx) <= weapon.attackRange*self.level.tileSize and abs(dy) <= weapon.attackRange*self.level.tileSize:
            dx = dx/weapon.attackRange
            dy = dy/weapon.attackRange
            #check all tiles to ensure they dont block the ray
            #step up in terms of self.level.tileSize (1 tile distance in pixels)
            for step in range (1,weapon.attackRange):
                #print(step)
                for row in self.level.tiles:
                    for tile in row:
                        #if there is a wall in the way (+self.level.tileSize//2 added to ensure it aims at the centre of the player
                        if tile.x <= self.x+self.level.tileSize//2 + (dx * step) <= tile.x1 and tile.y <= self.y+self.level.tileSize//2 + (dy * step) <= tile.y1 and tile.occupant != None:
                            if tile.occupant.entityType == "wall":
                                return False   
            #trigger action enchantments
            if len(self.enchantments) > 0:
                for enchantment in self.enchantments:
                    if enchantment.trigger == "rangedAttack":
                        self.triggerEnchant(enchantment) 
            return True

    def triggerEnchant(self,enchantment):
        #all possible effects
        def applyEffect(enchantment,origin,target):
            if target != None:

                #deduct mana
                if origin.mana >= enchantment.cost or enchantment.cost == 0:
                    origin.mana -= enchantment.cost

                    ##if enchantment just triggered is an ability,
                    if enchantment.trigger == "ability":
                        for enchant in origin.enchantments:
                                #trigger all enchantments that are triggered when another
                                #ability is triggered
                                if enchant.trigger == "otherAbility":
                                    self.triggerEnchant(enchant)
                        
                    #enchantments can now have multiple effects
                    for i in range(len(enchantment.effectType)):
                        
                        if origin != target:
                            originName = origin.name+"'s "
                        else:
                            originName = "their "

                        ##new statDepend stuff
                        magnitude = enchantment.magnitude[i]
                        if enchantment.statDepend[i] == "mp":
                            magnitude = origin.mana * magnitude

                        elif enchantment.statDepend[i] == "sp":
                            magnitude = origin.speed * magnitude

                        elif enchantment.statDepend[i] == "maxSp":
                            magnitude = origin.maxSpeed * magnitude

                        elif enchantment.statDepend[i] == "ap":
                            magnitude = origin.armour * magnitude

                        elif enchantment.statDepend[i] == "at":
                            magnitude = origin.attack * magnitude

                        elif enchantment.statDepend[i] == "hp":
                            magnitude = origin.health * magnitude
                            
                            
                                
                        if enchantment.effectType[i] == "hp":
                            target.health -= round(magnitude*self.mult)
                            if magnitude > 0:
                                self.text = (target.name+" was damaged by "+originName+enchantment.name+" for "+str(round(magnitude*self.mult))+" HP. ")
                                
                                if target.health <= 0:
                                    target.killer = self
                            else:
                                self.text = (target.name+" was healed by "+originName+enchantment.name+" for "+str(-1*round(magnitude*self.mult))+" HP. ")
                                ##no more overheals
                                if target.maxHealth < target.health:
                                    target.health = target.maxHealth
                                    ##refund mana
                                    origin.mana += enchantment.cost
                                    
                            ##also draw line to target
                            self.level.attackToRender.append([(self.x+self.level.tileSize//2,self.y+self.level.tileSize//2),(target.x+self.level.tileSize//2,target.y+self.level.tileSize//2)])
                                
                        elif enchantment.effectType[i] == "sp":
                            #speed no longer effected by mult to prevent 1-sided battles in the late game
                            target.speed -= magnitude
                            if magnitude > 0:
                                self.text = (target.name+" was slowed by "+originName+enchantment.name+" for "+str(round(magnitude*self.mult))+" SP. ")
                            else:
                                self.text = (target.name+" was hastened by "+originName+enchantment.name+" for "+str(-1*round(magnitude*self.mult))+" SP. ")
                            ##also draw line to target
                            self.level.attackToRender.append([(self.x+self.level.tileSize//2,self.y+self.level.tileSize//2),(target.x+self.level.tileSize//2,target.y+self.level.tileSize//2)])

                        elif enchantment.effectType[i] == "ap" or enchantment.effectType[i] == "tempAp":
                            target.armour -= round(magnitude*self.mult)
                            ##no more getting armour below 0
                            if target.armour < 0:
                                target.armour = 0
                            #needed for temp effects
                            if enchantment.effectType[i] == "tempAp":
                                self.tempArmour -= round(magnitude*self.mult)
                            if magnitude > 0:
                                self.text = (target.name+" was made vulnerable by "+originName+enchantment.name+" for "+str(round(magnitude*self.mult))+" AP. ")
                            else:
                                self.text = (target.name+"'s defence was bolstered by "+originName+enchantment.name+" for "+str(-1*round(magnitude*self.mult))+" AP. ")
                            
                            ##also draw line to target
                            self.level.attackToRender.append([(self.x+self.level.tileSize//2,self.y+self.level.tileSize//2),(target.x+self.level.tileSize//2,target.y+self.level.tileSize//2)])
                                
                        elif enchantment.effectType[i] == "mp":
                            target.mana -= round(magnitude*self.mult)
                            if magnitude > 0:
                                self.text = (target.name+" was drained by "+originName+enchantment.name+" for "+str(round(magnitude*self.mult))+" MP. ")
                            else:
                                self.text = (target.name+" was empowered by "+originName+enchantment.name+" for "+str(-1*round(magnitude*self.mult))+" MP. ")
                                ##no more overmagic
                                if target.maxMana < target.mana:
                                    target.mana = target.maxMana
                                    ##refund mana
                                    origin.mana += enchantment.cost

                            ##also draw line to target
                            self.level.attackToRender.append([(self.x+self.level.tileSize//2,self.y+self.level.tileSize//2),(target.x+self.level.tileSize//2,target.y+self.level.tileSize//2)])
                                
                        elif enchantment.effectType[i] == "dmg" or enchantment.effectType[i] == "tempDmg":
                            target.attack -= round(magnitude*self.mult)
                            #needed for temp effects
                            if enchantment.effectType[i] == "tempDmg":
                                self.tempAttack -= round(magnitude*self.mult)
                            if magnitude > 0:
                                self.text = (target.name+" was weakened by "+originName+enchantment.name+" for "+str(round(magnitude*self.mult))+" AT. ")
                            else:
                                self.text = (target.name+" was strengthened by "+originName+enchantment.name+" for "+str(-1*round(magnitude*self.mult))+" AT. ")
                                
                            ##also draw line to target
                            self.level.attackToRender.append([(self.x+self.level.tileSize//2,self.y+self.level.tileSize//2),(target.x+self.level.tileSize//2,target.y+self.level.tileSize//2)])


                        #status effects
                        elif enchantment.effectType[i] == "poison":
                            if magnitude == "all":
                                for Spellbook.poison in target.enchantments:
                                    target.enchantments.remove(Spellbook.poison)
                            else:
                                #don't give status effects to walls, refund cost
                                if target.entityType == "wall":
                                    origin.mana += enchantment.cost
                                else:
                                    for i in range(round(magnitude*self.mult)):
                                        target.enchantments.append(Spellbook.poison)
                                        self.text = (target.name+" has been sickened with "+str(round(magnitude*self.mult))+" stacks of Poison. ")

                        elif enchantment.effectType[i] == "disease":
                            if magnitude == "all":
                                for Spellbook.disease in target.enchantments:
                                    target.enchantments.remove(Spellbook.disease)
                            else:
                                #don't give status effects to walls, refund cost
                                if target.entityType == "wall":
                                    origin.mana += enchantment.cost
                                else:
                                    for i in range(round(magnitude*self.mult)):
                                        target.enchantments.append(Spellbook.disease)
                                        self.text = (target.name+" has been infected with "+str(round(magnitude*self.mult))+" stacks of Disease. ")
                                    
                        elif enchantment.effectType[i] == "frost":
                            if magnitude == "all":
                                for Spellbook.frost in target.enchantments:
                                    target.enchantments.remove(Spellbook.frost)
                            else:
                                #don't give status effects to walls, refund cost
                                if target.entityType == "wall":
                                    origin.mana += enchantment.cost
                                else:
                                    for i in range(round(magnitude*self.mult)):
                                        target.enchantments.append(Spellbook.frost)
                                        self.text = (target.name+" has been frozen with "+str(round(magnitude*self.mult))+" stacks of Frost. ")
                                    
                        elif enchantment.effectType[i] == "starSeed":
                            if magnitude == "all":
                                for Spellbook.starSeed in target.enchantments:
                                    target.enchantments.remove(Spellbook.starSeed)
                            else:
                                #don't give status effects to walls, refund cost
                                if target.entityType == "wall":
                                    origin.mana += enchantment.cost
                                else:
                                    for i in range(round(magnitude*self.mult)):
                                        target.enchantments.append(Spellbook.starSeed)
                                        self.text = (target.name+" has been implanted with "+str(round(magnitude*self.mult))+" Star Seeds. ")

                        elif enchantment.effectType[i] == "burn":
                            if magnitude == "all":
                                for Spellbook.burn in target.enchantments:
                                    target.enchantments.remove(Spellbook.burn)
                            else:
                                #don't give status effects to walls, refund cost
                                if target.entityType == "wall":
                                    origin.mana += enchantment.cost
                                else:
                                    for i in range(round(magnitude*self.mult)):
                                        target.enchantments.append(Spellbook.burn)
                                        self.text = (target.name+" has been wounded by "+str(round(magnitude*self.mult))+" stacks of Burn. ")

                        elif enchantment.effectType[i] == "burnEnchant":
                            #don't give enchants to walls, refund cost
                            if target.entityType == "wall":
                                origin.mana += enchantment.cost
                            else:
                                addEnchant = True
                                for enchant in target.enchantments:
                                    #if enchant already applied, refund cost
                                    if enchant == Spellbook.burningWeapon:
                                        origin.mana += enchantment.cost
                                        addEnchant = False
                                        break
                                #if enchant not already applied, apply it
                                if addEnchant == True:
                                    target.enchantments.append(Spellbook.burningWeapon)
                                    self.text = (target.name+"'s weapon has been set aflame, it now applies Burn on attack. ")

                        elif enchantment.effectType[i] == "enchantRemove":
                            if magnitude == "all":
                                for enchantment in target.enchantments:
                                    target.enchantments.remove(enchantment)
                            else:
                                for i in range(round(magnitude*self.mult)):
                                    if len(target.enchantments) > 0:
                                        self.text = (target.name+" has had "+target.enchantments[-1].name+" removed. ")
                                        #removes enchantment at end of list
                                        target.enchantments.pop(-1)

                        elif enchantment.effectType[i] == "multRemove":
                            #we dont want mult to become negative
                            #divide by 100 so magnitude can be displayed as percentage but function as mult
                            if magnitude/100 < target.mult:
                                target.mult -= magnitude/100
                            else:
                                target.mult = 0
                            
                            self.text = (target.name+" has had their Sacrifice reduced by"+str(magnitude)+"%. ")

                        #transformation
                        elif enchantment.effectType[i] == "wyvern":
                            target.equipment = (Armoury.stoneTotemTwo,None,None,None,None,None)
                            target.updateStats()
                            target.speed = target.maxSpeed
                            target.transformTurns += round(magnitude*self.mult)
                            self.text = (target.name+" has succumbed to Drakkak's anger and has transformed. This will last "+str(target.transformTurns)+" turns. ")

                            #trigger transform enchantments
                            if len(self.enchantments) > 0:
                                for enchantment in self.enchantments:
                                    if enchantment.trigger == "transform":
                                        self.triggerEnchant(enchantment)
                            
                            #fade out music over a second
                            #pygame.mixer.music.fadeout(1000)
                            pygame.mixer.music.load('music/Ride the Fire!.flac')
                            pygame.mixer.music.play(-1,0,0)
                            pygame.mixer.music.set_volume(0.6)

                        #teleportation
                        elif enchantment.effectType[i] == "teleport":
                            for i in range(magnitude):
                                for tile in target.tile.adjTiles:
                                    if tile != None:
                                        if tile.occupant == None:
                                            self.move(tile)
                                            #offset speed taken from teleporting
                                            self.speed += 1
                                            break
                            
                            #TODO: add enchantments that trigger on teleport


                        #enchantments can also trigger attacks
                        elif enchantment.effectType[i] == "attack":
                            #for each weapon
                            for j in range(int(abs(magnitude))):
                                for i in range(0,2):
                                    if origin.equipment[i] != None:
                                        #if weapon is ranged, try to attack
                                        if origin.equipment[i].attackRange > 1 and origin.rangedAttack(target,origin.equipment[i]):
                                            origin.attackEntity(target,origin.equipment[i])
                                        #if weapon is melee, try to attack
                                        elif origin.equipment[i].attackRange == 1:
                                            #check target is adjacent first
                                            for tile in origin.tile.adjTiles:
                                                if tile != None:
                                                    if tile.occupant == target:
                                                        origin.attackEntity(target,origin.equipment[i])

                        #attack enemy at any range
                        elif enchantment.effectType[i] == "rangedAttack":
                            for j in range(int(abs(magnitude))):
                                for i in range(0,2):
                                    if origin.equipment[i] != None:
                                        origin.attackEntity(target,origin.equipment[i])

                        #there'll be  a lot of summon stuff
                        else:
                            numSummons = magnitude
                            for tile in self.tile.adjTiles:
                                if tile != None:
                                    if tile.occupant == None:
                                        if self.entityType == "enemy":
                                            summonType = "enemy"
                                        elif self.entityType == "player" or self.entityType == "ally":
                                            summonType = "ally"
                                            
                                        if enchantment.effectType[i] == "frosthound":
                                            #summon frosthound on same team
                                            allyStats = Tables.direWolf
                                            ally = NPC(self.window,self.level,tile,allyStats[0],allyStats[1],allyStats[2],allyStats[3],allyStats[4],allyStats[5],allyStats[6],summonType,self.mult)
                                            self.text = (self.name+" has summoned "+ally.name+" using "+enchantment.name+". ")
                                            tile.occupant = ally

                                        if enchantment.effectType[i] == "fireball":
                                            #summon fireball on same team
                                            allyStats = Tables.fireball
                                            ally = NPC(self.window,self.level,tile,allyStats[0],allyStats[1],allyStats[2],allyStats[3],allyStats[4],allyStats[5],allyStats[6],summonType,self.mult)
                                            self.text = (self.name+" has summoned "+ally.name+" using "+enchantment.name+". ")
                                            tile.occupant = ally

                                        elif enchantment.effectType[i] == "phalanx":
                                            allyStats = Tables.phalanxGrowth
                                            ally = NPC(self.window,self.level,tile,allyStats[0],allyStats[1],allyStats[2],allyStats[3],allyStats[4],allyStats[5],allyStats[6],summonType,self.mult)
                                            self.text = (self.name+" has created a "+ally.name+" using "+enchantment.name+". ")
                                            tile.occupant = ally

                                        elif enchantment.effectType[i] == "ballista":
                                            allyStats = Tables.ballistaGrowth
                                            ally = NPC(self.window,self.level,tile,allyStats[0],allyStats[1],allyStats[2],allyStats[3],allyStats[4],allyStats[5],allyStats[6],summonType,self.mult)
                                            self.text = (self.name+" has created a "+ally.name+" using "+enchantment.name+". ")
                                            tile.occupant = ally

                                        elif enchantment.effectType[i] == "throne":
                                            ally = NPC(self.window,self.level,tile,Armoury.longsword,None,None,Armoury.winterCore,None,None,"The Throne of Winter",summonType,self.mult)
                                            self.text = (self.name+" has summoned "+ally.name+" using "+enchantment.name+". ")
                                            tile.occupant = ally

                                        elif enchantment.effectType[i] == "osirisTwo":
                                            ally = NPC(self.window,self.level,tile,Armoury.severingblade,None,Armoury.starScar,Armoury.osirisAttire2,Armoury.osirisTrousers,Armoury.starWalker,"Osiris the Starbane",summonType,self.mult)
                                            self.text = ("--Second Phase--. ")
                                            tile.occupant = ally

                                            #now with 2nd phase music
                                            pygame.mixer.music.fadeout(1000)
                                            pygame.mixer.music.load('music/Heolstor 2.mp3')
                                            pygame.mixer.music.play(-1,0,1000)

                                        elif enchantment.effectType[i] == "crystalLump":
                                            ally = NPC(self.window,self.level,tile,None,None,None,Armoury.crystalLumpPlayer,None,None,"Crystal Growth",summonType,self.mult)
                                            self.text = (self.name+" has created a "+ally.name+" using "+enchantment.name+". ")
                                            tile.occupant = ally
                                            
                                        #buff enemy summons
                                        if tile.occupant != None:
                                            if tile.occupant.entityType == "enemy":
                                                tile.occupant.speed += tile.occupant.maxSpeed

                                            #trigger spawn effects:
                                            for enchant in tile.occupant.enchantments:
                                                if enchant.trigger == "spawn":
                                                    tile.occupant.triggerEnchant(enchantment)

                                        numSummons -= 1
                                        if numSummons <= 0:  
                                            break
            

                else:
                    self.text = (origin.name+" has run out of mana. ")

                #print(self.text)
                self.level.text.append(self.text)

                    
        #apply effect on specific target from specific origin
        if enchantment.target == "attacker":
            #apply enchantment effect (enchantment,cause,target)
            applyEffect(enchantment,self.target,self)
        elif enchantment.target == "target":
            applyEffect(enchantment,self,self.target)
        elif enchantment.target == "self":
            if enchantment.trigger == "selfHit":
                applyEffect(enchantment,self.target,self.target)
            else:
                applyEffect(enchantment,self,self)

        elif enchantment.target == "adjAll" or enchantment.target == "adjEnemies" or enchantment.target == "adjAllies":
            for tile in self.tile.adjTiles:
                if tile != None:
                    if tile.occupant != None:
                        applyEffect(enchantment,self,tile.occupant)

        elif enchantment.target == "all":
            for entity in self.level.entities:
                #dont include walls to prevent spam in the log
                if entity.entityType != "wall":
                    applyEffect(enchantment,self,entity)

        #allAllies includes self
        elif enchantment.target == "allAllies":
            for entity in self.level.entities:
                if entity.entityType == self.entityType or (entity.entityType == "player" and self.entityType == "ally") or (entity.entityType == "ally" and self.entityType == "player"):
                    applyEffect(enchantment,self,entity)

        elif enchantment.target == "allEnemies":
            for entity in self.level.entities:
                if entity.entityType != self.entityType and entity.entityType != "wall":
                    if not((entity.entityType == "player" and self.entityType == "ally") or (entity.entityType == "ally" and self.entityType == "player")):
                        applyEffect(enchantment,self,entity)

        elif enchantment.target == "allWalls":
            for entity in self.level.entities:
                if entity.entityType == "wall":
                    applyEffect(enchantment,self,entity)

        elif enchantment.target == "nearestEnemy":
            applyEffect(enchantment,self,self.findTarget("enemy"))
        elif enchantment.target == "nearestAlly":
            applyEffect(enchantment,self,self.findTarget("ally"))

        
            
                
        
            
        
                        
#we gettin fancy with inheritances
class Player(Entity):

    def action(self):
        self.colour = (0,100,0)
        
        #if turn has ended and player is selected
        if self.endTurn == True and self.level.selectedPlayer == self:
            #remove self as selected player to stop the game freezing
            self.level.selectedPlayer = None
            
        #if turn hasnt ended and player is selected
        elif self.endTurn == False and self.level.selectedPlayer == self:
            self.colour = (0,255,0)
            self.tileSelected = None
            #variables for new attack code
            target = None
            attacked = False 

            #check all tiles
            for row in self.level.tiles:
                for tile in row:
                    if tile != None:
                        #if mouse is hovering over a tile which exists
                        if tile.x < self.mousePos[0] < tile.x1 and tile.y < self.mousePos[1] < tile.y1:
                            #mark that tile as selected
                            self.tileSelected = tile

                            if self.tileSelected.occupant != None:
                                target = self.tileSelected.occupant

                            self.window.blit(self.crosshair,[tile.x,tile.y])                               

            for event in pygame.event.get():
                #checks if mouse is clicked on a tile that exists
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #if RMB pressed:
                    if event.button == 3:
                        if target != None:
                            if target.entityType == "player":
                                #select player on level's behalf
                                self.level.selectedPlayer = target
                            
                    #if LMB pressed:
                    if event.button == 1:
                        if self.tileSelected != None:

                            #if there is an enemy to attack
                            if target != None:
                                #for each weapon
                                for i in range(0,2):
                                    if self.equipment[i] != None:
                                        #if weapon is ranged, try to attack
                                        if self.equipment[i].attackRange > 1 and self.rangedAttack(target,self.equipment[i]):
                                            self.attackEntity(target,self.equipment[i])
                                            attacked = True
                                            #print(self.name,"has made a ranged attack")
                                            
                                        #else if weapon is melee, try to attack
                                        elif self.tileSelected.occupant != None and self.tileSelected in self.tile.adjTiles:
                                            self.attackEntity(self.tileSelected.occupant,self.equipment[i])
                                            attacked = True
                                            #print(self.name,"has made a melee attack")
                                            

                                #subtract speed if attack hits            
                                if attacked == True:
                                    self.speed -= 1

                                    
                            #if tile is adjacent
                            elif self.tileSelected in self.tile.adjTiles:
                                #if tile isnt occupied
                                if self.tileSelected.occupant == None:
                                    #move to clicked tile
                                    self.move(self.tileSelected)

                elif event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()
                    break

                
            pressed = pygame.key.get_pressed()
            #skip turn
            if pressed[pygame.K_RETURN]:
                self.speed = 0
                pygame.time.wait(20)

            #main menu
            if pressed[pygame.K_ESCAPE]:
                Menus.mainMenu(self.window)

            elif pressed[pygame.K_1] or pressed[pygame.K_2] or pressed[pygame.K_3] or pressed[pygame.K_4] or pressed[pygame.K_5] or pressed[pygame.K_6]:
                #trigger abilities
                for i in range(len(self.abilities)):
                    if pressed[pygame.K_1] and i == 0:
                        self.triggerEnchant(self.abilities[i])
                    elif pressed[pygame.K_2] and i == 1:
                        self.triggerEnchant(self.abilities[i])
                    elif pressed[pygame.K_3] and i == 2:
                        self.triggerEnchant(self.abilities[i])
                    elif pressed[pygame.K_4] and i == 3:
                        self.triggerEnchant(self.abilities[i])
                    elif pressed[pygame.K_5] and i == 4:
                        self.triggerEnchant(self.abilities[i])
                    elif pressed[pygame.K_6] and i == 5:
                        self.triggerEnchant(self.abilities[i])
                    pygame.time.wait(60)
                                
        #render team
        pygame.draw.rect(self.window,self.colour,[self.tile.x,self.tile.y,55,55])
        #render sprite
        if self.image != None:
            self.window.blit(self.image,[self.x,self.y])
        #round speed to 1 d.p
        self.window.blit(self.font.render(str(round(self.speed,2)),True,(255,255,255)),(self.x + 15, self.y + 15))
            

class NPC(Entity):
    def pathAlgorithm(self,tile,target): #incredibly dumb ai TODO: make smarter
        
        if tile != None:
            xDistance = abs(target.x - tile.x)
            yDistance = abs(target.y - tile.y)
            #add these together
            distance = xDistance + yDistance

            #find lowest xDistance and YDistance
            if distance < self.pathfinding:
                #only attempt to move to a tile that isnt occupied by an entity of the same faction
                if tile.occupant == None:
                    self.tileSelected = tile
                    self.pathfinding = distance
                #only attempt to move to a tile that isnt occupied by an entity of the same faction
                elif (not(tile.occupant.entityType == "ally" or tile.occupant.entityType == "player") and self.entityType == "ally") or  (tile.occupant.entityType != "enemy" and self.entityType == "enemy"):
                    #if the tile is occupied by a wall, only break through if theres no other option
                    if tile.occupant.entityType == "wall":
                        if self.tileSelected == None:
                            self.tileSelected = tile
                            self.pathfinding = distance
                    else:
                        self.tileSelected = tile
                        self.pathfinding = distance

            #prevent enemys hitting themselves
            if self.tileSelected == self.tile:
                self.tileSelected = None
            
        
    def action(self):
        #find target:
        target = self.findTarget("enemy")
        if self.endTurn == False and target != None:
            #define a target to move towards
            #TODO: base it on closest enemy

            #keep track of if entity has attacked
            attacked = False

            ##trigger action enchantments
            #if len(self.enchantments) > 0:
                #for enchantment in self.enchantments:
                    #if enchantment.trigger == "action":
                        #self.triggerEnchant(enchantment) 
            

            #change this to set the maximum engagement range
            self.pathfinding = 10000

            #run the pathing algorithm on every adjacent tile
            #for every adjacent tile
            for tile in self.tile.adjTiles:
                #find the closest to the player
                self.pathAlgorithm(tile,target)

            #for each weapon
            for i in range(0,2):
                if self.equipment[i] != None:
                    #if weapon is ranged, try to attack
                    if self.equipment[i].attackRange > 1 and self.rangedAttack(target,self.equipment[i]):
                        self.attackEntity(target,self.equipment[i])
                        attacked = True
                        #print(self.name,"has made a ranged attack")
                    #if weapon is melee, try to attack
                    if self.tileSelected != None:
                        if self.tileSelected.occupant != None:
                            self.attackEntity(self.tileSelected.occupant,self.equipment[i])
                            attacked = True
                        #print(self.name,"has made a melee attack")

            #subtract speed if attack hits            
            if attacked == True:
                self.speed -= 1
                
            #if a tile is selected and no one is on it then move to it
            elif self.tileSelected != None and self.tileSelected.occupant == None:
                self.move(self.tileSelected)
            #if no tile is selected, stand still and end turn
            elif self.tileSelected == None:
                self.speed -= 1



        #no target? dont move
        if target == None:
            self.speed = 0
            
        #render team
        pygame.draw.rect(self.window,self.colour,[self.tile.x,self.tile.y,55,55])
        #render sprite
        if self.image != None:
            self.window.blit(self.image,[self.x,self.y])

            
class Wall(Entity):
    def action(self):
        self.window.blit(self.image,[self.x,self.y])
