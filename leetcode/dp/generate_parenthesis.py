"""
This was round 2 C3 question.

22. Generate Parentheses
Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
# n = 1, ()
# n = 2, (()), ()()  so wrap and append to end
# n = 3, ((())), ()(()), (())(), (()()), ()()()

"""
The real pattern is this:

(1) generate pair: ()
(2) generate 

O(N^2?): 24ms, 99%
O(N^2): 14.7MB, 40%
"""
# NOTE: see worksheet for this
def generate_parenthesis(n):
    # i.e. if n == 2, [[][][]]
    dp = [[] for i in range(n+1)]
    dp[0].append('')

    for i in range(n+1):  # 0-n
        for j in range(i):
            dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]

    return dp[n] 


print(generate_parenthesis(3))