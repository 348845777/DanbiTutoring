import pygame

class Square():
    def __init__(self, gameInstance, x, y, squareDimension, color=(0, 0, 210), boxLineWidth=2):
        self.gameInstance = gameInstance
        self.x = x
        self.y = y
        self.squareDimension = squareDimension
        self.boxLineWidth = boxLineWidth
        self.color = color

    def draw(self):
        self.rectangleObject = pygame.draw.rect(self.gameInstance.window, self.color,
                 [self.x, self.y, self.squareDimension, self.squareDimension], self.boxLineWidth)
        

class Text():
    def __init__(self, gameInstance, x, y, text="", color=(255,255,0)):
        self.gameInstance = gameInstance
        self.x = x
        self.y = y
        self.text = text
        self.color = color

    def draw(self):
        textObject = self.gameInstance.defaultFont.render(str(self.text), False, self.color)    
        self.gameInstance.window.blit(textObject, (self.x,self.y))