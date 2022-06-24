class Node():
    '''
    Node with own x and y coordinates on a grid
    '''
    def __init__(self, x, y, walkable):
        # Coordinates
        self.x = x
        self.y = y

        # Node status; 0 = walkable, 1 = not
        self.walkable = walkable

    def __lt__(self, other):
        '''
        in A* compare f value against infinity if not already calculated
        '''
        return False