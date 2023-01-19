# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution(object):
#     def isBalanced(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if not root:
#             return True
        
#         num_left_levels = self.descend(root.left, 1) if root.left else 0
#         num_right_levels = self.descend(root.right, 1) if root.right else 0

#         return abs(num_left_levels - num_right_levels) <= 1


#     def descend(self, node, num_levels):
#         """
#         Descend and accumulate number of levels. If we can go further, keep going, else return value.
#         """
#         if node.left:
#             return self.descend(node.left, num_levels+1)
#         elif node.right:
#             return self.descend(node.right, num_levels+1)
#         return num_levels

"""
2nd, correct solution

Time: O(N) where N is number of nodes
Space: O(H) where H is the height of the tree
    - This is because the maximum number of function calls that are stored on the stack is
    equal to the height of the tree
    - Each call to depth() will add one frame to the stack and each time the function returns it
    will remove one frame from the stack
"""
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.left), depth(node.right))

        if not root:
            return True

        left_depth = depth(root.left)
        right_depth = depth(root.right)

        if abs(left_depth - right_depth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)



# Input: root = [3,9,20,null,null,15,7] => true
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

sol = Solution()
print(sol.isBalanced(tree))

# Input: root = [1,2,2,3,3,null,null,4,4] => false
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(3)
tree.left.left.left = TreeNode(4)
tree.left.left.right = TreeNode(4)

sol2 = Solution()
print(sol2.isBalanced(tree))

# [1,2,2,3,null,null,3,4,null,null,4] => false
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(2)
tree.left.left = TreeNode(3)
tree.right.right = TreeNode(3)
tree.left.left.left = TreeNode(4)
tree.right.right.right = TreeNode(4)

sol3 = Solution()
print(sol3.isBalanced(tree))