"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        idx = -1
        while digits[idx] == 9:
            digits[idx] = 0

            idx -= 1

            # check if we're furthest to the left 
            # i.e. list is all 9s and we need to increase number of digits by adding 1
            if idx < -len(digits):
               digits = [1] + digits
               return digits 

        digits[idx] += 1

        return digits