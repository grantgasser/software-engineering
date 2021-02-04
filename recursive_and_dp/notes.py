"""
Recursive solutions, by definition, are built off of solutions to subproblems. Many times, this will mean
simply to compute f (n) by adding something, removing something, or otherwise changing the solution
for f(n -1) . In other cases, you might solve the problem for the first half of the data set, then the second
half, and then merge those results.

Bottom Up: start with simple case, like 1 element, then solve for
2 elements, then for 3 and so on. BUILD solution for one case off of
the previous case (or multiple previous cases)

Top-Down: divide the problem for case N into subproblems

Half-and-Half: divide data set in half
    => Binary search
    => Merge sort

Recursive vs. Iterative: recursive can be very space inefficient.
Each call adds layer to stack (O(n)) for n calls.

Usually better to do iteratively, but sometimes simpler to do recursive.

Discuss tradeoffs of recursive vs. iterative w/ interviewer!
"""

"""
Dynamic Programming & Memoization

Dynamic programming is mostly just a matter of taking a recursive algorithm and finding the overlapping
subproblems (that is, the repeated calls). You then cache those results for future recursive calls.\

So remove the redundancy (repeated calls) by storing results
"""


"""
DRAWING recursive tree is great way to figure out runtime
9 calls when n = 4, 15 calls when n = 5

                    4
            3               2
        2       1       1       0
    1       0       

Each parent has 2 children, except leaf nodes
so O(2^N), O(2^4) in this case
a little bit better than that (O(1.6) actually, but still exponential)

anyway, its O(2^N)!
"""
def recursive_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fib(n-1) + recursive_fib(n-2)

# dynamic (O(N))
def fib(n):
    return dp_recursive(n, [0]*(n+1))

def dp_recursive(n, memo):
    # base case, also val is same as idx
    if n == 0 or n == 1:
        memo[n] = n
        return n

    if memo[n] == 0:
        memo[n] = dp_recursive(n-1, memo) + dp_recursive(n-2, memo)
    
    # end
    return memo[n]

# start w/ fib(1) and fib(0), then use those to compute fib(2)
# no recursion here
def dp_bottom_up(n):
    if n == 0 or n == 1:
        return n

    memo = [0] * n 
    memo[0] = 0
    memo[1] = 1

    i = 2
    while i < n:
        memo[i] = memo[i-1] + memo[i-2]
        i += 1

    return memo[n-1]

print(dp_bottom_up(10))

# or even simpler, dont need a list!
def dp_simple(n):
    if n == 0:
        return 0

    a = 0
    b = 1
    i = 2
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1

    return c

print(dp_simple(10))

"""
See leetcode/climbing_stairs.py, fibonacci.py
"""