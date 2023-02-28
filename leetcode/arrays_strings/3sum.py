"""
nums = [-1,0,1,2,-1,-4]

sorted: [-4, -1, -1, 0, 1, 2]

[-1,0,1]

[-1,2,-1]


nums = [4, -2, 0, 1, 1, -4]

sorted: [-4, -2, 0, 1, 1, 4]

[-4, 0, 4]

[-2, 1, 1]
"""

"""O(N^2) solution"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            # Avoid dups of i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # 2-pointer approach
            left, right = i + 1, len(nums)-1
            while left < right:
                summ = nums[i] + nums[left] + nums[right]

                if summ < 0:
                    left += 1
                elif summ > 0:
                    right -= 1
                else: # if 0, we've found one
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # found one, now avoid dups! 
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    # now move on
                    left += 1
                    right -= 1
        return res

