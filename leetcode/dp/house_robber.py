"""
nums = [2,7,9,3,1]

init loot = [0, 2]

i = 2
loot[i] = max(loot[i-2] + nums[i-1], loot[i-1]) = max(7, 2)
loot = [0, 2, 7]

i = 3
loot[i] = max(2 + 9, 7) = 11
loot = [0, 2, 7]

i = 4
loot[i] = max(7 + 3, 11) = 11
loot = [0, 2, 7, 11]

i = 5
loot[i] = max(11 + 1, 11) = 12
loot = [0, 2, 7, 11, 12]
"""
# O(N) time, O(N) space
# could make it O(1) space by keeping track of prev
class Solution:
    def rob(self, nums: List[int]) -> int:
        loot = [0, nums[0]]
        
        # we go up to i = len(nums) because we need to consider the possibility of robbing
        # the last house
        for i in range(2, len(nums)+1):
            loot.append(max(loot[i-2] + nums[i-1], loot[i-1]))
        
        return loot[-1]
        