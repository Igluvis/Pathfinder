class Node():
    '''
    Node with own x and y coordinates on a grid
    '''
    def __init__(self, x=0, y=0, status='walkable'):
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

    # get status methods
    def get_wall(self):
        return self.status == 'wall'

    def get_walkable(self):
        return self.status == 'walkable'

    def get_start(self):
        return self.status == 'start'

    def get_end(self):
        return self.status == 'end'

    # set status methods
    def set_wall(self):
        self.status = 'wall'
    
    def set_walkable(self):
        self.status = 'walkable'

    def set_start(self):
        self.status = 'start'

    def set_end(self):
        self.status = 'end'

