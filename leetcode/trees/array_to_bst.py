"""
108 Sorted Array to BST

Given an integer array nums where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two 
subtrees of every node never differs by more than one.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Similar solution to 109 Sorted linked list to BST

    Nailed it on the first try :P

    O(N): 56ms, 99.96%
    O(N): 15.7MB, 100.00%
    """
    def build_subtree(self, arr, left, right):
        """Build subtree by exploring left and right halves of array - similar to binary search"""
        if left <= right:
            mid = (left + right) // 2
            root = TreeNode(arr[mid])
            root.left = self.build_subtree(arr, left, mid-1)
            root.right = self.build_subtree(arr, mid + 1, right)
            return root
        else:
            return None
    
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.build_subtree(nums, 0, len(nums) - 1)