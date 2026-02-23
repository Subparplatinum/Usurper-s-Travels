import pygame
import random
import Entity
import Armoury
import Tables
import sys
import Menus
#easily accessable variables
import Debug

class Tile:
    def __init__(self,x,y,path,tileSize):
        #tile image
        if random.random() < 0.2:
            self.image = pygame.image.load(path+"floor2.png")
        else:
            self.image = pygame.image.load(path+"floor.png")

        self.x = x
        self.y = y

        self.tileSize = tileSize
        self.x1 = self.x + self.tileSize
        self.y1 = self.y + self.tileSize

        #define adjacent tiles
        self.left = None
        self.right = None
        self.up = None
        self.down = None

        self.upLeft = None
        self.downLeft = None
        self.upRight = None
        self.downRight = None
        
        #define possible entity in tile
        self.occupant = None

        self.adjTiles = []

    def update(self,window):
        #draw
        window.blit(self.image,[self.x,self.y])


class Level:
    def __init__(self,window,lastLevel):
        self.endTurnText = pygame.image.load("sprites/theWorldTurns.png")

        self.levelComplete = False
        #for rendering enchantment effects
        self.bossFont = pygame.font.SysFont(None,40)
        self.font = pygame.font.SysFont(None,30)
        self.smolFont = pygame.font.SysFont(None,20)
        self.text = ["","","","","","","","","",""]
        self.colour = (255,255,255) #white for text

        #lore stuff
                    
        
        #generate level
        #10x10 tiles
        #90 x 90 px
        self.tiles = []
        #store all entities in level
        self.entities = []
        #store all dead entities in level
        self.deadEntities = []

        #store tile size for easy resizing in future
        self.tileSize = 60

        #store all items collected this level
        self.items = []

        #pick a spawn table (normal or boss):
        self.table = random.random()

        #store the selected entity
        self.selectedEntity = None

        #store attacks that need to be rendered
        self.attackToRender = []

        #store player currently being controlled
        self.selectedPlayer = None


        #keep track of level number (used for spawning bosses)
        if lastLevel == None:
            self.levelNum = Debug.levelNum
            self.mult = 1
        else:
            self.levelNum = lastLevel.levelNum + 1
            self.mult = lastLevel.mult + Debug.enemyMultBonus #enemy mult

        #super bosses (spawn at level 20)
        # Temporarily level 10
        if self.levelNum%10 == 0:
            self.spawnTable = Tables.superBossTables[random.randint(0,len(Tables.superBossTables)-1)]
            self.tableType = "superBoss"
            location = 3

            
        #boss table (spawn evey 5 levels)
        elif self.levelNum%5 == 0:
            self.spawnTable = Menus.selectBoss(window)
            self.tableType = "boss"
            location = 3
            
        #normal table (spawn every other time)
        else:
            self.spawnTable = Tables.spawnTables[random.randint(0,len(Tables.spawnTables)-1)]
            self.tableType = "normal"
            location = 2
            

        #this will be true when it is time for a world turn to take place
        self.endTurn = False

        self.window = window

    ##################################

        #change chance of wall spawning depending on environment
        wallChance = 0.2

        if self.spawnTable[location] == "The Wilderness":
            wallChance = 0.02


        #level sprites
        self.spritePath = self.spawnTable[1]

        #generate the level
        self.tiles = self.levelGen(self.window,self.tileSize,self.spritePath,wallChance)

    ##################################

        #spawn player and companion in random tile at start of game
        if lastLevel == None:

            for i in range(2):
                xcoord = random.randint(0,len(self.tiles[1])-1)
                ycoord = random.randint(0,len(self.tiles)-1)

                while self.tiles[ycoord][xcoord].occupant != None:
                    xcoord = random.randint(0,len(self.tiles[1])-1)
                    ycoord = random.randint(0,len(self.tiles)-1)

                if i == 0:   
                    #player
                    self.tiles[ycoord][xcoord].occupant = Menus.characterMenu(self.window,self,ycoord,xcoord)

                #temporarily removed

                elif i == 1:
                    #select a companion
                    self.tiles[ycoord][xcoord].occupant = Menus.companionMenu(self.window,self,ycoord,xcoord)

        #spawn player and companion in random tile after start of game (if they are still alive)
        if lastLevel != None:
            for entity in lastLevel.entities:
                if entity.entityType == "player":
                    #attempting random spawn locations
                    xcoord = random.randint(0,len(self.tiles[1])-1)
                    ycoord = random.randint(0,len(self.tiles)-1)
                    while self.tiles[ycoord][xcoord].occupant != None:
                        xcoord = random.randint(0,len(self.tiles[1])-1)
                        ycoord = random.randint(0,len(self.tiles)-1)
                    self.tiles[ycoord][xcoord].occupant = Entity.Player(window,self,self.tiles[ycoord][xcoord],entity.equipment[0],entity.equipment[1],entity.equipment[2],entity.equipment[3],entity.equipment[4],entity.equipment[5],entity.name,"player",entity.mult,entity.sigEnchant)
                    

        #spawn enemies in random tiles
        if self.tableType == "normal":
            #number of enemies increases with mult
            numEnemies = random.randint(int(1*self.mult),int(3*self.mult))
            for i in range(numEnemies):
                #pick enemy from spawn table
                enemy = self.spawnTable[0][random.randint(0,len(self.spawnTable[0])-1)]
                #select tile to spawn enemy on
                randRow = random.randint(0,len(self.tiles)-1)
                randTile = random.randint(0,len(self.tiles[randRow])-1)
                while self.tiles[randRow][randTile].occupant != None:
                    randRow = random.randint(0,len(self.tiles)-1)
                    randTile = random.randint(0,len(self.tiles[randRow])-1)
                #spawn enemy
                #enemies' stats are no longer affected by mult, only their quantity
                self.tiles[randRow][randTile].occupant = Entity.NPC(self.window,self,self.tiles[randRow][randTile],enemy[0],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5],enemy[6],enemy[7],self.mult)

        #spawn boss in random tile
        elif self.tableType == "boss" or self.tableType == "superBoss":
            #if boss spawn table used then spawn all enemies in list
            for enemy in self.spawnTable[0]:
                randRow = random.randint(0,len(self.tiles)-1)
                randTile = random.randint(0,len(self.tiles[randRow])-1)
                while self.tiles[randRow][randTile].occupant != None:
                    randRow = random.randint(0,len(self.tiles)-1)
                    randTile = random.randint(0,len(self.tiles[randRow])-1)
                #spawn boss
                #bosses are also no longer affected by mult
                self.tiles[randRow][randTile].occupant = Entity.NPC(self.window,self,self.tiles[randRow][randTile],enemy[0],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5],enemy[6],enemy[7],self.mult)

            


            #render lore

            #find length of dialogue

            #boss speaks (boss will always be first entity in list)
            textToRender = self.spawnTable[0][0][8]
            #find length of dialogue
            lenDialogue = len(textToRender)
            
            textToRender.append("-Press ENTER to continue-")
            #print(lenDialogue)

            #fade out music over a second
            pygame.mixer.music.fadeout(1000)
            #load boss theme
            pygame.mixer.music.load(self.spawnTable[2])
            #fade music in over 1 second
            pygame.mixer.music.play(-1,0,1000)

            finished = False
            while finished == False:
            
                #render boss title card
                self.window.fill((0,0,0))
                #if too much text, shrink it so its readable
                if lenDialogue >= 20:
                    Menus.drawText(self.window,self.font,self.colour,textToRender,0,0,20)
                else:
                    Menus.drawText(self.window,self.bossFont,self.colour,textToRender,0,0,40)
                pygame.display.flip()

                #let player move on when they want
                for event in pygame.event.get():
                    pressed = pygame.key.get_pressed()
                    if pressed[pygame.K_RETURN]:
                        #player is ready to move on
                        finished = True
                        self.window.fill((0,0,0))
            

        #now all entities are spawned, trigger their spawn effects:
        for entity in self.entities:
            for enchantment in entity.enchantments:
                if enchantment.trigger == "spawn":
                    entity.triggerEnchant(enchantment)


    def update(self,items):
        #presume there will be a world turn
        self.endTurn = True
        
        #draw every tile
        for row in self.tiles:
            for tile in row:
                tile.update(self.window)


        #assume level is complete
        self.levelComplete = True
        entityCount = 0
        for entity in self.entities:
            entity.update()
            #see what the other entities are up to
            if entity.entityType == "ally" or entity.entityType == "enemy":
                #if their turn is incomplete
                if entity.endTurn == False:

                    #update screen so you can actually see whats going on
                    pygame.display.flip()

                    #slow the game down
                    if entityCount < 10:
                        pygame.time.wait(120)
                    elif entityCount >= 10:
                        pygame.time.wait(60)

                        
                #mark level as complete if all enemies are slain
                if entity.entityType == "enemy":
                    self.levelComplete = False
            #stop turn from ending if entities still have goes left
            if entity.endTurn == False:
                self.endTurn = False
            #if entity is dead
            if entity.health <= 0:
                self.deadEntities.append(entity)
                
            entityCount += 1

        for entity in self.deadEntities:
            if entity != None:
                #delete all dead entites from list of entities and trigger death effects
                entity.lastWords()
                self.entities.remove(entity)
                #if entity was a player (perhaps here due to a retaliation attack), deselect them so the game doesn't crash
                if entity.entityType == "player":
                    self.selectedPlayer = None
        #reset list of dead entities
        self.deadEntities = []

        if self.endTurn == True: 
            self.worldTurn()

        #if level is complete remove items from this sinking ship
        if self.levelComplete == True:
            for item in self.items:
                items.append(item)
                
            ##add 1-3 items from the loot table to this list too (if normal level)
            if self.tableType == "normal":
                for item in random.sample(Armoury.lootTable, random.randint(1,3)):
                    items.append(item)
                    
            #else, add 1 item from boss loot table
            else:
                if self.spawnTable[5] != None:
                    #add boss drop to items
                    items.append(random.sample(self.spawnTable[5], 1)[0]) 
                    
                
            self.players = []
            #append all players to a special array so they can be easily accessed for inventory reasons
            for entity in self.entities:
                if entity.entityType == "player":
                    #untransform entites and update them 1 last time
                    if entity.transformTurns > 0:
                        entity.transformTurns = 1
                    entity.endTurn = True
                    entity.speed = 0
                    entity.endTurnActions = 1
                    entity.update()
                    self.players.append(entity)

            #if a boss was just beaten remove them from the pool
            if self.tableType == "boss":
                Tables.bossTables.remove(self.spawnTable)
                
                
            

        #render text of enchantments that have just been triggered
        self.window.blit(self.smolFont.render(self.text[-9]+self.text[-10],True,self.colour),(300,680))
        self.window.blit(self.smolFont.render(self.text[-7]+self.text[-8],True,self.colour),(300,710))
        self.window.blit(self.smolFont.render(self.text[-5]+self.text[-6],True,self.colour),(300,740))
        self.window.blit(self.smolFont.render(self.text[-3]+self.text[-4],True,self.colour),(300,770))
        self.window.blit(self.smolFont.render(self.text[-1]+self.text[-2],True,self.colour),(300,800))

        #render attacks
        for attack in self.attackToRender:
            pygame.draw.line(self.window,(0,0,255),attack[0],attack[1],5)

        self.attackToRender = []


        #mouse position
        self.mousePos = pygame.mouse.get_pos()
        #if mouse is hovering over an entity
        for entity in self.entities:
            if entity.tile.x < self.mousePos[0] < entity.tile.x1 and entity.tile.y < self.mousePos[1] < entity.tile.y1:
                #mark that entity as selected
                self.selectedEntity = entity

        #select an player to control
        if self.selectedPlayer == None:
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if self.selectedEntity != None:
                    if event.type == pygame.MOUSEBUTTONDOWN and self.selectedEntity.entityType == "player":
                        #if RMB pressed
                        if event.button == 3:
                            #select player
                            self.selectedPlayer = self.selectedEntity

                #exit pygame
                if event.type == pygame.QUIT: 
                    pygame.quit()

                #show tips
                elif pressed[pygame.K_ESCAPE]:
                    Menus.mainMenu(self.window)
            

        #presume no enchantment info will be shown
        self.enchantInfo = None
        #show its stats
        if self.selectedEntity != None:
            self.selectedEntity.showStats()

        if self.enchantInfo != None:
            lineNum = 0
            pygame.draw.rect(self.window,(0,0,0),[240,390,800,90])
            for line in self.enchantInfo:
                self.window.blit(self.font.render(line,True,(255,255,255)),(250,400+lineNum*40))
                lineNum +=1
            

            

    def worldTurn(self):
        self.window.blit(self.endTurnText,(300,250))
        pygame.display.flip()
        #wait 1 second
        #TODO: replace this wait with an animation
        pygame.time.wait(1000)
        self.endTurn = False

        
        ##this is run again to ensure enemies dont get any cheeky hits after they should've died
        for entity in self.entities:
            if entity.health <= 0:
                self.deadEntities.append(entity)

        for entity in self.deadEntities:
            #delete all dead entites from list of entities and trigger death effects
            entity.lastWords()
            self.entities.remove(entity)
        self.deadEntities = []

        end = True
        for entity in self.entities:
            #now += to take into account negative speed from enchantments
            entity.speed += entity.maxSpeed
            #end turn effects were being called every frame
            entity.endTurnActions = 1
            entity.startTurnActions = 1
            entity.endTurn = False
            if entity.entityType == "player":
                end = False
            #TODO: decrease stack of effects by 1

        #if all players dead, end the game
        if end == True:
            pygame.quit()
            sys.exit()
            
    
        


    #takes these things as input, returns a level
    def levelGen(self,window,tileSize,spritePath,wallChance):

        tiles = []

        #tiles have to be appended a row at a time to prevent errors
        tileLine = []

        for rowNum in range(11):
            for tileNum in range(11):
                tileLine.append(Tile(300 + tileNum*tileSize,rowNum*tileSize,spritePath,tileSize))

            #append tiles to row
            tiles.append(tileLine)
            #reset line, ready for new line to be appended
            tileLine = []


        ##############################
        ##find tile neighbours
        
        rowNum = 0
        tileNum = 0
        for row in tiles:
            for tile in row:
                #try...except... used to prevent crashes
                #if else statements used bc of cyclical nature of arrays when reversing
                if tileNum == 0:
                    tile.left = None
                else:
                     try: tile.left = row[tileNum - 1]
                     except: tile.left = None

                try: tile.right = row[tileNum + 1]
                except: tile.right = None

                if rowNum == 0:
                    tile.up = None
                else:
                    try: tile.up = tiles[rowNum - 1][tileNum]
                    except: tile.up = None

                try: tile.down = tiles[rowNum + 1][tileNum]
                except: tile.down = None

                if rowNum == 0 or tileNum == 0:
                    tile.upLeft = None
                else:
                    try: tile.upLeft = tiles[rowNum - 1][tileNum - 1]
                    except: tile.upLeft = None
                    
                if tileNum == 0:
                    tile.downLeft = None
                else:
                    try: tile.downLeft = tiles[rowNum + 1][tileNum - 1]
                    except: tile.downLeft = None

                if rowNum == 0:
                    tile.upRight = None
                else:
                    try: tile.upRight = tiles[rowNum - 1][tileNum + 1]
                    except: tile.upRight = None

                try: tile.downRight = tiles[rowNum + 1][tileNum + 1]
                except: tile.downRight = None

                #add tiles to adjTiles. will be useful for recursion stuff
                #this code is fine
                tile.adjTiles = [tile.left,tile.right,tile.up,tile.down,tile.upLeft,tile.downLeft,tile.upRight,tile.downRight]
                #print(tile.adjTiles)
                
                #generate walls while youre at it
                #chance of wall depends on environment
                if random.random() < wallChance and tile.occupant == None:
                    tile.occupant = Entity.Wall(window,self,tiles[rowNum][tileNum],None,None,None,Armoury.bricks,None,None,"Wall","wall",1,spritePath = self.spritePath+"wall.png")               
                        
                tileNum += 1
            rowNum += 1
            tileNum = 0

        

        return tiles

        
               
            
