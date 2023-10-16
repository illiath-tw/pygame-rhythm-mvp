# import stuff
import pygame
import sys
import asyncio

def exit():
    # have to quit display first to ensure that program doesn't lock up
    pygame.display.quit()
    # insert useful comment here
    pygame.quit()
    # throw a 0 to show that it worked properly
    sys.exit()
