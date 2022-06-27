from .node import Node


def build_nodes(rows, cols):
    '''
    node[x][y]
    makes a simple matrix with y rows and x cols containing a node
    walkable : walkable = 1; not walkable = 0
        rows: number of rows
        cols: number of cols
    '''
    nodes = []
    for x in range(cols):
        nodes.append([])
        for y in range(rows):
            # check if border
            if y == 0 or y == rows - 1 or x == 0 or x == cols - 1:
                nodes[x].append(Node(x=x, y=y, walkable=0))

            else:
                nodes[x].append(Node(x=x, y=y, walkable=1))

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
        get node at pos (x,y)
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
        returns if node at (x,y) is walkable == 1 and has to exist
            x: x coord
            y: y coord
        '''
        return self.nodes[x][y].walkable and self.inside(x, y)

    def neighbors(self, node):
        '''
        get all neighbors of one node
        1. checks each neighbor if walkable
        2. adds neighbor node to list
            node: node
        '''
        # coords
        x = node.x
        y = node.y

        neighbors = []

        # ↑
        if self.walkable(x, y - 1):
            neighbors.append(self.nodes[x][y - 1])

        # →
        if self.walkable(x + 1, y):
            neighbors.append(self.nodes[x + 1][y])

        # ←          
        if self.walkable(x - 1, y):
            neighbors.append(self.nodes[x - 1][y])

        # ↓
        if self.walkable(x, y + 1):
            neighbors.append(self.nodes[x][y + 1])

        return neighbors

    def cleanup(self):
        for x_nodes in self.nodes:
            for node in x_nodes:
                node.cleanup()