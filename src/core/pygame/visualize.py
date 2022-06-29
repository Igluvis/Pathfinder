import pygame


# Colors
RED = (255, 0, 0)           # start
GREEN = (0, 255, 0)         # Open
BLACK = (0, 0, 0)           # Wall
ORANGE = (255, 165 ,0)      # closed
TURQUOISE = (64, 224, 208)  # End
PURPLE = (128, 0, 128)      # ?
WHITE = (220, 220, 220)     # grid
BLUE = (0, 0, 255)          # PATH
YELLOW = (255, 255, 0)      # ?
GREY = (119, 136, 153)      # walkable

color_dic = {
    'walkable': GREY,
    'wall': BLACK,
    'start': RED,
    'end': BLUE,
    'closed': ORANGE,
    'open': GREEN,
    'path': TURQUOISE
}

def draw_grid(win, width, height, rows, cols):
    '''
    draws grid lines
        win: active pygame window
        width: width of window
        height: height of window
        rows: amount of rows
        cols: amount of columns
    '''
    color = BLACK
    gap_x = width // cols
    gap_y = height // rows
    for i in range(cols):
        pygame.draw.line(win, color, (0, i * gap_x), (height, i * gap_x))

    for j in range(rows):
        pygame.draw.line(win, color, (j * gap_y, 0), (j * gap_y, width))    

def get_color(node):
    '''
    returns color depending on current status of node
        node: node
    '''
    return color_dic[node.status]

def draw_nodes(win, grid, width, height):
    '''
    draws rectangles for each node
        win: pygame window
        grid: grid
        width: width of node
        height: height of node
    '''
    for columns in grid.nodes:
        for node in columns:
            pygame.draw.rect(win, get_color(node), (node.x * width, node.y * height, width, height))

def draw(win, grid, width, height, rows, cols):
    '''
    draws background, nodes and grid lines
        win: active pygame window
        grid: grid
        width: width of window
        height: height of window
        rows: amount of rows
        cols: amount of columns
    '''
    win.fill(WHITE)

    draw_nodes(win, grid, width=width/cols, height=height/rows)
    draw_grid(win, width, height, rows, cols)

    # BRUH I FORGOT .update AND WASTED 2h SEARCHING FOR THIS
    pygame.display.update()