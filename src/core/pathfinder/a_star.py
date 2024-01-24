import pygame, sys
from core.utils.backtracking import backtrace
import heapq
from .heuristic import manhattan, octile


def a_star(draw, clock, start, end, grid):
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

    # set start.g and start.f
    start.g = 0
    start.f = 0

    # put start in frontier list
    frontier = [start]

    while len(frontier) > 0:
        # pygame quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # aquire new current node from frontier list
        current = heapq.nsmallest(1, frontier)[0]
        frontier.remove(current)

        # found path
        if current == end:
            backtrace(draw, current, start, end, grid)
            return True

        # neighbors
        neighbors = grid.neighbors(current)

        # add each neighbor from current who is not in visited to frontier
        for neighbor in neighbors:
            # temp  g cost            
            temp_g = current.g + neighbor.cost
            
            # if neighbor not already visited or better path found
            if not neighbor.g or temp_g < neighbor.g:
                # g : distance from start to neighbor
                neighbor.g = temp_g 
                # h : estimated distance from neighbor to end
                neighbor.h = manhattan(neighbor, end)  
                # f : estimated distance from start to end
                neighbor.f = neighbor.g + neighbor.h

                # trace parent for backtracking
                neighbor.parent = current

                if neighbor not in frontier:
                    heapq.heappush(frontier, neighbor)
                    if not neighbor.get_end() and not neighbor.get_start():
                        neighbor.set_open()

        if grid.cols < 100 and grid.rows < 100:
            draw()
            clock()
        
        # close current node
        if current != start:
            current.set_closed()
    
    # path from start or end blocked
    print('No path found!')
    return False