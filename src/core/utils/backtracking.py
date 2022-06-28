def backtrace(draw, current, start, end):
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
        draw()

    return path