"""
70. Climbing Stairs - SAME AS recursive_and_dp/triple_step.py from CTCI
Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def __init__(self):
        self.ways = 0
    
    def climbStairs(self, n: int) -> int:
        self.climb_helper(n)
        return self.ways
    
    def climb_helper(self, target):
        if target == 0:
            # increment ways
            self.ways += 1
            return
            
        elif target > 0:
            for i in [1, 2]:
                self.climb_helper(target-i)
                
        elif target < 0:
            # went too far, backtrack
            return
            
            
"""
ex n = 2

c(2)
    c(1)
        c(0)
        self.ways += 1
        return
        c(-1)
        return
    c(0)
        self.ways += 1
        return
        
        
        2
    0       1
        0
        
This recursive solution is inefficient, does duplicate work!
Note c(0) is called twice.

O(2^N)

        3
    1           2
        0   0       1

Store in cache/memoization/DP
"""

"""
Cleaner Recursive solution, based on similar problem in CTCI
"""
def climb_helper(self, target):
    # base case
    if target < 0:
        return 0
    elif target == 0:
        return 1
    else:
        return self.climb_helper(target-1) + self.climb_helper(target-2)


"""
DP solution: With almost no help!

O(N) time and space

32ms, 56%
14MB, 48%
"""
class Solution:    
    def climbStairs(self, n: int) -> int:
        # memo[i] will contain how many ways to get to i using 1,2 steps
        memo = [0]*(n+1)
        self.climb_helper(n, memo)
        return memo[n]
        
    def climb_helper(self, target, memo):
        
        # base case
        if target < 0:
            return 0
        elif target == 0:
            return 1
        elif memo[target] != 0:
            return memo[target]
        else:
            memo[target] = self.climb_helper(target-1, memo) + self.climb_helper(target-2, memo)
            return memo[target]
        
    """
    []
    c(3) => 3  
        c(2) => 2
            c(1) => 1
                c(0) => 1
                
                c(-1) => 0
            
            c(0) => 1
            
        c(1) => 1, don't go down here bc its already stored!
            c(0)
            
            c(-1)
            
            
    c(2)
    """