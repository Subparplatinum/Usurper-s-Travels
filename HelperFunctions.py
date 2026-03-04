import pygame

#render text
def drawText(window,font,colour,textToRender,startX,startY,space):
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
    