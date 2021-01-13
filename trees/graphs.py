"""
Adjacency List

Could use hash table of lists (array, linkedlist, etc.), more compact
    => 0: [1]
       1: [2]
       2: [0, 3]

but a bit cleaner to use classes:
    => so basically just wrap the list in a node class
"""
class Graph(object):
    """
    The Graph class is used because, unlike in a tree, 
    you can't necessarily reach all the nodes from a single node.
    """
    def __init__(self, nodes=[]):
        self.nodes = nodes

class Node(object):
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.children = []


"""
Adjacency Matrix (2d array, 2d "list" in python) of 1s and 0s

0 -> 1
  ^  |
   \ v
3 -> 2
"""
graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]

# NOTE: all graph algorithms can be done on both adj. lists AND adj. matrices
# matrics somewhat less efficient because you have to check entire row (all nodes)
# identify the neighbors; with list, you know the neighbors and can iterate right
# thru the list

"""
Graph Search

DFS preferred if we want to visit every node in the graph, but either will work

BFS is better for shortest path (or any path) between 2 nodes
    => with a large graph, DFS might take you wayyyy down the rabbit hole when 
    the desired node could be as close as being a neighbor
"""

# RECURSIVE
def dfs(node):
    if not node:
        return
    
    print(node.data)

    # dfs
    node.visited = True
    for n in node.children:
        if not n.visited:
            dfs(n)

from collections import deque

# NOT RECURSIVE, JUST QUEUE
def bfs(node):
    if not node:
        return
    
    q = deque(node)
    while q:
        # deal with current node
        curr = q.popleft()
        curr.visited = True
        print(curr.data)

        # add neighbor nodes to the queue so they're visited before children
        for child in curr.children:
            if not child.visited:
                q.append(child)

"""
Bidirectional Search: shortest path between source and destination node
runs 2 simultaneous BFS, 1 from source and 1 from destination

ASSUMPTION: you know the dst exists and you have reference to it, you're
more concerned about the path than actually getting to the dst as you 
typically are in search problem

Bidirectional: O(k^(d/2)) where k is max # of neighbors a node can have and 
d is the # of levels (nodes) away src is from dst

BFS: O(k^d)
"""