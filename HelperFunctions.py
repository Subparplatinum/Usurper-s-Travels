import pygame
import os

allLore = {}

#iterate over all files in the lore folder and add them to a dictionary
def find_lore_recursive(path = "lore"):
    global allLore
    for filename in os.listdir(path):
        full_path = os.path.join(path,filename)
        # If file is actually folder, expand it
        if os.path.isdir(full_path):
            find_lore_recursive(full_path)

        #otherwise, if it is a text file, add to allLore
        elif filename.endswith(".txt"):
            with open(full_path, "r") as f:
                textLine = ""
                for line in f:
                    textLine += line
                allLore[filename[:-4]] = textLine

find_lore_recursive()

#render text
def drawText(window,font,colour,textToRender,startX,startY,space):
    #textToRender will be a string

    #split into individual words via spaces
    textLine = textToRender.split()

    #window ends at x = 1300, we need to wrap the text to prevent it going off screen
    XSpace = 1300 - startX

    #reformat text
    textToRender = []
    line = ""
    lineLen = 0
    for i in range(len(textLine)):
        if textLine[i] == "\p": # \p will denote the end of a paragraph
            textToRender.append(line)
            textToRender.append("") #add empty line
            line = ""
            lineLen = 0
        else:
            #either add text to existing line or create a new one and add it there
            if lineLen+font.size(textLine[i]+" ")[0] >= XSpace:
                textToRender.append(line)
                line = ""
                lineLen = 0

            if lineLen+font.size(textLine[i]+" ")[0] < XSpace:
                lineLen += font.size(textLine[i]+" ")[0]
                line += textLine[i]+ " "

    # We dont want the last line to be left out        
    textToRender.append(line)

    #print(textToRender)
    #write text to the screen
    lineNum = 0
    for line in textToRender:
        window.blit(font.render(line,True,colour),(startX,startY+space*lineNum))

        lineNum += 1

class Button:
    def __init__(self,x,y,width,height,text,colour,hoverColour,font,action):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.colour = colour
        self.hoverColour = hoverColour
        self.font = font
        self.action = action

    def draw(self,mousePos,window):
        if self.x < mousePos[0] < self.x + self.width and self.y < mousePos[1] < self.y + self.height:
            pygame.draw.rect(window,self.hoverColour,[self.x,self.y,self.width,self.height])
            if pygame.mouse.get_pressed()[0]:
                #button is being clicked
                self.action()
        else:
            pygame.draw.rect(window,self.colour,[self.x,self.y,self.width,self.height])
        window.blit(self.font.render(self.text,True,(255,255,255)),(self.x+10,self.y+10))
    