"""
O(N)
O(1)
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first_idx = 0
        second_idx = len(s) - 1
        
        while first_idx < second_idx:
            temp = s[first_idx]
            s[first_idx] = s[second_idx]
            s[second_idx] = temp
            
            first_idx += 1
            second_idx -= 1