"""
8.1 Triple Step: A child is running up a staircase with n steps and 
can hop either 1 step, 2 steps, or 3 steps at a time. 
Implement a method to count how many possible ways the child can 
run up the stairs.

Might be easy to start w/ inefficient recursive soln before moving
on to DP.
"""

# O(3^N), exp like fibonacci
def triple_step(n):
    # think about last step, similar to fib
    if n < 0:
        return 0
    elif n == 0:
        return 0
    else:
        return triple_step(n-1) + triple_step(n-2) + triple_step(n-3)

def dp_triple_step(n):
    memo = [-1] * n
    return dp(n, memo)

def dp(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = dp(n-1, memo) + dp(n-2, memo) + dp(n-3, memo)
        return memo[n]

# NOTE: even w/ memoization, this will overflow at a number like 37