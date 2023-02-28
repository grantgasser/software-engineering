"""
Optimization: max profit

Constraint: w >= capital[i]

capital_to_profits: 

{
    0: [1],
    1: [2,3]
}

w is 0, so take max(capital_to_profits[w]) => 1
- remove that value from array, add to w

1: 
i = 0
w = 0 => 1

2:

{
    0: [],
    1: [2,3]
}

w is 1, so take max(capital_to_profits[w]) => 3

w = 4

-----

k = 3, w = 1, profits = [10,3,2,5], capital = [0,2,1,3]

w == 1, so => 2

w == 3, so => 5

w == 8, so => 10; not just [w], but anything equal to or less than w
- 

{
    0: [10],
    2: [3]
}

look at all keys <= w, find max profit of those, e.g. max([3, 10])

done

-----------------------------------
O(N^2)

k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
"""

"""
BF algorithm, solution is correct, just too slow for large input

I believe its O(N*K)
"""
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        indexes = set([])  # {0, ..}
        for _ in range(k):
            i = 0
            max_profit_per_iteration = 0
            max_idx = None
            while i < len(capital):
                if i not in indexes:  # this should be O(1) check
                    if capital[i] <= w:
                        if profits[i] > max_profit_per_iteration:
                            max_profit_per_iteration = profits[i]
                            max_idx = i
                        
                i += 1

            w += max_profit_per_iteration
            indexes.add(max_idx)
        
        return w
