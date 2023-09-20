import pygame
from screeninfo import get_monitors
import random
from pygame.locals import *
from button import Button
from gameInstance import GameInstance, GameVariables
from gameObjects import Square, Text
#TODO put button in another file
#TODO figure out what fps and fpsclock is for
#TODO figure out what display flip is for
#TODO don't make everything global

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()
window=pygame.display.set_mode() # Create Screen (width x height)

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

squareDimension = 100
monitors = get_monitors() 
randx = random.randint(0, monitors[0].width - squareDimension)
randy = random.randint(0, monitors[0].height - squareDimension)

clickCounter = 0
countdownTimer = 10

gameVariables = GameVariables(clickCounter, countdownTimer)
gameInstance = GameInstance(window, my_font, gameVariables)

gameObjects = []
gameSquare = Square(gameInstance, randx, randy, squareDimension)
clickCounterText = Text(gameInstance, 0, 100, gameInstance.gameVariables.clickCounter)
countdownText = Text(gameInstance, 0, 0, gameInstance.gameVariables.countdownTimer)
gameObjects.append(gameSquare)
gameObjects.append(clickCounterText)
gameObjects.append(countdownText)

def checkUserInput(event, instance):
    global gameSquare, countdownText
    if not instance.gameComplete:
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = gameSquare.rectangleObject.collidepoint(pygame.mouse.get_pos())
            
            if click == 1:
                instance.gameVariables.clickCounter = instance.gameVariables.clickCounter +1
                clickCounterText.text = instance.gameVariables.clickCounter
                gameSquare.x = random.randint(0, monitors[0].width - squareDimension)
                gameSquare.y = random.randint(0, monitors[0].height - squareDimension)
            
    if event.type == KEYDOWN and event.key == K_ESCAPE:
        pygame.quit()
    if event.type == pygame.QUIT:
        pygame.quit()

def checkCounterEvent(event, instance):
    global countdownText
    if not instance.gameComplete:
       if event.type == pygame.USEREVENT: 
            if instance.gameVariables.countdownTimer == 0: 
                instance.gameComplete = True
            else:
                instance.gameVariables.countdownTimer = instance.gameVariables.countdownTimer -1
                countdownText.text = instance.gameVariables.countdownTimer    

def resetGame(instance):
    global countdownText, timerText
    print('Game Reset')
    instance.gameComplete = False
    instance.gameVariables.clickCounter = 0
    instance.gameVariables.countdownTimer = 10
    countdownText.text = instance.gameVariables.countdownTimer

buttons = []
customButton = Button(gameInstance, 30, 30, 400, 100, 'Reset Game', resetGame)
buttons.append(customButton)

while True:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        checkUserInput(event, gameInstance)
        checkCounterEvent(event, gameInstance)

    for object in gameObjects:
        object.draw()

    for button in buttons:
        button.process()
    
    fpsClock.tick(fps)
    pygame.display.flip()



# https://prod.liveshare.vsengsaas.visualstudio.com/join?FAFDCA5B918FABB04E6BF7583A7F8D983403