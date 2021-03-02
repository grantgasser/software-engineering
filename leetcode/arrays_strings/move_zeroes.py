def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.

    Solution is simple, just take a minute or two to think through it
    O(N) time
    O(1) space
    """
    # key: last_nonzero_idx should be equal to number of nonzero elements after this loop
    last_nonzero_idx = 0
    for num in nums:
        if num != 0:
            nums[last_nonzero_idx] = num
            last_nonzero_idx += 1
            
    # fill out the rest of the arr w/ zeroes
    # since these values were already moved to the front
    while last_nonzero_idx < len(nums):
        nums[last_nonzero_idx] = 0
        last_nonzero_idx += 1

    return nums

print(moveZeroes([0, 1, 0, 3, 12]))