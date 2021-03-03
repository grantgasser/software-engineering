"""
215. Kth Largest Element in an Array
Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
"""
def findKthLargest(nums, k):
    """
    Time: O(N log N)
    Space: ?? list.sort() is an "in-place" sorting algo, but if it uses
        mergesort then doesn't it use extra memory?
    """
    nums.sort()
    return nums[-k]


import heapq
def find_kth_largest(nums, k):
    """
    heapify: arr=>heap O(N), https://docs.python.org/3/library/heapq.html#heapq.heapify

    Get kth largest O(k)

    Time: O(N) to make heap, O(K Log N) to get kth largest (you know which level it is,
        you just have to search the whole level)
        => O(N + K log N)
    Space: O(N) space
    """
    return heapq.nlargest(k, nums)[-1]

    
print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))