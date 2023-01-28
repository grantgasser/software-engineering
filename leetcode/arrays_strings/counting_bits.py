"""
338 Counting Bits

Given an integer n, return an array ans of length n + 1 such 
that for each i (0 <= i <= n), ans[i] is the number of 1's in 
the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

"""

"""
Could likely use binary number properties to make more efficient

This solution is O(N * len)
"""
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]*(n+1)

        for i in range(n+1):
            binary_str = str(bin(i))
            result[i] += binary_str.count('1')
        
        return result