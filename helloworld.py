import pygame
from screeninfo import get_monitors
import random
from pygame.locals import *
pygame.init()
window=pygame.display.set_mode() # Create Screen (width x height)
window.fill((0, 0, 0))
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

squareDimension = 100

monitors = get_monitors() 
randx = random.randint(0, monitors[0].width - squareDimension)

randy = random.randint(0, monitors[0].height - squareDimension)

pygame.time.set_timer(pygame.USEREVENT, 1000)

rect = pygame.draw.rect(window, (0, 0, 210),
                 [randx, randy, squareDimension, squareDimension], 2)
clickCounter = 0
run = True
countdownTimer = 10
gameComplete = False
text_surface = my_font.render(str(countdownTimer), False, (255,255,0))
clickobject = my_font.render(str(clickCounter), False, (255,255,0))
print()



def drawThings(_window):
    global randx, randy, text_surface, rect, squareDimension, clickobject
    rect = pygame.draw.rect(_window, (0, 0, 210), [randx, randy, squareDimension, squareDimension], 2)
    _window.blit(text_surface, (0,0))
    _window.blit(clickobject, (0,100))
def checkEvent(event, window):
    global countdownTimer, gameComplete, run, randx, randy, text_surface, clickCounter, clickobject
    if not gameComplete:
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = rect.collidepoint(pygame.mouse.get_pos())
            
            if click == 1:
                clickCounter = clickCounter +1
                randx = random.randint(0, monitors[0].width - squareDimension)

                randy = random.randint(0, monitors[0].height - squareDimension)
            clickobject = my_font.render(str(clickCounter), False, (255,255,0))    

        elif event.type == pygame.USEREVENT: 
            if countdownTimer == 0: 
                gameComplete = True
            else:
                countdownTimer = countdownTimer -1
            text_surface = my_font.render(str(countdownTimer), False, (255,255,0))
            
             
    if event.type == KEYDOWN and event.key == K_ESCAPE:
        run = False 
    if event.type == pygame.QUIT:
        run = False

while run is True:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        
        checkEvent(event, window)
    drawThings(window)
    pygame.display.update()
pygame.quit()


# https://prod.liveshare.vsengsaas.visualstudio.com/join?4EBA39F400052D79093CCDADCFDD72B90250