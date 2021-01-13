"""
4.1 
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.

Using BFS
"""
from graphs import Graph, Node
from collections import deque

def route(src_node, dst_val):
    # bfs
    q = deque(src_node)

    # might need to set all visited to False in case this graph
    # has been used before

    while q:
        curr = q.popleft()
        curr.visited = True

        if curr.data == dst_val:
            return True

        for child in curr.children:
            if not child.visited:
                q.append(child)

    return False
