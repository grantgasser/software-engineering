# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        
        locs = {1: head}
        length = 1
        curr = head
        
        # count and store nodes based on location
        while curr.next:
            curr = curr.next
            length += 1
            locs[length] = curr
            
        # rotate
        rotate = k % length
        if not rotate:
            return head
        
        # new tail node
        new_last_node_idx = length - rotate
        locs[new_last_node_idx].next = None
        
        # re-assign previous last node
        locs[length].next = head
        
        # return new head
        return locs[new_last_node_idx + 1]