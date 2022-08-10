import math


def octile(node_a, node_b):
    '''
    calculates distance for 2 nodes based on octile geometry
        node_a: node
        node_b: node
    '''
    f = math.sqrt(2) - 1
    dx = abs(node_a.x - node_b.x)
    dy = abs(node_a.y - node_b.y)
    if dx < dy:
        return f * dx + dy
    else:
        return f * dy + dx

def manhattan(node_a, node_b):
    '''
    calculates distance for 2 nodes based on manhattan geometry
        node_a: node
        node_b: node
    '''
    return abs(node_a.x - node_b.x) + abs(node_a.y - node_b.y)