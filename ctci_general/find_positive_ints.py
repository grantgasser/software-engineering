"""
Find all positive integer solutions under 1000 to a^3 + b^3 = c^3 + d^3

BF: check all combinations of 1000 (1000^4 = 1,000,000,000,000, 1 trillion)

Better: do half - 1000*1000 = 1,000,000

a = 2, b = 3, c, d

c = 2, d = 3, then a and b will be same as c and d from the above^ iteration
"""

def brute_force(limit=1000):
    