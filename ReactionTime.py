################################################################################
# Imports ######################################################################
################################################################################

from pygame.locals import *
import pygame, sys, math

################################################################################
# Screen Setup #################################################################
################################################################################

pygame.init()
scr = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Box Test')

################################################################################
# Game Loop ####################################################################
################################################################################

while True:
    pygame.display.update(); scr.fill((200, 200, 255))
    pygame.draw.circle(scr, (0, 0, 0), (400, 300), 100)

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]

    sqx = (x - 400)**2
    sqy = (y - 300)**2

    if math.sqrt(sqx + sqy) < 100:
        print 'inside'

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

################################################################################
################################################################################
################################################################################