def backtrace(draw, current, start, end, grid):
    '''
    draw: update window
    current: current node
    '''
    path = []
    while current != start:
        path.append(current)

        # draw path
        if not current.get_end() and not current.get_start():
                current.set_path()

        current = current.parent
        if grid.cols < 30 and grid.rows < 30:
                    draw()

    return path