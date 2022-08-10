import pygame, sys
from core.utils.backtracking import backtrace


def breadth_first(draw, clock, start, end, grid):
    '''
    starting at start node, frontier is expanding outward,
    whilst marking visited nodes
        draw: updates screen with pygame
        clock: upper boundary for fps, regulates speed
        start: start node
        end: end node
        grid: grid
    '''
    draw()

    # put start in frontier list
    frontier = [start]

    while len(frontier) > 0:
        # pygame quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # aquire new current node from frontier list
        current = frontier.pop(0)

        # found path
        if current == end:
            backtrace(draw, current, start, end, grid)
            return True

        # close current node
        if current != start:
            current.set_closed()

        # neighbors
        neighbors = grid.neighbors(current)

        # add each neighbor from current who is not in visited to frontier
        for neighbor in neighbors:
            # skip visited nodes
            if neighbor.get_closed() or neighbor.get_open():
                continue
            
            frontier.append(neighbor)

            # trace parent for backtracking
            neighbor.parent = current
            if not neighbor.get_end() and not neighbor.get_start():
                neighbor.set_open()
        
        if grid.cols < 30 and grid.rows < 30:
            draw()
            clock()
    
    # path from start or end blocked
    print('No path found!')
    return False