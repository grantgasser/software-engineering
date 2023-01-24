"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

KEY INSIGHT: use `carry` to carry one to the left (same way 9=>0 in decimal)
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0

        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            x = int(a[i]) if i >= 0 else 0
            y = int(b[j]) if j >= 0 else 0

            # carry over and add appropriate digit to result
            added = x + y + carry
            result = str(added % 2) + result

            # carry should be 1 if added is 2
            carry = added // 2

            i -= 1
            j -= 1

        if carry:
            result = "1" + result

        return result