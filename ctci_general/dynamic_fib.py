# recursive, O(2^N) fib
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(7))

# dynamic fibonacci, O(N)
def dyn_fib(n):
    memo = [0 for x in range(n)]
    
    for i in range(n):
        dyn_fib2(i, memo)

    return memo[-1]
    
def dyn_fib2(n, memo):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif memo[n] > 0:
        return memo[n]

    memo[n] = dyn_fib2(n - 1, memo) + dyn_fib2(n - 2, memo)

# even simpler
def dyn_fib3(n):
    # base case
    if n == 0: return 0
    elif n == 1: return 1

    memo = [None] * n 
    memo[0] = 0
    memo[1] = 1

    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]

    return memo[i-1] + memo[i-2]

# even better, don't have to store a table! just the last #, it builds off itself
def dyn_fib4(n):
    # base case
    if n == 0: return 0
    elif n == 1: return 1

    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c

    return c


print(dyn_fib(8))
print(dyn_fib3(8))
print(dyn_fib4(8))