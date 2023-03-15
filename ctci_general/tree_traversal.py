"""
CTCI Tree Traversal
"""

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

"""
tree:
        1
    2       3
4      5     

(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Note for a BST, in-order search should produce the sorted order of the elements

        5
    2       8
1      3        10

Inorder: 1 2 3 5 8 10
"""

def in_order(node):
    if not node:
        return 
    
    in_order(node.left)
    print(node.val)
    in_order(node.right)

print('\nin order:')
in_order(root)

def pre_order(node):
    if not node:
        return 
    
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

print('\npre order:')
pre_order(root)

def post_order(node):
    if not node:
        return 
    
    post_order(node.left)
    post_order(node.right)
    print(node.val)

print('\npost order:')
post_order(root)


print('\nConstructing BST.')
bst = Node(5)
bst.left = Node(2)
bst.left.left = Node(1)
bst.left.right = Node(3)
bst.right = Node(8)
bst.right.right = Node(10)

print('\nin order (bst):')
in_order(bst)


def bfs(node):
    if not node:
        raise ValueError('Node is empty.')

    q = [node]

    while q:
        #print('Q:', [e.val for e in q])
        curr_node = q.pop(0)
        print(curr_node.val)

        for n in [curr_node.left, curr_node.right]:
            if n:
                q.append(n)

print('\nBFS:')
bfs(bst)