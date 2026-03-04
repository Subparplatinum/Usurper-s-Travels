import pygame
import Armoury
import Entity
import Spellbook
import sys
import Tables
import random
#easy access variables
import Debug
from HelperFunctions import *

font = pygame.font.SysFont(None,40)
smolFont = pygame.font.SysFont(None,20)
bigFont = pygame.font.SysFont(None,160)
colour = (255,255,255)
red = (100,0,0)
grey = (100,100,100)

def selectBoss(window):
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

        window.blit(font.render("Determine the your next destination:",True,colour),(350,50))


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
                                
def controlMenu(window):

    finished = False
    textToRender = ["Right click on a green character to select them.",
                    "Left click on a tile to move there.",
                    "Hover over an entity to show information about them.",
                    "Left click on an enemy in weapon range to attack them.",
                    "Weapon ranges are shown by grey boxes when an entity is hovered over.",
                    "Press ENTER to skip a character's turn.",
                    "Sacrifice items to increase the multiplier for your character's stats.",
                    "Press the number shown above abilities to trigger that ability.",
                    "Press S while hovering over an entity to only look at that entity's stats.",
                    "Press S again while not hovering over an entity to look at other entities' stats.",
                    "Press ESC to access this menu while playing a level.",
                    "Press ESC to exit this menu."]

    #while menu hasnt been exited
    while not(finished):
        pygame.display.flip()
        window.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()

        for line in textToRender:
            window.blit(font.render(line,True,colour),(0,100+50*textToRender.index(line)))

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

    #DO NOT ADD "TBA" HERE
    textToRender = [""]
    enchantment = None

    #play opening cutscene when game first starts
    openingCutscene(window,font,colour)

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

            #Debug Class
            if Debug.debugClassEnabled:
                pygame.draw.rect(window,(100,100,100),[190,440,300,40])
                if 190 < mousePos[0] < 490 and 440 < mousePos[1] < 480:
                    textToRender = ["You are Derius Bugg, Lord of a Functional and","Balanced Game."]
                    pygame.draw.rect(window,red,[190,440,300,40])
                window.blit(font.render("Derius Bugg",True,colour),(200,450))

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

                    if Debug.debugClassEnabled:
                        if 190 < mousePos[0] < 490 and 440 < mousePos[1] < 480:
                            player = [Armoury.smoughHammer,None,Armoury.potHelm,Armoury.breastplate,Armoury.legplate,Armoury.metalBoots]
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

        #Crystal Golem
        pygame.draw.rect(window,(100,100,100),[190,190,300,40])
        if 190 < mousePos[0] < 490 and 190 < mousePos[1] < 240:
            textToRender = ["A marble golem overgrown with glowing blue crystals.",
                            "These crystals are fragments of the star-god Astra,",
                            "know as the Broken Star - who shattered herself to",
                            "bring magic to the world.",""]
            pygame.draw.rect(window,red,[190,190,300,40])
        window.blit(font.render("Crystalised Golem",True,colour),(200,200))
            

        #Valiant Golem        
        pygame.draw.rect(window,(100,100,100),[190,240,300,40])
        if 190 < mousePos[0] < 490 and 240 < mousePos[1] < 290:
            textToRender = ["An iron golem impaled by a lance-shaped meteorite",
                            "sent by the star-god Dareon, known as the",
                            "Shining Knight. It has sworn an oath to purge",
                            "Asterant of all evils, and in its past travels has",
                            "somehow befriended a horse.",""]
            pygame.draw.rect(window,red,[190,240,300,40])
        window.blit(font.render("Valiant Golem",True,colour),(200,250))

        #Burning Golem       
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



def startOfGame(window):
    window.fill((0,0,0))
    #fade out music over a second
    pygame.mixer.music.fadeout(1000)
    #play battle music
    pygame.mixer.music.load('music/battle'+str(random.randint(1,4))+'.mp3')
    #fade music in over 1 second
    pygame.mixer.music.play(-1,0,1000)


def openingCutscene(window,font,colour):

    openingLore = []
    loreFile = open("lore/opening.txt","r")
    for line in loreFile:
        openingLore.append(line.strip())
    loreFile.close()

    openingLore.append("")
    openingLore.append("-Press ENTER to continue-")                                                                                                                                                                                                         
        
    finished = False
    while finished == False:
        window.fill((0,0,0))
        #draw text
        drawText(window,font,colour,openingLore,0,0,40)
            
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

def startMenu(window):

    #play menu music
    # Fade it in if music is already playing, otherwise just start it
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load("music/Usurper's Travels.mp3")
    pygame.mixer.music.play(-1,0,0)

    menu = 0

    def changeMenu(value):
        nonlocal menu
        menu = value


    playButton = Button(500,500,200,50,"Play",grey,red,font, lambda: changeMenu(1))
    controlsButton = Button(500,600,200,50,"Controls",grey,red,font, lambda: changeMenu(2))


    # While play hasnt been pressed, stay in menu
    while menu != 1:
        pygame.display.flip()
        window.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()


        if menu == 0:
            window.blit(bigFont.render("Usurper's Travels",True,red),(100,50))

            # Draw Play button
            playButton.draw(mousePos,window)
        
            # Draw Controls button
            controlsButton.draw(mousePos,window)

        # If Controls button pressed:
        if menu == 2:
            controlMenu(window)
            menu = 0

        #let player exit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()