class Node():
    '''
    Node with own x and y coordinates on a grid
    '''
    def __init__(self, x, y, status):
        # Coordinates
        self.x = x
        self.y = y

        '''
        walkable
        wall
        start
        end
        '''
        self.status = status

    def __lt__(self, other):
        '''
        in A* compare f value against infinity if not already calculated
        '''
        return False

    def cleanup(self):
        self.status = 'walkable'