# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
128ms, 98%
16.5MB, 9%
"""
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        done = False
        
        # special case, root is null
        if not root:
            root = TreeNode(val)
            return root
        
        # binary search
        while curr:
            if val < curr.val:
                prev = curr
                curr = curr.left
            elif val > curr.val:
                prev = curr
                curr = curr.right
                
        # gone as far as we can, curr is null, insert the new val
        if val < prev.val:
            prev.left = TreeNode(val)
        elif val > prev.val:
            prev.right = TreeNode(val)
            
                    
        return root
                
            
            
        