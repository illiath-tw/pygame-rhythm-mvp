# import pygame package 
import pygame

# import init and exit functions
from exit import exit
from init import init

# initialize the window
init()

# creating a bool value which checks 
# if game is running 
running = True
  
# keep game running till running is true 
while running: 
      
    # Check for event if user has pushed 
    # any event in queue 
    for event in pygame.event.get(): 
          
        # if event is of type quit then  
        # set running bool to false 
        if event.type == pygame.QUIT: 
            running = False

#Game's over. Quitting!
exit()
