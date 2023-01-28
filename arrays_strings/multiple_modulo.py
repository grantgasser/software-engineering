"""
You are given an array of integers a and an integer k. Your task is to calculate the number of ways to pick two different indices i < j, such that a[i] + a[j] is divisible by k.

Example

For a = [1, 2, 3, 4, 5] and k = 3, the output should be solution(a, k) = 4.

There are 4 pairs of numbers that sum to a multiple of k = 3:

a[0] + a[1] = 1 + 2 = 3
a[0] + a[4] = 1 + 5 = 6
a[1] + a[3] = 2 + 4 = 6
a[3] + a[4] = 4 + 5 = 9
"""

"""O(N^2), too slow"""
def solution(a, k):
    num_pairs_divisible = 0

    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if (a[i] + a[j]) % k == 0:
                num_pairs_divisible += 1
    return num_pairs_divisible
    