"""
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

TODO

Can't you just have p1 and p2? Send p2 to end of list. 
Then loop while comparing p1 and p2 as they both move towards the middle?
This would be O(N) time and O(1) space.
    => Because its not doubly linked! No reference to previous nodes.
"""

from linked_list import Node, List

class ListPalindrome(List):
    def __init__(self, head):
        super().__init__(head)

    def get_reverse_list(self, node):
        # TODO


    def is_equal(self, list1_node, list2_node):
        while list1_node and list2_node:
            if list1_node.val != list2_node.val:
                return False
            
            # advance
            list1_node = list1_node.next
            list2_node = list2_node.next

        return not (list1_node and list2_node)

    def is_palindrome(self):
        """
        Solution #1: Reverse and Compare
        """
        reverse_list = self.get_reverse_list()
        return self.is_equal(self.head, reverse_list)


head = Node(0)
l = ListPalindrome(head)
l.add(1)
l.add(2)
l.add(1)
l.add(0)
print(l)

#print(l.is_palindrome())  # expect 5