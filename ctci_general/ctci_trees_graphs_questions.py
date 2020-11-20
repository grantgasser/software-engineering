"""
CTCI Trees and Graphs Questions
"""

"""
1) Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""
def route(src, dst):
	q = [src]
	while q:
		curr = q.pop(0)
		curr.visited = True
		for n in curr.neighbors:
			if n == dst:
				return True
			if not n.visited:
				q.append(n)

	return False

"""
2) Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.

I worked it out, binary search is the way to go, but not searching, just going thru all
"""
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

def create_min_bst(arr, left, right):
    if (right < left):
        return None

    mid = (left + right) // 2
    node = Node(arr[mid])

    node.left = create_min_bst(arr, left, mid - 1)
    node.right = create_min_bst(arr, mid + 1, left)

    return node


def min_tree(arr):
    return create_min_bst(arr, 0, len(arr) - 1)
	

arr = [1, 3, 4, 7, 9, 13, 15]
tree = min_tree(arr)
print(tree.val)
print(tree.left.val)
print(tree.left.left.val)

# right sub
print(tree.right.val)