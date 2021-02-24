"""
347. Top K Frequent Elements
Medium

Similar questions: 
    - https://leetcode.com/problems/top-k-frequent-words/
    - and 451, see frequency_sort.py

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
def topKFrequent(self, nums, k):
    """
    Hash table and sort by value.

    O(N Log N): 50%
    O(N): worst case is all values in nums are unique, 77%
    """
    # O(N)        
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        
    # O(N log N): worse case is all values in nums are unique
    sorted_keys = sorted(freq, key=freq.get, reverse=True)
    
    return sorted_keys[:k]


from collections import Counter
import heapq
def topk_heap(nums, k):
    """
    Create hash table then create heap w/ k elements, giving us topk

    O(N log K)
    O(N + K) 
    """
    # O(1)
    if k == len(nums):
        return nums

    # hash table
    freq = Counter(nums)

    # create heap of k elements, basically sort k elements then return result: O(N log K)
    # https://docs.python.org/3/library/heapq.html#heapq.nlargest
    # equivalent result: sorted(iterable, key=key, reverse=True)[:k] (though not equivalent in time complexity)
    return heapq.nlargest(k, freq.keys(), key=freq.get)

print(topk_heap([1, 1, 1, 2, 2, 3], 2))


def topk_bucket(nums, k):
    """
    https://leetcode.com/problems/top-k-frequent-elements/discuss/740374/Python-5-lines-O(n)-buckets-solution-explained

    1) Create list of empty lists as buckets to store nums w/ frequencies 1, 2, ... n
    2) Iterate thru nums and store frequencies in hash table
    3) Iterate thru hash table and add nums to their respective buckets based on their frequencies
    4) Get last k values in list of buckets 
        => either concat all lists into 1 big list or iterate until we've gotten k values

    O(N) time: slower on submission but better time complexity so ohh well - they must not have tested it much
    O(N) space
    """
    # 1) O(N)
    buckets = [[] for _ in range(len(nums))]
    
    # 2) O(N)
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # 3) O(N) - worst case is all nums are unique
    for num, freq in freq.items():
        buckets[freq-1].append(num)

    # 4) O(k) - get last k nums which correspond to nums w/ highest frequency
    outer_idx = len(buckets) - 1
    topk = []
    while len(topk) < k:
        for num in buckets[outer_idx]:
            topk.append(num)

        outer_idx -= 1

    return topk

print(topk_bucket([1, 1, 1, 2, 2, 3], 2))