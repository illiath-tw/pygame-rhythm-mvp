from itertools import product

import pygame
import sys

pygame.init()
DISPLAY = pygame.display.set_mode((512, 1024))
DISPLAY.fill((175, 193, 124))
pygame.display.update()
#for r, g, b in product(range(0, 255, 16), repeat=3):
#    print('r={}, g={}, b={}'.format(r, g, b))
#    DISPLAY.fill((r, g, b))
#    pygame.display.update()
#    pygame.time.delay(100)
pygame.time.delay(10000)
#raw_input("Press Enter to continue...")
pygame.quit()
sys.exit()
