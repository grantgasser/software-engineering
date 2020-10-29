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
        1
    2       3
4      5     

(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1
"""

def in_order(node):
    if node == None:
        return node 
    
    in_order(node.left)
    print(node.val)
    in_order(node.right)

print('\nin order:')
print(in_order(root))

def pre_order(node):
    if node == None:
        return node 
    
    print(node.val)
    pre_order(node.left)
    pre_order(node.right)

print('\npre order:')
print(pre_order(root))

def post_order(node):
    if node == None:
        return node 
    
    post_order(node.left)
    post_order(node.right)
    print(node.val)

print('\npost order:')
print(post_order(root)) 