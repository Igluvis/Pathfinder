import pygame, sys, random
from core.pygame.visualize import draw_mazegrid


def binary_maze(draw, clock, start, end, grid):
    '''
    perfect maze
    starting at grid.nodes[0,0] for every 2 steps open randomly east or south border
        draw: updates screen with pygame
        clock: upper boundary for fps, regulates speed
        start: start node
        end: end node
        grid: grid
    '''
    draw()

    run = True
    mode = 'southeast'

    while run:
        # pygame quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # draw mazegrid
        draw_mazegrid(grid, start, end)

        # seperate grid into passages and borders
        for column in grid.nodes[::2]:
            for node in column[::2]:
                neighbors = grid.neighbors(node, mode, maze = True)
                # neighbors has to exist - corner edge case
                if neighbors:
                    # make passage randomly between 2 directions
                    passage = random.choice(neighbors)
                    if passage != start and passage != end:
                        passage.set_walkable()

                draw()
                clock()
        
        run = False