import pygame
from core.utils.grid import Grid
from core.pygame.visualize import draw
from core.pygame.misc import get_node

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

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    if start:
                        start.cleanup()
                    node = get_node(pygame.mouse.get_pos(), grid, width=width//cols, height=height//rows)
                    node.status = 'start'
                    start = node

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if end:
                        end.cleanup()
                    node = get_node(pygame.mouse.get_pos(), grid, width=width//cols, height=height//rows)
                    node.status = 'end'

            # Draw wall with left mouse click
            if pygame.mouse.get_pressed()[0]:
                node = get_node(pygame.mouse.get_pos(), grid, width=width//cols, height=height//rows)
                node.status = 'wall'

            # empty node with right click
            if pygame.mouse.get_pressed()[2]:
                node = get_node(pygame.mouse.get_pos(), grid, width=width//cols, height=height//rows)
                node.status = 'walkable'

    pygame.quit()