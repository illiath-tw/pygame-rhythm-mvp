# import pygame package 
import pygame

# import init and exit functions
from exit import exit
from init import init

# initialize the window
def main(): 
    init()

    # do other things
    print("working!")

def inputchecker():
    pygame.event.get(): 

    #if it is a quit action, run exit()
    if event.type == pygame.QUIT:
        exit(0)
#def gameloop():


main()
