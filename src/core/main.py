import pygame
import grid


def main(win, width):
    '''
    main pygame loop
    '''
    ROWS, COLS = 50

    # creates simple matrix
    # grid = grid(ROWS)  # matrix with values representing status of nodes (0 = walkable, 1 = non-walkable)

    # run loop
    run = True

    while run:
        for event in pygame.event.get():
            # Escape
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()