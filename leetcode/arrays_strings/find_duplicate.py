def findDuplicate(nums):
    """
    First idea: hash table and check dups
    
    O(N) time, O(N) space, doesn't modify nums
    """
    hash_map = {}
    for num in nums:
        if hash_map.get(num):
            return num
        else:
            hash_map[num] = hash_map.get(num, 0) + 1


def find_duplicate(nums):
    """
    Sort (in-place)

    Time: O(N log N)
    Space: O(1)?? list.sort() is an "in-place" sorting algo, but if it uses
        mergesort then doesn't it use extra memory?
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return nums[i]

print(find_duplicate([1, 3, 4, 2, 2]))
        