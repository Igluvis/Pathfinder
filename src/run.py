import pygame
from core.main import main

# Window
WIDTH = 800
HEIGHT = 800 
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathfinder")

# Main loop
main(WIN, WIDTH, HEIGHT)