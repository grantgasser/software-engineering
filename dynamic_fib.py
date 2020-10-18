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


print(dyn_fib(8))