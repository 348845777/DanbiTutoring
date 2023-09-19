import pygame
from screeninfo import get_monitors
import random
from pygame.locals import *
# import button

#TODO put button in another file
#TODO figure out what fps and fpsclock is for
#TODO figure out what display flip is for
#TODO don't make everything global

pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
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

objects = []

class Button(): 
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = my_font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])

        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        window.blit(self.buttonSurface, self.buttonRect)

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

def myFunction():
    global countdownTimer, gameComplete, clickCounter
    print('Button pressed')
    gameComplete = False
    clickCounter = 0
    countdownTimer = 10

customButton = Button(30, 30, 400, 100, 'Button One (onePress)', myFunction)
customButton1 = Button(30, 140, 400, 100, 'Button Two (multiPress)', myFunction, True)

while run is True:
    window.fill((0, 0, 0))
    for event in pygame.event.get():
        checkEvent(event, window)

        
    drawThings(window)
    for object in objects:
        object.process()

    pygame.display.flip()
    fpsClock.tick(fps)
    pygame.display.update()
pygame.quit()


# https://prod.liveshare.vsengsaas.visualstudio.com/join?FAFDCA5B918FABB04E6BF7583A7F8D983403