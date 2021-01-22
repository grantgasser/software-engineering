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

# NOTE: key takeaway is that in-order traversal of BST should be sorted!

from binary_tree import TreeNode

"""My first attempt"""
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

"""Solution 1 from CTCI"""
def copyBST(root, array):
    """In-order => array. O(N) where N is # of nodes"""
    if not root:
        return

    copyBST(root.left, array)
    array.append(root.data)  # do work in middle since in-order
    copyBST(root.right, array)

def is_sorted(array):
    """Check if array is sorted. O(N)"""
    idx = 0
    while idx < len(array) - 1:
        if array[idx] >= array[idx+1]:
            return False
            print('Not sorted! at idx=', idx)
        idx += 1
    return True

def solution1(root, array):
    """
    In-order, copy elements to array, then check to see if array is sorted.

    Takes up extra memory. ASSUMPTION: no duplicates in tree

    Time: O(N), Space: O(N)
    """
    copyBST(root, array)
    print(array)
    is_valid_bst = is_sorted(array)
    return is_valid_bst


"""But don't need array! Can do in-order search and keep track of previous node to compare"""


root = TreeNode(9)
root.left = TreeNode(6)
root.left.right = TreeNode(8)
root.left.left =  TreeNode(3)
root.left.left.left = TreeNode(1)

root.right = TreeNode(17)
root.right.left = TreeNode(15)

print('My soln:', validate_bst(root))
print()

# solution 1: in-order => array => sorted?
print('\nSolution 1:')
array = []
print(solution1(root, array))

print('check case: 8 => 11')
array = []
root.left.right = TreeNode(11)
print(solution1(root, array))