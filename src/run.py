import pygame
from core.main import main

# Window
WIDTH = 660
HEIGHT = 660
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinder")

# Grid
ROWS, COLS = 55, 55

# Main loop
if WIDTH % COLS == 0 and HEIGHT % ROWS == 0:
    main(WIN, WIDTH, HEIGHT, ROWS, COLS)
else: print('Node size has to be integer')