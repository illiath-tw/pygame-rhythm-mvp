# import pygame package 
import pygame
import pygame.gfxdraw

# import init and exit functions
from exit import exit
from init import init

# initialize the window
def main(): 
    init()

    # do other things
    print("working!")   
    drawgameplayarea()
    inputchecker()

def inputchecker():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
def gameloop():
    running = true
    while running == true:
        inputchecker()
    

def drawgameplayarea():
    bg = pygame.Surface((1920, 1080), flags=0, depth=8)
    wholescreen = pygame.Rect(0, 0, 1920, 1080)
    white = pygame.Color(255, 255, 255)
    pygame.gfxdraw.box(bg, wholescreen, white)
    

    
main()
