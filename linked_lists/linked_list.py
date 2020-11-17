# base node class
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# base list class
class List(object):
    def __init__(self, head):
        self.head = head

    def add(self, val):
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = Node(val)

    def __repr__(self):
        rep = ''
        curr = self.head
        while curr:
            rep += '->'
            rep += str(curr.val)
            curr = curr.next

        rep += '->NULL'
        return rep