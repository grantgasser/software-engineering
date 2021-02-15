"""
46. Permutations
Medium

Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order

nPk = n! / (n-k)!

Time: BCR seems to be N! since we need to generate N! combinations
O(N^2 * (N-1)!): 40ms, 72%

Space: N! permutations, each w/ N elements
O(N * N!): 14.4MB, 47%
"""
from copy import copy, deepcopy

def permute(nums):
    permutations = [[nums[0]]]

    # O(N)
    for insert_num_idx in range(1, len(nums)):

        # iterate thru existing subarrays, O((N-1)!)
        new_permutations = []
        for subarray in permutations:
            j = 0
            # iterate thru subarray, O(N)
            while j < len(subarray) + 1:
                # get copy so as to not change original subarray that we're iterating thru
                new_subarray = copy(subarray)

                # insert new number (insert_num) at each possible location w/in subarray
                new_subarray.insert(j, nums[insert_num_idx])

                # append new subarray with inserted num into a new list of permutations
                new_permutations.append(new_subarray)
                j += 1

            # replace old permutations with new list of permutations
            permutations = copy(new_permutations)

    return permutations

print(permute([1,2,3]))  # 3! = 6
print(len(permute([1,2,3, 4])))  # 4! = 24 subarrays/permutations
