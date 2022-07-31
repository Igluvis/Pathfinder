import pygame, sys, random
from core.pygame.visualize import draw_mazegrid


def sidewinder(draw, clock, start, end, grid):
    '''
    goes through columns and adds nodes to a list, randomly closes list and opens a passage to a predefined direction
        draw: updates screen with pygame
        clock: upper boundary for fps, regulates speed
        start: start node
        end: end node
        grid: grid
    '''
    draw()

    run = True
    mode = 'south'

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
            # set current
            current = column[0] 
            # group
            group = [current]
            
            while group:
                # close run
                if not grid.neighbors(current, mode, maze = True) or (
                    current.x > 0 and 
                    random.randrange(2) == 0
                    ):
                    node = random.choice(group)
                    if grid.neighbors(node, mode = 'west', maze = True):
                        passage = grid.neighbors(node, mode = 'west', maze = True)[0]
                        if passage != start and passage != end:
                            passage.set_walkable()

                    group = []
                
                elif grid.neighbors(current, mode, maze = True):
                    passage = grid.neighbors(current, mode, maze = True)[0]
                    if passage != start and passage != end:
                            passage.set_walkable()

                if grid.neighbors(current, mode, maze = True):
                    current = grid.node(current.x, current.y + 2)
                    group.append(current)
                    
                draw()
                clock()
        
        run = False