import pygame
#initialise pygame
pygame.init()

import Armoury
import Entity
import Inventory
import Level
import Menus

#create a window
#level itself will be 900 x 900. 200 px on either side for UI
window = pygame.display.set_mode((1300,800))
pygame.display.set_caption("Usurper's Travels")
#create a clock
clock = pygame.time.Clock()


#store items collected by player
items = []

lastLevel = None

#Run Main menu
Menus.startMenu(window)

environment = Level.Level(window,lastLevel)

#game loop
while True:

    #get ready to generate the next level when level is marked as complete
    if environment.levelComplete:
        lastLevel = environment
        #allow the player to access their inventory
        Inventory.inventory(items,lastLevel.players,window,lastLevel)
        environment = Level.Level(window,lastLevel) 

    #update everything
    #when level ends items will be stored, so they need to be kept in here
    environment.update(items)

    if environment.gameOver:
        # Reset game
        Menus.startMenu(window)
        environment = Level.Level(window,None)
        items = []

    #refresh screen
    pygame.display.flip()
    window.fill((0,0,0))
    #game runs at 60fps
    clock.tick(60)
    
