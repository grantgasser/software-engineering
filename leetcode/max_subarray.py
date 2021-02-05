"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

Solution Discussion:
https://www.youtube.com/watch?v=5WZl3MMT0Eg

NOTE: key point is to ignore negative "prefixes" (not all neg. values, just prefixes)
but, ironically, if you want max contiguous subarray, its ok to go down in value, just don't go negative
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, curr_sum = nums[0], nums[0]
iterate.... if prefix (i.e. curr_sum) is negative, curr_sum = max(0, num)
update max_sum

think of sliding windows, right pointer is iterating 1 by 1, left pointer is
moving over to the right to avoid negatives
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]

# O(N). OK I was able to code it up given the above explanation
def max_subarray(nums):
    max_sum = nums[0]
    prefix = nums[0]

    i = 1
    while i < len(nums):
        if prefix < 0:
            prefix = max(0, nums[i])  # key
        else:
            prefix += nums[i]

        # update max so far
        #print(prefix)
        max_sum = max(max_sum, prefix)
        i +=1

    return max_sum

print(max_subarray(nums))


# same exact solution but cleaner, though not as easy to understand
def max_subarray2(nums):
    i = 1
    while i < len(nums):
        if nums[i-1] > 0:  # is prefix positive? okay add it to curr list element (which will be the prefix for next element!)
            nums[i] += nums[i-1]
        i += 1
    return max(nums)

print(max_subarray2(nums))


"""
NOTE: O(N^2) solution exceeded time limit

Looks incorrect, don't waste time though
"""
from numpy import inf
def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    
    # O(N^2) - iterating thru all possible subarrays
    max_sum = float(-inf)
    for i, val in enumerate(nums):
        curr_sum = val
        max_sum = max(max_sum, curr_sum)
            
        # iterate thru remaining values after i
        j = i + 1
        while j < len(nums):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
            j += 1
            
    return max_sum

print(maxSubArray(nums))