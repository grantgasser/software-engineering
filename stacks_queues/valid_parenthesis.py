"""
stack:

['(']

')' pop

ex2
['(']
['']


ex n:
'([])' or ''

['(', '[']

']', ['(', '['] => ['(']
-------------------------------
O(N) Runtime: 48 ms, faster than 37.33% of Python3 online submissions for Valid Parentheses.
O(N) Memory Usage: 13.9 MB, less than 70.33% of Python3 online submissions for Valid Parentheses.

"""
class Solution:
    def isValid(self, s: str) -> bool:
        string_stack = ''
        opens = ['(', '{', '[']
        closes = [')', '}', ']']
        
        for char in s:
            # append an opening to stack
            if char in opens:
                string_stack += char
              
            else:
                # otherwise, close a pair
                i = closes.index(char)
                if string_stack and string_stack[-1] == opens[i]:
                    string_stack = string_stack[:-1]
                else:
                    return False
            
        return True if not string_stack else False
            
            