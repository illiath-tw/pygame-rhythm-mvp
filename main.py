# import pygame package 
import pygame
import pygame.gfxdraw
import pygame
import sys

# define base colors
bgcolor = [66, 0, 57]
color2 = [147, 47, 109]
color3 = [224, 123, 224]
color4 = [220, 204, 255]
color5 = [246, 242, 255]

# define display size
displaysize = [512, 1024]

def init():
    
    # initialize pygame
    pygame.init()

    # set background color
    DISPLAY = pygame.display.set_mode((displaysize))
    DISPLAY.fill((bgcolor))

    # update display
    pygame.display.update()
    

def quitmain():

    #quit pygame and exit
    pygame.quit()
    sys.exit()

#initialize game
init()

# wait a moment
pygame.time.delay(1000)

#quit app
quitmain()
