import pygame
import Armoury
import Entity
import Spellbook
import sys
import Tables
import random
#easy access variables
import Debug


#openingLore = ["The land of Asterant has been thrown into chaos. Its king, Raah, murdered a star -",
#                        "one of the gods of Asterant. To kill a star is a cardinal sin, for without their guiding light",
#                        "keeping the Darkness at bay, the people of Asterant will inevitably be consumed. Thus,",
#                        "the Zodiacs of the Pale City",
#                        "declared him the Archenemy, and all across Asterant Usurpers rose up to take his throne.",
#                        "Followers of Khorgan, the Bloody Star - a violent god that grants strength through sacrifice",
#                        " - and assisted by divine golems created by the Zodiacs, they travel Asterant, growing in",
#                        "strength, until they are ready to take the throne.","",
#                        "-Press ENTER to continue-"]

openingLore = []
loreFile = open("lore/opening.txt","r")
for line in loreFile:
    openingLore.append(line.strip())
loreFile.close()

openingLore.append("")
openingLore.append("-Press ENTER to continue-")

def selectBoss(window):

    font = pygame.font.SysFont(None,40)
    smolFont = pygame.font.SysFont(None,20)
    colour = (255,255,255)
    red = (100,0,0)
    grey = (100,100,100)

    bosses = random.sample(Tables.bossTables, 3)

    finished = False
    #while menu hasnt been exited
    while True:
        pygame.display.flip()
        window.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()

        #big buttons
        pygame.draw.rect(window,grey,[25,100,340,800])
        pygame.draw.rect(window,grey,[375,100,340,800])
        pygame.draw.rect(window,grey,[725,100,340,800])

        #render different colours if hovering over buttons
        if 100 < mousePos[1]:
            if 25 < mousePos[0] < 375:
                pygame.draw.rect(window,red,[25,100,340,800])
            elif 375 < mousePos[0] < 725:
                pygame.draw.rect(window,red,[375,100,340,800])
            elif 725 < mousePos[0] < 1065:
                pygame.draw.rect(window,red,[725,100,340,800])
        
        #text
        window.blit(font.render(bosses[0][3],True,colour),(35,440))
        window.blit(font.render(bosses[1][3],True,colour),(385,440))
        window.blit(font.render(bosses[2][3],True,colour),(735,440))

        window.blit(font.render("Determine the rift's destination:",True,colour),(350,50))


        #if player presses esc, exit menu
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 < mousePos[1]:
                    if 25 < mousePos[0] < 375:
                        return bosses[0]
                    elif 375 < mousePos[0] < 725:
                        return bosses[1]
                    elif 725 < mousePos[0] < 1065:
                        return bosses[2]
                    
            elif event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
                    

#TODO: create class for inventory menu
def inventory(items,players,window,levelNum):
    finished = False
    #used to move items around
    selectedItem = None

    try: player1 = players[0]
    except: player1 = None
    
    try: player2 = players[1]
    except: player2 = None
    
    font = pygame.font.SysFont(None,40)
    smolFont = pygame.font.SysFont(None,20)
    bigFont = pygame.font.SysFont(None,300)
    colour = (255,255,255)
    grey = (100,100,100)
    red = (100,0,0)
    
    #if boss level has just concluded,
    if levelNum%5 == 0:
        #fade out music over a second
        pygame.mixer.music.fadeout(1000)
        pygame.mixer.music.load('music/battle'+str(random.randint(1,4))+'.mp3')
        #fade music in over 1 second
        pygame.mixer.music.play(-1,0,1000)

    #where the columns will be located
    weaponPos = 0
    helmetPos = 200
    breastplatePos = 400
    leggingsPos = 600
    bootsPos = 800

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
        

                                         
    for equipment in items:
        sort(equipment)


    def showStats(equipment,font,colour,startPos,window,mousePos):
        window.blit(font.render(equipment.name,True,colour),(900,startPos))
        window.blit(font.render("HP: "+str(round(equipment.healthBonus*player1.mult)),True,colour),(900,startPos + 30))
        window.blit(font.render("AP: "+str(round(equipment.armourBonus*player1.mult)),True,colour),(900,startPos + 60))
        window.blit(font.render("SP: "+str(equipment.speedBonus),True,colour),(900,startPos + 90))
        window.blit(font.render("MP: "+str(round(equipment.manaBonus*player1.mult)),True,colour),(900,startPos + 120))
        window.blit(font.render("AT: "+str(round(equipment.attackBonus*player1.mult)),True,colour),(900,startPos + 150))
        if equipment.equipType == "weapon":
            if equipment.twoHanded == True:
                window.blit(font.render("Two-Handed",True,colour),(900,startPos + 180))
            else:
                window.blit(font.render("One-Handed",True,colour),(900,startPos + 180))

        #render enchantment
            if equipment.enchantment != None:
                pygame.draw.rect(window,grey,[900,startPos + 210,300,30])
                window.blit(font.render(equipment.enchantment.name,True,(0,255,255)),(900,startPos + 210))
                if 900 < mousePos[0] < 1100 and (startPos + 210) < mousePos[1] < (startPos + 240):
                    pygame.draw.rect(window,red,[900,startPos + 210,300,30])
                    window.blit(font.render(equipment.enchantment.name,True,(0,255,255)),(900,startPos + 210))
                    return equipment.enchantment
                
        else:
            
            if equipment.enchantment != None:
                pygame.draw.rect(window,grey,[900,startPos + 180,300,30])
                window.blit(font.render(equipment.enchantment.name,True,(0,255,255)),(900,startPos + 180))
                if 900 < mousePos[0] < 1100 and (startPos + 180) < mousePos[1] < (startPos + 210):
                    pygame.draw.rect(window,red,[900,startPos + 180,300,30])
                    window.blit(font.render(equipment.enchantment.name,True,(0,255,255)),(900,startPos + 180))
                    return equipment.enchantment

    #render win screen
    window.fill((0,0,0))
    
    #if final boss beaten then end the game
    if levelNum == Debug.lastLevelNum:
        pygame.quit()
        sys.exit()
        
    #if level just before final boss
    if levelNum == 19:
        text = ["big boss coming"]
        
    #if level just before regular boss
    elif (levelNum+1)%5 == 0:
        text = ["boss coming"]

    #if level just after regular boss
    elif (levelNum%5) == 0:
        text = ["boss beat"]
        
    #if normal level
    else:
        text = ["normal level"]

    text.append("-Press ENTER to continue-")
    while not(finished):
        window.fill((0,0,0))
        drawText(window,font,colour,text,50,100,100)
        pygame.display.flip()

        #let player move on when they want
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RETURN]:
                #player is ready to move on
                finished = True
            
            elif event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

    finished = False
    hoveredItem = None
    while not(finished):
        enchantInfo = None
        pygame.display.flip()
        window.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()

        #player 1 equipment
        if player1 != None:
            window.blit(font.render(player1.name,True,colour),(300,0))
            for i in range(len(player1.equipment)):
                if player1.equipment[i] != None:
                    pygame.draw.rect(window,grey,[290,40+(i*50),295,45])
                    #if hovering over equipment:
                    if 290 < mousePos[0] < 585 and 40+(i*50) < mousePos[1] < 85+(i*50):
                        #show stats
                        pygame.draw.rect(window,red,[290,40+(i*50),295,45])
                        hoveredItem = player1.equipment[i]
                    window.blit(font.render(player1.equipment[i].name,True,colour),(300,50+(i*50)))
            
        #player 2 equipment
        if player2 != None:
            window.blit(font.render(player2.name,True,colour),(600,0))
            for i in range(len(player2.equipment)):
                if player2.equipment[i] != None:
                    pygame.draw.rect(window,grey,[590,40+(i*50),295,45])
                    #if hovering over equipment:
                    if 590 < mousePos[0] < 885 and 40+(i*50) < mousePos[1] < 85+(i*50):
                        #show stats
                        pygame.draw.rect(window,red,[590,40+(i*50),295,45])
                        hoveredItem = player2.equipment[i]
                    window.blit(font.render(player2.equipment[i].name,True,colour),(600,50+(i*50)))

        #unused equipment

        #titles
        window.blit(font.render("Weapons",True,colour),(weaponPos,450))
        window.blit(font.render("Helmets",True,colour),(helmetPos,450))
        window.blit(font.render("Breasplates",True,colour),(breastplatePos,450))
        window.blit(font.render("Leggings",True,colour),(leggingsPos,450))
        window.blit(font.render("Boots",True,colour),(bootsPos,450))

        #level number
        window.blit(font.render("Level: "+str(levelNum + 1),True,colour),(0,100))

        #mult num
        window.blit(font.render("Sacrifice: "+str(round((player1.mult-1)*100))+"%",True,colour),(0,150))

        #actual equipment
        for i in range(len(weapons)):
            pygame.draw.rect(window,grey,[weaponPos - 5,497+(i*20),197,17])
            #if hovering over equipment
            if weaponPos - 5 < mousePos[0] < weaponPos + 192  and 497+(i*20) < mousePos[1] < 514+(i*20):
                pygame.draw.rect(window,red,[weaponPos - 5,497+(i*20),197,17])
                #show stats
                hoveredItem = weapons[i]
            window.blit(smolFont.render(weapons[i].name,True,colour),(weaponPos,500 + (i*20)))
                
        for i in range(len(helmets)):
            pygame.draw.rect(window,grey,[helmetPos - 5,497+(i*20),197,17])
            #if hovering over equipment
            if helmetPos - 5 < mousePos[0] < helmetPos + 192  and 497+(i*20) < mousePos[1] < 514+(i*20):
                pygame.draw.rect(window,red,[helmetPos - 5,497+(i*20),197,17])
                #show stats
                hoveredItem = helmets[i]
            window.blit(smolFont.render(helmets[i].name,True,colour),(helmetPos,500 + (i*20)))
                
        for i in range(len(breastplates)):
            pygame.draw.rect(window,grey,[breastplatePos - 5,497+(i*20),197,17])
            #if hovering over equipment
            if breastplatePos - 5 < mousePos[0] < breastplatePos + 192  and 497+(i*20) < mousePos[1] < 514+(i*20):
                pygame.draw.rect(window,red,[breastplatePos - 5,497+(i*20),197,17])
                #show stats
                hoveredItem = breastplates[i]
            window.blit(smolFont.render(breastplates[i].name,True,colour),(breastplatePos,500 + (i*20)))
                
        for i in range(len(leggings)):
            pygame.draw.rect(window,grey,[leggingsPos - 5,497+(i*20),197,17])
            #if hovering over equipment
            if leggingsPos - 5 < mousePos[0] < leggingsPos + 192  and 497+(i*20) < mousePos[1] < 514+(i*20):
                pygame.draw.rect(window,red,[leggingsPos - 5,497+(i*20),197,17])
                #show stats
                hoveredItem = leggings[i]
            window.blit(smolFont.render(leggings[i].name,True,colour),(leggingsPos,500 + (i*20)))
                
        for i in range(len(boots)):
            pygame.draw.rect(window,grey,[bootsPos - 5,497+(i*20),197,17])
            #if hovering over equipment
            if bootsPos - 5 < mousePos[0] < bootsPos + 192  and 497+(i*20) < mousePos[1] < 514+(i*20):
                pygame.draw.rect(window,red,[bootsPos - 5,497+(i*20),197,17])
                #show stats
                hoveredItem = boots[i]
            window.blit(smolFont.render(boots[i].name,True,colour),(bootsPos,500 + (i*20)))
                

            
        #if enter key pressed:
        window.blit(font.render("ENTER - brave the rift",True,colour),(50,750))
        window.blit(font.render("RMB - sacrifice an item",True,colour),(550,750))
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_RETURN]:
                #player is ready to move on
                finished = True
                window.fill((0,0,0))

            if event.type == pygame.MOUSEBUTTONDOWN:
                #if LMB pressed
                if event.button == 1:
                    #distinguish between items

                    #only update itemPos if player is selecting items from their inventory, not already equipped items
                    if mousePos[1] > 497:
                        itemPos = (mousePos[1]-497)//20
                        #print(itemPos)
                        if weaponPos < mousePos[0] < helmetPos:
                            try: selectedItem = weapons[itemPos]
                            except: selectedItem = None
                            itemList = weapons
                            #print(selectedItem)

                        elif helmetPos < mousePos[0] < breastplatePos:
                            try: selectedItem = helmets[itemPos]
                            except: selectedItem = None
                            itemList = helmets
                            #print(selectedItem)
                            
                        elif breastplatePos < mousePos[0] < leggingsPos:
                            try: selectedItem = breastplates[itemPos]
                            except: selectedItem = None
                            itemList = breastplates
                            #print(selectedItem.name)

                        elif leggingsPos < mousePos[0] < bootsPos:
                            try: selectedItem = leggings[itemPos]
                            except: selectedItem = None
                            itemList = leggings
                            #print(selectedItem)
                            
                        elif bootsPos < mousePos[0]:
                            try: selectedItem = boots[itemPos]
                            except: selectedItem = None
                            itemList = boots
                            #print(selectedItem)

                    #TODO: render stats of equipment being hovered over AND equipment selected
                        

                    #if clicked again on item in player inventory, swap the items
                    player = None
                    if 290 <= mousePos[0] <= 585:
                        player = player1
                    elif 590 <= mousePos[0] <= 885:
                        player = player2
                                        
                    if player != None:
                        for i in range(len(player.equipment)):
                            #if equipment clicked
                            if 40+(i*50) < mousePos[1] < 85+(i*50):
                                
                                #unequip equipment
                                #WORKS
                                sort(player.equipment[i])
                                items.append(player.equipment[i])
                                player.equipment[i] = None

                                #if replacement equipment is selected
                                if selectedItem != None:

                                    #prevent player from dual wielding if weapon cannot be dual wielded?
                                    prevent = False
                                    if selectedItem in weapons:
                                        for j in range(2):
                                            if player.equipment[j] != None:
                                                if player.equipment[j].twoHanded == True or selectedItem.twoHanded == True:
                                                    prevent = True
                                    
                                    if (i == 0 or i == 1) and selectedItem.equipType == "weapon":
                                        #if player can equip the weapon, let them equip it
                                        if prevent != True:
                                            player.equipment[i] = selectedItem
                                            itemList.remove(selectedItem)
                                            items.remove(selectedItem)
                                            selectedItem = None

                                    if (i == 2) and selectedItem.equipType == "helmet":
                                        player.equipment[i] = selectedItem
                                        itemList.remove(selectedItem)
                                        items.remove(selectedItem)
                                        selectedItem = None

                                    if (i == 3) and selectedItem.equipType == "breastplate":
                                        player.equipment[i] = selectedItem
                                        itemList.remove(selectedItem)
                                        items.remove(selectedItem)
                                        selectedItem = None
                                        
                                    if (i == 4) and selectedItem.equipType == "leggings":
                                        player.equipment[i] = selectedItem
                                        itemList.remove(selectedItem)
                                        items.remove(selectedItem)
                                        selectedItem = None

                                    if (i == 5) and selectedItem.equipType == "boots":
                                        player.equipment[i] = selectedItem
                                        itemList.remove(selectedItem)
                                        items.remove(selectedItem)
                                        selectedItem = None

                #if RMB pressed
                elif event.button == 3:

                    #MAKE THIS MORE EFFICIENT
                    if mousePos[1] > 497:
                        itemPos = (mousePos[1]-497)//20
                        #print(itemPos)
                        itemRemoved = False
                        if weaponPos < mousePos[0] < helmetPos:
                            try: selectedItem = weapons[itemPos]
                            except: selectedItem = None

                            if selectedItem != None:
                                weapons.remove(selectedItem)
                                items.remove(selectedItem)
                                itemRemoved = True
                                selectedItem = None

                        elif helmetPos < mousePos[0] < breastplatePos:
                            try: selectedItem = helmets[itemPos]
                            except: selectedItem = None
                            
                            if selectedItem != None:
                                helmets.remove(selectedItem)
                                items.remove(selectedItem)
                                itemRemoved = True
                                selectedItem = None
                            
                        elif breastplatePos < mousePos[0] < leggingsPos:
                            try: selectedItem = breastplates[itemPos]
                            except: selectedItem = None
                            
                            if selectedItem != None:
                                breastplates.remove(selectedItem)
                                items.remove(selectedItem)
                                itemRemoved = True
                                selectedItem = None

                        elif leggingsPos < mousePos[0] < bootsPos:
                            try: selectedItem = leggings[itemPos]
                            except: selectedItem = None
                            
                            if selectedItem != None:
                                leggings.remove(selectedItem)
                                items.remove(selectedItem)
                                itemRemoved = True
                                selectedItem = None
                            
                        elif bootsPos < mousePos[0]:
                            try: selectedItem = boots[itemPos]
                            except: selectedItem = None
                            
                            if selectedItem != None:
                                boots.remove(selectedItem)
                                items.remove(selectedItem)
                                itemRemoved = True
                                selectedItem = None

                        if itemRemoved == True:
                            player1.mult = round(player1.mult + Debug.playerMultBonus,2) #player mult
                            if player2 != None:
                                player2.mult = round(player2.mult + Debug.playerMultBonus,2) #player mult

                elif event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()

        #render text and button at mouse position
        if selectedItem != None:
            pygame.draw.rect(window,red,[mousePos[0],mousePos[1],197,17])
            window.blit(smolFont.render(selectedItem.name,True,colour),(mousePos[0],mousePos[1]))
            #show selected item stats
            enchantInfo = showStats(selectedItem,font,colour,0,window,mousePos)

        #render information of last item hovered over
        if hoveredItem != None:
            if enchantInfo == None:
                enchantInfo = showStats(hoveredItem,font,colour,270,window,mousePos)
            else:
                showStats(hoveredItem,font,colour,270,window,mousePos)
                
        if enchantInfo != None:
            lineNum = 0
            #render all lines of info
            pygame.draw.rect(window,(255,0,0),[250,400,800,100])
            
            values = []
            #add all magnitudes to list for formatting
            for magnitude in enchantInfo.magnitude:
                values.append(str(round(abs(magnitude))))
                    
            lineNum = 0
            for line in enchantInfo.desc:
                window.blit(pygame.font.SysFont(None,30).render(line.format(*values),True,(255,255,255)),(250,400+lineNum*40))
                lineNum +=1
                
                
    window.fill((0,0,0))
    pygame.display.flip()
                                
def mainMenu(window):
    font = pygame.font.SysFont(None,40)
    smolFont = pygame.font.SysFont(None,20)
    colour = (255,255,255)

    finished = False
    #while menu hasnt been exited
    while not(finished):
        pygame.display.flip()
        window.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()

        window.blit(font.render("Right click on a green character to select them.",True,colour),(0,100))
        window.blit(font.render("Left click on a tile to move there.",True,colour),(0,150))
        window.blit(font.render("Hover over an entity to show information about them.",True,colour),(0,200))
        window.blit(font.render("Left click on an enemy in weapon range to attack them.",True,colour),(0,250))
        window.blit(font.render("Weapon ranges are shown by grey boxes when an entity is hovered over.",True,colour),(0,300))
        window.blit(font.render("Press ENTER to skip a character's turn.",True,colour),(0,350))
        window.blit(font.render("Sacrifice items to increase the multiplier for your character's stats.",True,colour),(0,400))
        window.blit(font.render("Press the number shown above abilities to trigger that ability",True,colour),(0,450))

        #if player presses esc, exit menu
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                #player is ready to move on
                finished = True
                window.fill((0,0,0))
            
            elif event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

def characterMenu(window,level,ycoord,xcoord):
    font = pygame.font.SysFont(None,40)
    smolFont = pygame.font.SysFont(None,20)
    colour = (255,255,255)
    red = (100,0,0)
    grey = (100,100,100)

    #DO NOT ADD "TBA" HERE
    textToRender = [""]
    enchantment = None
    
    #play menu music
    pygame.mixer.music.load("music/Usurper's Travels.mp3")
    pygame.mixer.music.play(-1,0,0)

    #play opening cutscene when game first starts
    openingCutscene(window,font,colour,openingLore)

    menu = 1

    def renderEnchant(enchantment,startPos):
        if enchantment != None:
            #length of button now dynamic
            pygame.draw.rect(window,grey,[700,startPos,10 + len(enchantment.name)*15,30])
            window.blit(font.render(enchantment.name,True,(0,255,255)),(700,startPos))
            #if hovering over enchantment
            if 700 < mousePos[0] < 900 and startPos < mousePos[1] < (startPos + 30):
                pygame.draw.rect(window,red,[700,startPos,10 + len(enchantment.name)*15,30])
                window.blit(font.render(enchantment.name,True,(0,255,255)),(700,startPos))
                pygame.draw.rect(window,(255,0,0),[250,400,800,100])

                values = []
                #add all magnitudes to list for formatting
                for magnitude in enchantment.magnitude:
                    values.append(str(round(abs(magnitude))))
                    
                lineNum = 0
                for line in enchantment.desc:
                    window.blit(pygame.font.SysFont(None,30).render(line.format(*values),True,(255,255,255)),(250,400+lineNum*40))
                    lineNum +=1
        
    #while menu hasnt been exited
    while True:
        pygame.display.flip()
        window.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()

        if menu == 1:
            
            window.blit(font.render("Choose your background:",True,colour),(200,100))

            #Swordsman
            pygame.draw.rect(window,(100,100,100),[190,190,300,40])
            if 190 < mousePos[0] < 490 and 190 < mousePos[1] < 240:
                textToRender = ["You are proficient in the art of the sword."]
                pygame.draw.rect(window,red,[190,190,300,40])
            window.blit(font.render("Swordsman",True,colour),(200,200))

            #Archer       
            pygame.draw.rect(window,(100,100,100),[190,240,300,40])
            if 190 < mousePos[0] < 490 and 240 < mousePos[1] < 290:
                textToRender = ["You are proficient in the art of the bow."]
                pygame.draw.rect(window,red,[190,240,300,40])
            window.blit(font.render("Archer",True,colour),(200,250))

            #Rogue        
            pygame.draw.rect(window,(100,100,100),[190,290,300,40])
            if 190 < mousePos[0] < 490 and 290 < mousePos[1] < 340:
                textToRender = ["You are proficient in the art of the thrown blade."]
                pygame.draw.rect(window,red,[190,290,300,40])
            window.blit(font.render("Rogue",True,colour),(200,300))

            #Mage       
            pygame.draw.rect(window,(100,100,100),[190,340,300,40])
            if 190 < mousePos[0] < 490 and 340 < mousePos[1] < 390:
                textToRender = ["You are proficient in celestial magics."]
                pygame.draw.rect(window,red,[190,340,300,40])
            window.blit(font.render("Mage",True,colour),(200,350))

            #Priest
            pygame.draw.rect(window,(100,100,100),[190,390,300,40])
            if 190 < mousePos[0] < 490 and 390 < mousePos[1] < 440:
                textToRender = ["You are proficient in the arts of divine healing."]
                pygame.draw.rect(window,red,[190,390,300,40])
            window.blit(font.render("Priest",True,colour),(200,400))

            #render descriptions
            lineNum = 0
            for line in textToRender:
                window.blit(font.render(line,True,colour),(500,200+40*lineNum))
                lineNum += 1
                
            

            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Swordsman
                    if 190 < mousePos[0] < 490 and 190 < mousePos[1] < 230:
                        player = [Armoury.greatsword,None,Armoury.potHelm,Armoury.breastplate,Armoury.legplate,Armoury.metalBoots]
                        menu = 2
                        
                    #Archer
                    if 190 < mousePos[0] < 490 and 240 < mousePos[1] < 280:
                        player = [Armoury.bow,None,Armoury.potHelm,Armoury.breastplate,Armoury.breeches,Armoury.metalBoots]
                        menu = 2
                        
                    #Rogue
                    if 190 < mousePos[0] < 490 and 290 < mousePos[1] < 330:
                        player = [Armoury.throwingKnife,Armoury.throwingKnife,None,Armoury.tunic,Armoury.breeches,Armoury.boots]
                        menu = 2

                    #Mage
                    if 190 < mousePos[0] < 490 and 340 < mousePos[1] < 380:
                        player = [Armoury.starStaff,None,None,Armoury.mageCloak,Armoury.mageRobe,Armoury.mageBoots]
                        menu = 2

                    #Priest
                    if 190 < mousePos[0] < 490 and 390 < mousePos[1] < 430:
                        player = [Armoury.holyStaff,Armoury.longsword,None,Armoury.mageCloak,Armoury.mageRobe,Armoury.mageBoots]
                        menu = 2

                elif event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()

        elif menu == 2:
            
            window.blit(font.render("Choose your race:",True,colour),(200,100))

            #Human
            pygame.draw.rect(window,(100,100,100),[190,190,300,40])
            if 190 < mousePos[0] < 490 and 190 < mousePos[1] < 240:
                textToRender = ["TBA"]
                pygame.draw.rect(window,red,[190,190,300,40])
                enchantment = Spellbook.lessRegen
            window.blit(font.render("Human",True,colour),(200,200))

            #Elf      
            pygame.draw.rect(window,(100,100,100),[190,240,300,40])
            if 190 < mousePos[0] < 490 and 240 < mousePos[1] < 290:
                textToRender = ["TBA"]
                pygame.draw.rect(window,red,[190,240,300,40])
                enchantment = Spellbook.attune
            window.blit(font.render("Elf",True,colour),(200,250))
                
            #Dwarf     
            pygame.draw.rect(window,(100,100,100),[190,290,300,40])
            if 190 < mousePos[0] < 490 and 290 < mousePos[1] < 340:
                textToRender = ["TBA"]
                pygame.draw.rect(window,red,[190,290,300,40])
                enchantment = Spellbook.stalwart
            window.blit(font.render("Dwarf",True,colour),(200,300))

            #Lizardkin      
            pygame.draw.rect(window,(100,100,100),[190,340,300,40])
            if 190 < mousePos[0] < 490 and 340 < mousePos[1] < 390:
                textToRender = ["TBA"]
                
                pygame.draw.rect(window,red,[190,340,300,40])
                enchantment = Spellbook.poisonous
            window.blit(font.render("Lizardkin",True,colour),(200,350))

            #Harpy     
            pygame.draw.rect(window,(100,100,100),[190,390,300,40])
            if 190 < mousePos[0] < 490 and 390 < mousePos[1] < 440:
                textToRender = ["TBA"]
                pygame.draw.rect(window,red,[190,390,300,40])
                enchantment = Spellbook.quick
            window.blit(font.render("Harpy",True,colour),(200,400))

            #beastkin   
            pygame.draw.rect(window,(100,100,100),[190,440,300,40])
            if 190 < mousePos[0] < 490 and 440 < mousePos[1] < 480:
                textToRender = ["TBA"]
                pygame.draw.rect(window,red,[190,440,300,40])
                enchantment = Spellbook.bloodDrink
            window.blit(font.render("Beastkin",True,colour),(200,450))

            #ratkin
            pygame.draw.rect(window,(100,100,100),[190,490,300,40])
            if 190 < mousePos[0] < 490 and 490 < mousePos[1] < 540:
                textToRender = ["TBA"]
                pygame.draw.rect(window,red,[190,490,300,40])
                enchantment = Spellbook.filthBlessing
            window.blit(font.render("Ratkin",True,colour),(200,500))

            #wyvernkin 
            """
            pygame.draw.rect(window,(100,100,100),[190,490,300,40])
            if 190 < mousePos[0] < 490 and 490 < mousePos[1] < 540:
                textToRender = ["Like all creatures, they are distant descendents",
                                "of the primordial wyverns that first emerged from",
                                "Elyrax's ashen crucible. However, they have retained",
                                "more of their dragon-blood, making them master",
                                "shapeshifters."]
                pygame.draw.rect(window,red,[190,490,300,40])
                enchantment = Spellbook.dragonchild
            window.blit(font.render("Wyvernkin",True,colour),(200,500))
            """

            #back button
            pygame.draw.rect(window,(100,100,100),[190,740,300,40])
            if 190 < mousePos[0] < 490 and 740 < mousePos[1] < 780: 
                pygame.draw.rect(window,red,[190,740,300,40]) 
            window.blit(font.render("Back",True,colour),(200,750))

            #render descriptions
            lineNum = 0
            for line in textToRender:
                window.blit(font.render(line,True,colour),(500,200+40*lineNum))
                lineNum += 1
            renderEnchant(enchantment,200+40*lineNum)
                
            

            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Human
                    if 190 < mousePos[0] < 490 and 190 < mousePos[1] < 230:
                        player.append(Spellbook.lessRegen)
                        menu = 3
                        
                    #Elf
                    elif 190 < mousePos[0] < 490 and 240 < mousePos[1] < 280:
                        player.append(Spellbook.attune)
                        menu = 3
                        
                    #Dwarf
                    elif 190 < mousePos[0] < 490 and 290 < mousePos[1] < 330:
                        player.append(Spellbook.stalwart)
                        menu = 3

                    #lizardkin
                    elif 190 < mousePos[0] < 490 and 340 < mousePos[1] < 380:
                        player.append(Spellbook.poisonous)
                        menu = 3

                    #harpy
                    elif 190 < mousePos[0] < 490 and 390 < mousePos[1] < 430:
                        player.append(Spellbook.quick)
                        menu = 3

                    #beastkin
                    elif 190 < mousePos[0] < 490 and 440 < mousePos[1] < 480:
                        player.append(Spellbook.bloodDrink)
                        menu = 3

                    #ratkin
                    elif 190 < mousePos[0] < 490 and 490 < mousePos[1] < 540:
                        player.append(Spellbook.filthBlessing)
                        menu = 3
                  

                    #wyvernkin
                    """
                    if 190 < mousePos[0] < 490 and 490 < mousePos[1] < 540:
                        player.append(Spellbook.dragonchild)
                        menu = 3
                    """
                        
                    #back
                    if 190 < mousePos[0] < 490 and 740 < mousePos[1] < 780:
                        menu = 1

                elif event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()

        elif menu == 3:
            return Entity.Player(window,level,level.tiles[ycoord][xcoord],player[0],player[1],player[2],player[3],player[4],player[5],"The Usurper","player",1,player[6])

def companionMenu(window,level,ycoord,xcoord):
    font = pygame.font.SysFont(None,40)
    smolFont = pygame.font.SysFont(None,20)
    colour = (255,255,255)
    red = (100,0,0)
        
    
    #while menu hasnt been exited
    while True:
        pygame.display.flip()
        window.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()
        textToRender = [""]

            
        window.blit(font.render("Choose a golem companion:",True,colour),(200,100))

        #Skyla
        pygame.draw.rect(window,(100,100,100),[190,190,300,40])
        if 190 < mousePos[0] < 490 and 190 < mousePos[1] < 240:
            textToRender = ["A marble golem overgrown with glowing blue crystals.",
                            "These crystals are fragments of the star-god Astra,",
                            "know as the Broken Star - who shattered herself to",
                            "bring magic to the world.",""]
            pygame.draw.rect(window,red,[190,190,300,40])
        window.blit(font.render("Crystalised Golem",True,colour),(200,200))
            

        #Donkey         
        pygame.draw.rect(window,(100,100,100),[190,240,300,40])
        if 190 < mousePos[0] < 490 and 240 < mousePos[1] < 290:
            textToRender = ["An iron golem impaled by a lance-shaped meteorite",
                            "sent by the star-god Dareon, known as the",
                            "Shining Knight. It has sworn an oath to purge",
                            "Asterant of all evils, and in its past travels has",
                            "somehow befriended a horse.",""]
            pygame.draw.rect(window,red,[190,240,300,40])
        window.blit(font.render("Valiant Golem",True,colour),(200,250))

        #Heinrich         
        pygame.draw.rect(window,(100,100,100),[190,290,300,40])
        if 190 < mousePos[0] < 490 and 290 < mousePos[1] < 340:
            textToRender = ["A basalt golem which cracks and buckles as it",
                            "stuggles to contain the fires of the star-god Drakkak,",
                            "known as the Father of Wyverns - who yearns to set the",
                            "world aflame.",""]
            pygame.draw.rect(window,red,[190,290,300,40])
        window.blit(font.render("Burning Golem",True,colour),(200,300))

        #render descriptions
        drawText(window,font,colour,textToRender,500,200,40)

        #if player presses esc, exit menu
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                #Crystal Golem
                if 190 < mousePos[0] < 490 and 190 < mousePos[1] < 230:
                    startOfGame(window)
                    return Entity.Player(window,level,level.tiles[ycoord][xcoord],Armoury.greatsword,None,Armoury.potHelm,Armoury.breastplate,Armoury.legplate,Armoury.metalBoots,"Crystal Golem","player",1,Spellbook.wildMagic)
                #Valiant Golem
                if 190 < mousePos[0] < 490 and 240 < mousePos[1] < 280:
                    startOfGame(window)
                    return Entity.Player(window,level,level.tiles[ycoord][xcoord],Armoury.oatLance,None,None,Armoury.breastplate,Armoury.frenteguerra,Armoury.riderBoots,"Valiant Golem","player",1,Spellbook.charge)

                #Burning Golem
                if 190 < mousePos[0] < 490 and 290 < mousePos[1] < 330:
                    startOfGame(window)
                    return Entity.Player(window,level,level.tiles[ycoord][xcoord],Armoury.stonePillar,None,None,Armoury.mageCloak,Armoury.mageRobe,Armoury.mageBoots,"Burning Golem","player",1,Spellbook.wyvern)

            elif event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()

#render text
def drawText(window,font,colour,textToRender,startX,startY,space):
    lineNum = 0
    for line in textToRender:
        window.blit(font.render(line,True,colour),(startX,startY+space*lineNum))
        lineNum += 1



def startOfGame(window):
    window.fill((0,0,0))
    #fade out music over a second
    pygame.mixer.music.fadeout(1000)
    #play battle music
    pygame.mixer.music.load('music/battle'+str(random.randint(1,4))+'.mp3')
    #fade music in over 1 second
    pygame.mixer.music.play(-1,0,1000)


def openingCutscene(window,font,colour,textToRender):                                                                                                                                                                                                         
        
        finished = False
        while finished == False:
            window.fill((0,0,0))
            #draw text
            drawText(window,font,colour,textToRender,0,0,40)
            
            pygame.display.flip()
        
            
            #let player move on when they want
            for event in pygame.event.get():
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_RETURN]:
                    #player is ready to move on
                    finished = True

                elif event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()