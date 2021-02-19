"""
109. Convert Sorted List to Binary Search Tree
Medium

Given the head of a singly linked list where elements are sorted in ascending order, 
convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which 
the depth of the two subtrees of every node never differ by more than 1.

GOOD PROBLEM!
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Solution 1:
    O(N log N) time: iterate thru all half-lists, N/2 + (2 * N/4) + (4 * N/8) + (8 * N/16) .. 
        => 2^(i-1) + N/2^i from i = 1 to log N (bc cutting in half)
        => which reduces to 2^-1 * N = N/2 from i = 1:log N which means we N things N log N times = O(N log N) 
    O(log N): log N recursive calls
    """
    def find_middle(self, head):
        # slow and fast ptr technique (1x and 2x: when 2x is at end, 1x is at middle)
        prev = None
        runner1 = head
        runner2 = head
        
        while runner2 and runner2.next:
            prev = runner1
            runner1 = runner1.next
            runner2 = runner2.next.next
            
        # prev ptr used to disconnect left sublist from right sublist
        if prev:
            prev.next = None
            
        return runner1
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # if list is empty, invalid case, not the base case
        if not head:
            return None
        
        # find middle, which is end of left list and next to begin of right list
        middle = self.find_middle(head)
        
        # create subtree with root and left and right subtrees
        root = TreeNode(middle.val)
        
        # base case: 1 element in list
        if head == middle:
            return root
        
        # how do we ensure call to f(head) doesnt just find the same middle value again?
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(middle.next)
        
        return root


"""
Can optimize further by trading space for time.

Convert to array which is O(N) space and then run binary search on array

O(N) time: O(N) to convert to array. Accessing mid is O(1) so not necessarily a BST
O(N) space

GOOD TRY BUT DIDN'T PASS, TWEAK A BIT
"""
def convert_linked_list_to_array(head):
    ptr = head

    arr = []
    while ptr:
        arr.append(ptr.val)
        ptr = ptr.next

    return arr 

def binary_search(arr, left, right):
    mid = (left + right) // 2

    #while left <= right:
    if left >= right:
        return None

    # create root with middle value     
    root = TreeNode(arr[mid])

    # create left and right subtrees
    root.left = binary_search(arr[left:mid], left, mid-1)
    root.right = binary_search(arr[mid:], mid, right)
    
    return root

def convert_linked_list_to_BST(head):
    # convert list to array
    arr = convert_linked_list_to_array(head)

    return binary_search(arr, 0, len(arr)-1)