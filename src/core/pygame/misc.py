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