import pygame


from pygame.locals import *
pygame.init()
window=pygame.display.set_mode((800, 500)) # Create Screen (width x height)
window.fill((255, 0, 0))
rect = pygame.draw.rect(window, (0, 0, 210),
                 [100, 100, 400, 100], 2)
run = True

while run is True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = rect.collidepoint(pygame.mouse.get_pos())
            if click == 1:
                run = False
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()

# https://prod.liveshare.vsengsaas.visualstudio.com/join?E84A55C82187FFA656E39AEB8E92EE24F23A