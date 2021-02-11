"""
Max SubArray (Dynamic Programming Problem)

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Use Kadane's Algo!

The logic to solve this problem is similar to "max subarray problem" using Kadane's Algorithm. 

Similar to Leetcode 53, but difference is the answer can be negative in 53, here you just dont buy/sell and get 0
"""

# very subtle! code is simple but idea is hard to grasp
# O(N)
def maxProfit(prices):
    max_curr = 0  # note max_curr is anchored at 0, won't go below
    max_so_far = 0
    
    i = 1
    while i < len(prices):
        # (prices[i] - prices[i-1]) is today's difference, so new_max_curr is max_curr combined w/ today's difference
        # i.e. 8 = 5 + 3 OR -2 = 5 + -7
        new_max_curr = max_curr + (prices[i] - prices[i-1])

        # did adding today's price diff keep us above 0? if not, set to 0, else set new
        # i.e. 8 = max(0, 8) OR 0 = max(0, -2)
        max_curr = max(0, new_max_curr)  # key: stay >= 0 
        
        max_so_far = max(max_so_far, max_curr)  
        
        i += 1
        
    return max_so_far

# expect 5
print(maxProfit([7,1,5,3,6,4]))  # diff = [-6, 4, -2, 3, -2]