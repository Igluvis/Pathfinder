import pygame
from core.utils.grid import Grid
from core.pygame.visualize import draw

def main(win, width, height, rows, cols):
    '''
    main pygame loop
        win: pygame.window
        width: width of window
        height: height of window
    '''
    # create grid
    grid = Grid(rows, cols)

    # functional nodes
    start = None
    end = None
    
    # run loop
    run = True

    while run:
        # update screen
        draw(win, grid, width, height, rows, cols)
        for event in pygame.event.get():
            # Escape
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()