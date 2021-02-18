"""
Tedious code with weird conditions

Because nums has distinct elements, binary search can be expected to work in log N time.

O(log N)
O(1)
"""
def search(nums, target):
    # case of short arrays
    if len(nums) <= 3:
        if target in nums:
            return nums.index(target)
    
    # weird binary search
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        
        # if left and right are right next to each other
        if right - left == 1:
            if target == nums[right]:
                return right
            elif target == nums[left]:
                return left
            else:
                break
        
        mid = (left + right) // 2
        
        # usual binary search conditions, but with some sub-conditions
        if nums[mid] > target:
            # if pivot not in left side (i.e. normal increasing)
            if nums[left] < nums[mid]:
                # if target is between left and mid
                if nums[left] < target:
                    # go left
                    right = mid - 1
                elif nums[left] > target:
                    # go right
                    left = mid + 1
                else:
                    return left
            else:
                # pivot is in left side, so we know we'll get to target, go left
                right = mid - 1
            
        elif nums[mid] < target:
            # if pivot not in right side (i.e. normal increasing)
            if nums[right] > nums[mid]:
                # if target is between mid and right
                if nums[right] > target:
                    # go right
                    left = mid + 1
                elif nums[right] < target:
                    # go left
                    right = mid - 1
                else:
                    return right
            else:
                # pivot is in right side so we know we'll get to target, go right
                left = mid + 1
        else:
            return mid
        
    return -1

print(search([5, 1, 2, 3, 4], 1))