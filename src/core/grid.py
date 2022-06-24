from utils.node import Node


def build_nodes(rows, cols):
    '''
    node[x][y]
    makes a simple matrix with number of rows and cols equal to rows
    marks unwalkable nodes with values of 1
    '''
    nodes  = []
    for x in range(rows):
        nodes .append([])
        for y in range(cols):
            if y == 0 or y == rows - 1 or x == 0 or x == rows - 1:
                nodes [x].append(Node(x=x, y=y, walkable=1))

            else:
                nodes [x].append(Node(x=x, y=y, walkable=0))

    return nodes 

class Grid():
    '''
    creates nodes according to grid size
    '''
    def __init__(self, rows, cols, matrix):
        self.rows = rows
        self.cols = cols

        self.nodes = build_nodes(self.rows, self.cols)

    def node(self, x, y):
        '''
        get node at pos (x,y)
        '''
        return self.nodes[x][y]

    def neighbors(self, node):
        '''
        get all neighbors of one node
        '''
        # coords
        x = node.x
        y = node.y

        neighbors = []

        # ↓
        if self.row < self.total_rows - 1 and not self.nodes[self.row + 1][self.col].is_barrier():
            self.neighbors.append(self.nodes[self.row + 1][self.col])

        # ↑
        if self.row > 0 and not self.nodes[self.row - 1][self.col].is_barrier():
            self.neighbors.append(self.nodes[self.row - 1][self.col])

        # →
        if self.col < self.total_rows - 1 and not self.nodes[self.row][self.col + 1].is_barrier():
            self.neighbors.append(self.nodes[self.row][self.col + 1])

        # ←          
        if self.col > 0 and not self.nodes[self.row][self.col - 1].is_barrier():
            self.neighbors.append(self.nodes[self.row][self.col - 1])
