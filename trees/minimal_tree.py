"""
4.2 Minimal Tree: Given a sorted (increasing order) array with unique integer elements, 
write an algorithm to create a binary search tree with minimal height.
"""

# [2, 4, 5, 9, 13, 18]
"""
     5
  2    13
    4 9   18
"""
from binary_tree import TreeNode

def minimal_tree(arr, lo=0, hi=None):
    # basically just binary search here, time: O(N), space: O(N)
    if hi < lo:
        return None

    mid = (hi + lo) // 2
    print(arr[mid])

    root = TreeNode(arr[mid])
    root.left = minimal_tree(arr, lo, mid - 1)  # left
    root.right = minimal_tree(arr, mid + 1, hi)  # right

    return root

def get_min_tree(arr):
    return minimal_tree(arr, 0, len(arr)-1)


arr = [2, 4, 5, 9, 13, 18]
tree = get_min_tree(arr)
print(tree)
    