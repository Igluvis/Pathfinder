import pygame, sys, random


def draw_mazegrid(grid, start, end):
    '''
    ooooo
    oxoxo
    ooooo
    draws x's
        grid: grid
        start: start node
        end: end node
    '''
    for column in grid.nodes[1::2]:
            for node in column[1::2]:
                if node != start and node != end:
                    node.set_wall()

def binary_maze(draw, clock, start, end, grid):
    '''
    starting at grid.nodes[0,0] for every 2 steps open randomly east or south border
        draw: updates screen with pygame
        clock: upper boundary for fps, regulates speed
        start: start node
        end: end node
        grid: grid

        works only for uneven grid sizes
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

        # draw pillars
        draw_mazegrid(grid, start, end)

        # seperate grid into passages and borders
        for column in grid.nodes[::2]:
            for node in column[::2]:
                neighbors = grid.neighbors(node, mode, maze = True)
                # neighbors has to exist - corner edge case
                if neighbors:
                    for neighbor in neighbors: 
                        if neighbor != start and neighbor != end:
                            neighbor.set_wall()
                    
                    # make passage
                    passage = random.choice(neighbors)
                    if passage != start and passage != end:
                        passage.set_walkable()

                draw()
                clock()
        
        run = False