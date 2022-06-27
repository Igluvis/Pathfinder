import pygame
import grid


def main(win, width, height):
    '''
    main pygame loop
        win: pygame.window
        width: width of window
        height: height of window
    '''
    ROWS, COLS = 50, 50
    # create grid

    # run loop
    run = True

    while run:
        for event in pygame.event.get():
            # Escape
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()