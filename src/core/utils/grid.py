from .node import Node


def build_nodes(rows, cols):
    '''
        node[x][y]
        makes a simple matrix with y rows and x cols containing a node
        status
            rows: number of rows
            cols: number of cols
    '''
    nodes = []

    for x in range(cols):
        nodes.append([])
        for y in range(rows):
            # create node
            nodes[x].append(Node(x=x, y=y, status='walkable'))

    return nodes 

class Grid():
    '''
    creates nodes according to grid size
    '''
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.nodes = build_nodes(self.rows, self.cols)

    def node(self, x, y):
        '''
        get Node at pos (x,y)
            x: x coord
            y: y coord
        '''
        return self.nodes[x][y]

    def inside(self, x, y):
        '''
        check, if field position is inside map
            x: x pos
            y: y pos
        '''
        return 0 <= x < self.cols and 0 <= y < self.rows

    def walkable(self, x, y):
        '''
        helper function
        checks if Node is inside Grid, walkable
            x: x coord
            y: y coord
        '''
        return (self.nodes[x][y].get_walkable() or self.nodes[x][y].get_end()) if self.inside(x, y) else False

    def neighbors(self, node, mode = 'all'):
        '''
        get all neighbors of one node
        1. checks each neighbor if walkable
        2. adds neighbor node to list
            node: node
            mode: string(all, northeastsouthwest)
        '''
        # coords
        x = node.x
        y = node.y

        neighbors = []

        # ↑
        if self.walkable(x, y - 1) and (mode == 'all' or 'north' in mode):
            neighbors.append(self.nodes[x][y - 1])

        # →
        if self.walkable(x + 1, y) and (mode == 'all' or 'east' in mode):
            neighbors.append(self.nodes[x + 1][y])

        # ←          
        if self.walkable(x - 1, y) and (mode == 'all' or 'west' in mode):
            neighbors.append(self.nodes[x - 1][y])

        # ↓
        if self.walkable(x, y + 1) and (mode == 'all' or 'south' in mode):
            neighbors.append(self.nodes[x][y + 1])

        return neighbors

    def cleanup(self):
        '''
        resets node.parent and node.status to default in grid
        '''
        for columns in self.nodes:
            for node in columns:
                node.cleanup()