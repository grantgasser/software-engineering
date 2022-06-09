"""
https://leetcode.com/problems/merge-k-sorted-lists/

BF:

traverse:
[1, 4, 5, 1, 3, 4, 2, 6]

sort:
[1, 1, 2, 3, 4, 5, 6]

build linked list:
1=>1=>2=>...

If N is all the elements 
    Time: -> O(N + N log N) -> O(N log N)
    Space: -> O(N)


More optimal:
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKListsBF(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # BRUTE FORCE
        merged_list = []
        
        # If list is empty
        if not lists:
            return
        
        # Convert array of linked lists to one array
        for root in lists:
            while root:
                merged_list.append(root.val)
                root = root.next
                
        # If there were null nodes
        if not merged_list:
            return
                
        # Sort
        sorted_merged_list = sorted(merged_list)
        
        # Build return linked list
        root = ListNode(sorted_merged_list[0])
        node = root
        for x in sorted_merged_list[1:]:
            node.next = ListNode(x)
            node = node.next
            
        return root
    
    
    """
    Divide & Conquer - similar merging to mergeSort
    
    [[1,4,5],[1,3,4],[2,6]]
    
    merge([1, 4, 5], [1, 3, 4])
        res = [1], l = [4, 5], r = [1,3,4]
        res = [1,1], l = [4,5], r = [3,4]
        res = [1,1,3], l = [4,5], r = [4]
        res = [1,1,3,4], l = [5], r = [4]
        res = [1,1,3,4,4], l = [5], r = []
        
        return res = [1,1,3,4,4,5], ...
        
        6 iters to merge 6 elements
        NOTE: if one is empty (stop checking both and just fill out with the remaining array)
        
    
    merge([1,1,3,4,4,5], [2,6])
        res = [1]
        res = [1,1]
        res = [1,1,2]
        res = [1,1,2,3]
        res = [1,1,2,3,4]
        res = [1,1,2,3,4,4]
        res = [1,1,2,3,4,4,5]
        
        return res = [1,1,2,3,4,4,5,6]
        
        8 iters to merge 8 elements
        
    14 iters total
    k = 3 lists, N = 8
    
    guess: (k-1)N or O(kN) - probably should do more analysis on this
        
        
    [[1,2], [4, 6, 8], [1, 3, 6, 7], [2, 9], [1,8], [2,5,11]]
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        
        # The O(k) part
        result = lists[0]
        for linked_list in lists[1:]:
            if result and linked_list: 
                result = self.mergeHelper(result, linked_list)
            elif result and not linked_list:
                result = self.mergeHelper(result, None)
            elif not result and linked_list:
                result = self.mergeHelper(None, linked_list)
            
        return result
        
        
    # The O(N) part - returns merged & sorted array of left and right   
    def mergeHelper(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        curr_result = None
        
        # While not at end of either linked lists
        while left and right:
            if left.val <= right.val:
                if not curr_result:
                    curr_result = ListNode(left.val)
                    result = curr_result
                else:
                    curr_result.next = ListNode(left.val)
                    curr_result = curr_result.next
                    
                # Move to next node of left
                left = left.next
                
            else:
                if not curr_result:
                    curr_result = ListNode(right.val)
                    result = curr_result
                else:
                    curr_result.next = ListNode(right.val)
                    curr_result = curr_result.next
                    
                # Move to next node of right
                right = right.next
                
        # At this point we've finished 1 linked list, need finish the other
        while left:
            curr_result.next = ListNode(left.val)
            left = left.next
                
        while right:
            curr_result.next = ListNode(right.val)
            right = right.next
                
        
        return result