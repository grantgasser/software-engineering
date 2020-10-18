def search(nums, target):
    """
    Ugly because the damn special case
    
    Runtime: 240 ms, 83%
    Memory Usage: 15 MB
    """
    idx = -1
    
    # cases: n = 1
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1
    
    # init indexes
    left = 0
    right = len(nums) - 1
    
    # binary search
    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    
    return idx

print(search([-1,0,3,5,9,12], 9))

# C++ 
"""
Runtime: 76 ms, 84%
Memory Usage: 28 MB
"""
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int idx = -1;
        
        // special case
        if (nums.size() == 1){
            if (nums[0] == target)
                return 0;
            else
                return -1;
        }
        
        // init
        int left = 0;
        int right = nums.size() - 1;
        
        // binary search
        while (left <= right){
            int mid = (left + right) / 2;
            if (target < nums[mid])
                right = mid - 1;
            else if (target > nums[mid])
                left = mid + 1;
            else
                return mid;
        }
        
        
        return idx;
    }
};