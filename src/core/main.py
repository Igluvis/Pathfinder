import pygame
from core.utils.grid import Grid


def main(win, width, height, rows, cols):
    '''
    main pygame loop
        win: pygame.window
        width: width of window
        height: height of window
    '''
    # create grid
    grid = Grid(rows, cols)

    # run loop
    run = True

    while run:
        for event in pygame.event.get():
            # Escape
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()