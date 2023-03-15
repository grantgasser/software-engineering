from binary_tree import TreeNode

"""
Also, "level order" traversal is a breadth-first search in a tree

Also, "in-order" on a BST is the sorted order of the elements
"""

# left remains before right, only thing changes is the
# order of the print and recursive calls
def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    if node:
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data)

"""
      10
  5       15
2    7  12    17
"""

# test
tree = TreeNode(10)
tree.left = TreeNode(5)
tree.right = TreeNode(15)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(7)
tree.right.left = TreeNode(12)
tree.right.right = TreeNode(17)

print('\nInorder:')
inorder(tree)

print('\nPreorder:')
preorder(tree)

print('\nPostorder:')
postorder(tree)

