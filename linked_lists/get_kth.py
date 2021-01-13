"""
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

A more optimal, but less straightforward, solution is to implement this iteratively. We can use two pointers,
p1 and p2. We place them k nodes apart in the linked list by putting p2 at the beginning and moving pi
k nodes into the list. Then, when we move them at the same pace, pi will hit the end of the linked list after
LENGTH - k steps. At that point, p2 will be LENGTH - k nodes into the list, or k nodes from the end.
"""

from linked_list import Node, List

class ListKthLast(List):
    def __init__(self, head):
        super().__init__(head)

    def kth_to_last(self, k):
        """
        Assuming length is unknown, since not given. 
        """
        p1 = self.head
        p2 = self.head 

        # move p2 k spots over
        for i in range(k):
            p2 = p2.next 

        # now move both p1 and p2, k spots apart, to the end
        while p2.next:
            p1 = p1.next
            p2 = p2.next

        return p1.val


head = Node(1)
l = ListKthLast(head)
l.add(2)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l.add(7)
print(l)
print(l.kth_to_last(2))  # expect 5
print(l.kth_to_last(5))  # expect 2
