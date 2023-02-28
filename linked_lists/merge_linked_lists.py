"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = dummy = ListNode()
        ptr1, ptr2 = list1, list2

        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                curr.next = ListNode(ptr1.val)
                curr = curr.next
                ptr1 = ptr1.next
            else:
                curr.next = ListNode(ptr2.val)
                curr = curr.next
                ptr2 = ptr2.next

        curr.next = ptr1 if ptr1 else ptr2

        return dummy.next

        
