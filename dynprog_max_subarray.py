"""
Max SubArray (Dynamic Programming Problem)

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Use Kadane's Algo!

The logic to solve this problem is same as "max subarray problem" using Kadane's Algorithm. 
"""

# very subtle! code is simple but idea is hard to grasp
# O(N)
def maxProfit(prices):
    max_curr = 0
    max_so_far = 0
    
    i = 1
    while i < len(prices):
        # (prices[i] - prices[i-1]) is today's difference, so new_max_curr is max_curr combined
        # w/ today's difference
        new_max_curr = max_curr + (prices[i] - prices[i-1])
        max_curr = max(0, new_max_curr)
        
        max_so_far = max(max_so_far, max_curr)
        
        i += 1
        
    return max_so_far

# expect 5
print(maxProfit([7,1,5,3,6,4]))