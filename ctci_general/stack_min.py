"""
Design a stack with push, pop, and min() that all are O(1)

eg.

push(5) => {5}, mins = [5]

push(6) => {6, 5}, mins = [5]

push(3) => {3, 6, 5}, mins = [3,5]

push(1) => {1, 3, 6, 5}, mins = [1,3,5]

# push(9) => {9, 1, 3, 6, 5}, mins = [1, 3, 5]

case: if you pop the min, must find new min
- but remember pop has to be O(1)

pop() => {3, 6, 5}, mins = [3, 5]

pop() => {6, 5}, mins = [5]

pop() => {5}, mins = [5]


for pop():
time: O(1)
space: O(N) bc we store prev mins
"""

class Stack:
    def __init__(self):
        self.s = []
        self.mins = []

    def push(self, val):
        self.s.append(val)

        # Update min if necessary
        if not self.mins or self.get_min() > val:
            # Push to mins stack (no need for a method)
            self.mins.append(val)

    def pop(self):
        if self.s:
            # Remove the top from stack
            top = self.s.pop()

            # If the top was a min, remove that min as well
            if top == self.mins[-1]:
                self.mins.pop()
        else:
            raise IndexError('Cannot remove from empty stack.')

    def get_min(self):
        return self.mins[-1]
    

stack = Stack()

stack.push(5)
print(stack.s)
stack.push(6)
print(stack.s)
stack.push(3)
print(stack.s)
print('min:', stack.get_min())
stack.push(1)
print(stack.s)
print('min:', stack.get_min())
stack.pop()
print(stack.s)
print('min:', stack.get_min())
stack.pop()
print(stack.s)
stack.pop()
print(stack.s)
stack.pop()
print(stack.s)

# Error
stack.pop()