class Node(object):
    '''
    Node with own x and y coordinates on a grid
    '''
    def __init__(self, x=0, y=0, status='walkable', cost=1):
        # Coordinates
        self.x = x
        self.y = y

        '''
        walkable
            start
            end
        wall
        closed
        open
        '''
        self.status = status
        self.g = 0
        self.cost = cost

    def __lt__(self, other):
        '''
        in A* compare f value against infinity if not already calculated
        h as tiebreaker
        '''
        try:
            return self.f < other.f if self.f != other.f else self.h < other.h
        except:
            return self.g < other.g

    # get status methods
    def get_wall(self):
        return self.status == 'wall'

    def get_walkable(self):
        return self.status == 'walkable' or self.status == 'start' or self.status == 'end'

    def get_start(self):
        return self.status == 'start'

    def get_end(self):
        return self.status == 'end'

    def get_closed(self):
        return self.status == 'closed'

    def get_open(self):
        return self.status == 'open'

    def get_path(self):
        return self.status == 'path'

    # set status methods
    def set_wall(self):
        self.status = 'wall'
    
    def set_walkable(self):
        self.status = 'walkable'

    def set_start(self):
        self.status = 'start'

    def set_end(self):
        self.status = 'end'

    def set_closed(self):
        self.status = 'closed'

    def set_open(self):
        self.status = 'open'

    def set_path(self):
        self.status = 'path'

    def cleanup(self):
        # backtracking
        self.parent = None

        # make walkable
        if not self.get_start() and not self.get_end() and not self.get_wall():
            self.set_walkable()

        # cost cleanup
        self.h = 0
        self.g = 0
        self.f = 0