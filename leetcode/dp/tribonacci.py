"""
1137. N-th Tribonacci Number

Like fib but previous 3 not 2

O(N) dynamic programming solution
"""
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        tribonacci = [0, 1, 1]

        for i in range(3, n+1):
            tribonacci.append(tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3])
        
        return tribonacci[n]