import heapq


def a_star(draw, start, end, grid):
    '''
        draw: updates screen with pygame
        start: start node
        end: end node
        grid: grid
    '''
    draw()