"""
509. Fibonacci Number
Easy


44ms, 43%
14MB, 91%
"""
class Solution:
    # O(N) time and O(N) space
    def fib(self, n: int) -> int:
        memo = [0]*(n+1)
        self.fib_helper(n, memo)
        return memo[n]
    
    def fib_helper(self, n, memo):
        if n == 0:
            return 0
        elif n == 1:
            memo[n] = 1
            return memo[n]
        elif memo[n] > 0:
            return memo[n]
        else:
            memo[n] = self.fib_helper(n-1, memo) + self.fib_helper(n-2, memo)
            return memo[n]

    # didn't perform much better but its O(N) time and O(1) space
    def fib_simpler(self, n: int) -> int:
        # try to do it with just remembering last 2 values, doesn't even need to be recursive
        if n == 0: return 0
        elif n == 1: return 1
        
        # start a and b at 0 and 1
        a, b = 0, 1
        
        # only need 2 previous values (a and b), c is the current fib value
        i = 1
        while i < n:
            c = a + b
            a = b
            b = c
            
            i += 1
            
        return c