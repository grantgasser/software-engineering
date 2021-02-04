"""
We define a harmonious array as an array where the difference between its maximum 
value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious 
subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by 
deleting some or no elements without changing the order of the remaining elements.


Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2

Example 3:
Input: nums = [1,1,1,1]
Output: 0

Time: 19%
Space: 66%
"""

# REVIEW: really elegant O(N) solution
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # TODO: input validation
        
        max_length = 0
        
        # create frequency map (or use collections.Counter())
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
        # look at num occurences of pairs that are distance 1 away
        for num in nums:
            if freq.get(num-1, 0) > 0:
                # NOTE: don't forget to utilize functions like min/max/abs/etc
                max_length = max(max_length, freq[num] + freq[num-1])
                
            if freq.get(num+1, 0) > 0:
                max_length = max(max_length, freq[num] + freq[num+1])
                
        return max_length