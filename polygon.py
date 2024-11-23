import pygame
from pygame.locals import *
 
pygame.init()
 
window = pygame.display.set_mode((600, 600))
 
window.fill((255, 255, 255))
 
pygame.draw.polygon(window, (255, 0, 0), [[300, 300], [100, 400],[100, 300]])

pygame.display.update()



