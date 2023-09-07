import pygame


from pygame.locals import *
pygame.init()
window=pygame.display.set_mode((800, 500)) # Create Screen (width x height)
window.fill((255, 0, 0))
pygame.draw.rect(window, (0, 0, 200),
                 [100, 100, 400, 100], 2)
run = True
while run is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

