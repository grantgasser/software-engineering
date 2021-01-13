"""
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.

FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

"""
With buffer:

O(N) time, O(N) space

init buffer. iterate thru list

if dup:
    del node
else:
    add to buffer
""" 

"""
W/o buffer:

brute force way. for each node, iter through list and check if dup; O(N^2)

OR

total time: O(N LOG N)

sort first (O(N LOG N))

O(N)
iterate
    if prev == curr:
    del one of them
"""
from linked_list import Node, List

class ListRemoveDup(List):
    def __init__(self, head):
        super().__init__(head)

    # with buffer
    def remove_dup1(self):
        """
        Time: O(N), Space: O(N)
        """
        vals = {}
        curr = self.head
        prev = curr  # runner 
 
        while curr.next:
            val = vals.get(curr.val)
            if val is not None:
                # remove curr
                prev.next = curr.next
                curr = curr.next 
            else:
                # keep track of values we've seen
                vals[curr.val] = 1
                prev = curr
                curr = curr.next

    # w/o buffer 
    def remove_dup2(self):
        """
        Time: O(N^2), Space: O(1)
        """
        slow = self.head 

        while slow:
            fast = slow
            while fast and fast.next:
                # duplicate
                if slow.val == fast.next.val:
                    fast.next = fast.next.next
                fast = fast.next
            slow = slow.next


head = Node(1)
l = ListRemoveDup(head)
l.add(2)
l.add(2)
l.add(3)
l.add(4)
print(l)
l.remove_dup1()
print(l)
l.add(4)
l.add(5)
print(l)
l.remove_dup2()
print(l)
l.add(3)
print(l)
l.remove_dup2()
print(l)


