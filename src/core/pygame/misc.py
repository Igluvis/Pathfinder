import heapq


def get_node(pos, grid, width, height):
    '''
    gets node on grid based on mouse pos
    returns corresponding node
        pos: mouse position on press
        grid: grid
        rows: rows
        cols: cols
    return: node
    '''
    x_pos, y_pos = pos
    x = x_pos // width
    y = y_pos // height
    
    return grid.node(x,y)

def algo_clock(clock_gear):
    '''
    returns fps for algo visualizer clock
    fps     s to complete
    30      44
    60      22
    120     11
        clock_gear: int from [0,1,2]
    '''
    match clock_gear:
        case 0: return 30
        case 1: return 60
        case 2: return 120

def get_g(node):
    return node.g

def find_furthest_node(grid):
    '''
    return node with highest g value
        grid: grid
    '''
    visited = []
    for column in grid.nodes:
        for node in column:
            if node.get_closed():
                visited.append(node)

    visited.sort(key=get_g)
    furthest = visited[-1]
    print(furthest.g)
    return furthest