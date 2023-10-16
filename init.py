# import pygame
import pygame
from exit import exit

def init():
    # initializing imported module 
    pygame.init() 
  
    # displaying a window of height 
    # 500 and width 400 
    pygame.display.set_mode((640, 480))

    # set the title

    pygame.display.set_caption('Untitled Rhythm Game')

    # creating a bool value which checks 
    # if game is running 
    #running = True
  
    # keep game running till running is true 
    #while running: 
      
        # Check for event if user has pushed 
        # any event in queue 
        #for event in pygame.event.get(): 
          
            # if event is of type quit then  
            # set running bool to false 
            #if event.type == pygame.QUIT: 
                #running = False

    # Game's over. Quitting!
    #exit()
