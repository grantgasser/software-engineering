"""
2.6 Palindrome: Implement a function to check if a linked list is a palindrome.

TODO
"""

from linked_list import Node, List

class ListPalindrome(List):
    def __init__(self, head):
        super().__init__(head)

    def get_reverse_list(self):
        curr = self.head 

    def is_equal(self, list1, list2):
        return False

    def is_palindrome(self):
        """
        Solution #1: Reverse and Compare
        """
        reverse_list = self.get_reverse_list()
        return self.is_equal(self.head, reverse_list)