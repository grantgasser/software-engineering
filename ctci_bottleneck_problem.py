"""
Example: Given an array of distinct integer values, count the number of pairs of integers that
have difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference
k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9) .

Hashing is fast!
"""

# special: [], [x]

# BF, O(N^2)
def k_diff_pairs(arr, k):
    pairs = []
    if len(arr) <= 1:
        return pairs

    if k < 0:
        raise ValueError('k needs to be greater than 0 instead of: {}'.format(k))

    for i, val in enumerate(arr):
        j = i + 1
        while j < len(arr):
            if abs(val - arr[j]) == k:
                pairs.append((val, arr[j]))
            j += 1

    return pairs

print(k_diff_pairs([1,7,5,9,2,12,3], 2))

# smarter: O(N LOG N)
def k_diff_pairs_med(arr, k):
    pairs = []
    if len(arr) <= 1:
        return pairs

    if k < 0:
        raise ValueError('k needs to be greater than 0 instead of: {}'.format(k))

    # sort first O(N LOG N)
    arr_sorted = sorted(arr)

    # binary search to get 2 possible values x and y
    # O(N LOG N)
    # [1, 2, 3, 5, 7, 9, 12]
    for i, v in enumerate(arr_sorted):
        left = i + 1
        right = len(arr_sorted) - 1
         
        while left <= right:
            mid = (left + right) // 2
            target = v + k
            if target < arr_sorted[mid]:
                right = mid - 1
            elif target > arr_sorted[mid]:
                left = mid + 1
            else:
                pairs.append((v, arr_sorted[mid]))
            
    return pairs

# bug lol
#print(k_diff_pairs_med([1,7,5,9,2,12,3], 2))

# fast, O(N) using hash table, so simple (almsot the simplest approach!)
def k_diff_pairs_fast(arr, k):
    pairs = []
    if len(arr) <= 1:
        return pairs

    if k < 0:
        raise ValueError('k needs to be greater than 0 instead of: {}'.format(k))

    # O(N)
    hash_map = {}
    for i, v in enumerate(arr):
        hash_map[v] = i

    # O(N)
    for i, v in enumerate(arr):
        y = v + k
        if hash_map.get(y):
            pairs.append((v, y))

    return pairs

print(k_diff_pairs_fast([1,7,5,9,2,12,3], 2))