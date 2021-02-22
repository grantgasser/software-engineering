"""Really slow"""
def subsets(nums):
    subsets = [set([])]
        
    for n in range(1, len(nums) + 1):
        for sub_idx, _ in enumerate(subsets):
            for num in nums:
                new_sub = set(list(subsets[sub_idx]) + [num])
                
                # slow, but ensures no duplicates
                if new_sub not in subsets:
                    subsets.append(new_sub)
    
    return subsets

print(subsets([1, 2, 3]))


"""
Simple DP solution. Build up/cascade

0: []
1: [] [1]
2: [] [1] [2] [1,2]
3: [] [1] [2] [1,2] [3] [1,3] [2,3] [1,2,3]

O(N * 2^N): 36ms, 58%
O(N * 2^N): 14.4MB, 54% - exactly # of subsets multiplied by number N
of elements in each subset
"""
def fast_subsets1(nums):
    subsets = [[]]
        
    # note the list addition going on
    for num in nums:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [num])
            
        subsets += new_subsets
            
    return subsets


# NOTE: almost, but not quite
def backtrack_subsets(nums):
    # backtracking solution
    subsets = [[]]
    
    # get all subsets of length n
    for n in range(1, len(nums) + 1):
        curr = []
        
        # while first_idx + n is still w/in bounds
        first_idx = 0
        while first_idx <= len(nums) - n:
            idx = first_idx
            
            # while subset size is less than n
            while len(curr) < n:
                #print(f'appending {nums[idx]} to {curr}')
                curr.append(nums[idx])
                #print('after:', curr)
                idx += 1

                # add subset and backtrack
                if len(curr) == n:
                    subsets.append(curr.copy())
                    curr.pop()  # backtrack - careful about the reference!
                    
                    # exhausted all possible subsets of length n
                    if idx >= len(nums):
                        # leave the while loop and go to next first_idx
                        break

            
            first_idx += 1
        
    return subsets

print(backtrack_subsets([1,2,3]))