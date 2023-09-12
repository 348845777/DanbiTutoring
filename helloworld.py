import pygame
from screeninfo import get_monitors
import random
from pygame.locals import *
pygame.init()
window=pygame.display.set_mode() # Create Screen (width x height)
window.fill((0, 0, 0))

squareDimension = 100

monitors = get_monitors() 
randx = random.randint(0, monitors[0].width - squareDimension)

randy = random.randint(0, monitors[0].height - squareDimension)



rect = pygame.draw.rect(window, (0, 0, 210),
                 [randx, randy, squareDimension, squareDimension], 2)

run = True

print()
while run is True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = rect.collidepoint(pygame.mouse.get_pos())
            if click == 1:
                window.fill((0, 0, 0))
                randx = random.randint(0, monitors[0].width - squareDimension)

                randy = random.randint(0, monitors[0].height - squareDimension)

                rect = pygame.draw.rect(window, (0, 0, 210), [randx, randy, squareDimension, squareDimension], 2)
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            run = False
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

# https://prod.liveshare.vsengsaas.visualstudio.com/join?4EBA39F400052D79093CCDADCFDD72B90250