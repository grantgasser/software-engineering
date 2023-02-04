"""

([]) - valid

s: (
s: ([
s: (
s: empty -> valid

([)]

s: (
s: [
we see ")", doesn't match top of stack -> invalid

{[()]}

s: {
s: {[
s: {[(
see ")", match/pop
s: {[
see "]", match/pop
s: {
see "}" match/pop

O(N) where N is len(s)

space -> O(N/2) -> O(N)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        stack = []
        left_parens = ['(', '{', '[']  # linked by index
        right_parens = [')', '}', ']']

        for paren in s:
            if paren in left_parens:
                # Push left paren to stack
                stack.append(paren)
            elif paren in right_parens:
                # Pop and check match
                if stack:
                    popped_paren = stack.pop()
                    if left_parens.index(popped_paren) != right_parens.index(paren):
                        return False
                else:
                    return False
            else:
                raise ValueError('Unknown character')

        return len(stack) == 0 