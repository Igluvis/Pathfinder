import math


def octile(node_a, node_b):
    f = math.sqrt(2) - 1
    dx = abs(node_a.x - node_b.x)
    dy = abs(node_a.y - node_b.y)
    if dx < dy:
        return f * dx + dy
    else:
        return f * dy + dx

def manhattan(node_a, node_b):
    return abs(node_a.x - node_b.x) + abs(node_a.y - node_b.y)