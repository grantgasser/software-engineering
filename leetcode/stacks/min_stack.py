"""
155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = float(inf)

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        # if x < min val, reset min val
        self.min_val = min(self.min_val, x)

    def pop(self) -> None:
        popped_val = self.stack.pop()
        
        # because we changed the list, we need to check if min val changed
        if popped_val == self.min_val:
            if self.stack:
                self.min_val = min(self.stack)  # linear
            else:
                self.min_val = float(inf)
            
        return popped_val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # O(1)
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()