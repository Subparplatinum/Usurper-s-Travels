import pygame
import sys
import random
import Debug
from HelperFunctions import *

def inventory(items,players,window,level):
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
    if level.levelNum%5 == 0:
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
    if level.levelNum == Debug.lastLevelNum:
        text = ["The World Unfurls"]
        
    #if level just before final boss
    elif level.levelNum == Debug.lastLevelNum - 1:
        text = ["big boss coming"]
        
    #if level just before regular boss
    elif (level.levelNum+1)%5 == 0:
        text = ["boss coming"]

    #if level just after regular boss
    elif (level.levelNum%5) == 0:
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
        window.blit(font.render("Level: "+str(level.levelNum + 1),True,colour),(0,100))

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
        window.blit(font.render("ENTER - Travel on",True,colour),(50,750))
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