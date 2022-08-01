import pygame
from core.main import main

# Window
WIDTH = 600
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinder")

# Grid
ROWS, COLS = 15, 15

# Main loop
if WIDTH % COLS == 0 and HEIGHT % ROWS == 0:
    main(WIN, WIDTH, HEIGHT, ROWS, COLS)
else: print('Node size has to be integer')