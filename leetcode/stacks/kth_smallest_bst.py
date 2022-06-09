# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Store in array as we go along?

[5, 3, 2, 1] return arr[arr.len-k] => 3

[3, 1] return arr[arr.len-k] => 1

                15
        12              20
    8       14      17      24
5       10              19

k = 5, 14 

LNR traversal: [5, 8, 10, 12, 14]

if arr.len == k: return arr[-1]


Key: LNR is a way to transform BST into sorted array!
"""

# iterative
class Solution:
    def __init__(self):
        self.sorted_vals = []
    
    # time: O(N)
    # space: O(N)
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
#         def in_order(node):
#             return in_order(node.left) + [node.val] + in_order(node.right) if node else []
        
#         return in_order(root)[k-1]

    # using a stack 
    """
    [5, 3, 2, 1] => pop() 3 times => 3
    
    [3, 1] => pop() one time => 1
    
    
    [15, 12, 8, 5] => pop 5, k = 4
    [15, 12, 8, 10] => add right
    
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in order traversal add to stack as we go along, then pop when percolating up
        stack = []
        while True:
            # go left while we can
            while root:
                stack.append(root)
                root = root.left

            # "visit" this node
            root = stack.pop()
            k -= 1

            # if we've "visited" k nodes, we're done
            if k == 0:
                return root.val

            # go right to complete the in-order
            root = root.right