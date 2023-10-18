# import pygame package 
import pygame
import pygame.gfxdraw
import pygame
import sys

def init():
    pygame.init()
    DISPLAY = pygame.display.set_mode((512, 1024))
    DISPLAY.fill((175, 193, 124))
    pygame.display.update()
    pygame.time.delay(10000)

def quitmain():
    pygame.quit()
    sys.exit()

init()
quitmain()
