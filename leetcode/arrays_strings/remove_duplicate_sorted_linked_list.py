"""
83. Remove Duplicates from Sorted List
Easy

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Ex1 
Input: head = [1,1,2]
Output: [1,2]

Ex2
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

    def delete_duplicates(self, head: ListNode) -> ListNode:
        """
        O(N): 40ms, 82%
        O(1): 14.3MB, 30%
        """
        if not head or not head.next:
            return head
        
        # linear search w/ 2 running pointers (prev and curr)
        prev = head
        curr = head.next
        while curr:
            # delete curr if same as prev
            if curr.val == prev.val:
                prev.next = curr.next
                curr.next = None  # may not be necessary
                
                # move curr along
                curr = prev.next  # (prev.next used to be curr.next)
                
            else:
                # move both pointers along if not the same val
                prev = prev.next
                curr = curr.next
                
        return head
