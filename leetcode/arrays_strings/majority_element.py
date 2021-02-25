"""
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
class Solution:
    """
    Initial idea

    O(N): 39%
    O(N): 52%
    """
    def majorityElement(self, nums: List[int]) -> int:
        # O(N) {3: 2, 2: 1} 
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # O(N) find majority element
        for k, v in freq.items():
            if v > len(nums) // 2:
                return k

    """
    OR
    """
    def majorityElement2(self, nums: List[int]) -> int:
        # O(N) {3: 2, 2: 1} 
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
            # a little faster, less memory as well, but still O(N) and O(N)
            if freq[num] > (len(nums) // 2):
                return num

    """
    O(N) time
    O(1) space

    Walk through the array w/ curr_majority and count and its pretty intuitive
    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    """
    def majorityElement(self, nums: List[int]) -> int:
        curr_majority = nums[0]
        count = 1
        
        for i in range(1, len(nums)):
            if nums[i] == curr_majority:
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    # change curr majority
                    curr_majority = nums[i]
                    count += 1
                    
        return curr_majority
    