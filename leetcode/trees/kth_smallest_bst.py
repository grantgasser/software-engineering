class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
In-order traversal => sorted list of values. Then get kth value.

O(N) time: O(N) for In-order + O(1) for kth value
O(N) space: N recursive calls as well as N values in list
"""
def in_order(root, arr):
    """Perform in-order traversal to get sorted vals"""
    if root.left:
        in_order(root.left, arr)
    arr.append(root.val)
    if root.right:
        in_order(root.right, arr)

def kthSmallest(root: TreeNode, k: int) -> int:
    # NOTE: the array being passed by reference
    sorted_array = []
    in_order(root, sorted_array)
    return sorted_array[k-1]

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.right = TreeNode(3)

print(kthSmallest(root, 1))  # => expect 2


"""
Cheekier leetcode solution
"""
def kthSmallest(self, root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    def inorder(r):
        return inorder(r.left) + [r.val] + inorder(r.right) if r else []

    return inorder(root)[k - 1]


"""
NOTE: we're traversing the tree in sorted order, so why visit all N nodes?

Just stop at the kth node!

Can convert the recursion to iteration w/ a stack
"""
def kth_smallest_stack(root, k):
    """
    The in-order iteration is subtle

    O(H + K) where H is the height of the train: main question: is the tree balanced?
        => worst case, tree is completely unbalanced: O(N + K)
        => best case, tree is balanced: O(log N + K)
    O(H)
        => worst case: O(N), best case: O(log N)
    """
    stack = []
    while True:
        # go left while we can
        while root:
            stack.append(root.val)
            root = root.left

        # "visit" this node
        root = stack.pop()
        k -= 1

        # if we've "visited" k nodes, we're done
        if k == 0:
            return root.val

        # go right to complete the in-order
        root = root.right

kth_smallest_stack(root, 1)