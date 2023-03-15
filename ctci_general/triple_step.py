"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs.

num_ways = [0, 0, 0, 0, 0, 0]

say we want to know num_ways[n] or num_ways[5]

num_ways[5] = num_ways[4] + num_ways[3] + num_ways[2]

aka f(n) = f(n-1) + f(n-2) + f(n-3) which of course can be done recursively, but is O(3^N)!

[1, 2, 4]
"""
def count_ways(n):
    ways = [-1]*(n+1)
    ways[0] = 1
    ways[1] = 1
    ways[2] = 2

    if n <= 1: return ways[n]

    else:
        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2] + ways[i-3]

        return ways[n]
    
print(count_ways(3))
print(count_ways(4))
print(count_ways(5))



