"""
4.5 Validate BST: Implement a function to check if a binary tree is a binary search tree.

BST: left child <= parent < right child

NOTE: solution is subpar, only compares children to parents, 
    - what about to grandparents or higher? i.e. what if 8 was changed to 11. 
    its > 6 so it would pass here, but also greater than 9 so thats not good

    => to improve, keep track of prev nodes in a list or queue


EASY SOLUTION (p. 258, assuming no duplicates): do in-order traversal and put 
elements in array, then check to see if array is sorted.

Probably need to look at this one closer...
"""

from binary_tree import TreeNode

def inorder(root, side=None, parent_val=None):
    if root:
        res = inorder(root.left, 'left', root.data)  # go left
        if not res:
            return False

        # check BST rule
        if side == 'left':
            if root.data > parent_val:
                print('Not BST. Left child > parent: {} > {}'.format(root.data, parent_val))
                return False
        elif side == 'right':
            if root.data <= parent_val:
                print('Not BST. Right child <= parent: {} <= {}'.format(root.data, parent_val))
                return False

        res = inorder(root.right, 'right', root.data)  # go right
        if not res:
            return False

    return True

def validate_bst(root):
    return inorder(root)
    

root = TreeNode(9)
root.left = TreeNode(6)
root.left.right = TreeNode(8)
root.left.left =  TreeNode(3)
root.left.left.left = TreeNode(1)

root.right = TreeNode(17)
root.right.left = TreeNode(15)

print(validate_bst(root))