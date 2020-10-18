def combinationSum(candidates, target):
    """My attempt. Good try, Close."""
    combinations = []
    
    # empty
    if not candidates:
        return combinations
    
    if target == 0:
        return combinations

    
    # DFS where each candidate is the root
    for i, v in enumerate(candidates):
        stack = [v]
        
        current_total = 0
        curr_combo = []
        equal_to_target = False
        
        while stack:
            curr = stack.pop()
                
            # test
            if (current_total + curr) < target:
                # good
                current_total += curr
                curr_combo.append(curr)
                
                # add children
                for j, v2 in enumerate(candidates):
                    stack.append(v2)
                
            elif (current_total + curr) == target:
                # good, but done
                current_total += curr
                curr_combo.append(curr)
                equal_to_target = True    
                
                # break because we're done
                break
                
            else:
                # bad, go somewhere else
                continue
                
        if curr_combo and equal_to_target and curr_combo not in combinations:
            combinations.append(curr_combo)
                
            
    
    return combinations


def backtracking(res, v, candidates, target, curr):
    if target == 0:
        # V.COPY() ! 
        res.append(v.copy())
        return

    if target < 0:
        return

    else:
        i = curr 
        while i < len(candidates):
            if candidates[i] <= target:
                v.append(candidates[i])
                backtracking(res, v, candidates, target - candidates[i], i)
                v.pop()
            else:
                break
            i += 1

def combo_sum_backtracking(candidates, target):
    """
    Backtracking converted from C++
    
    Close but maybe a bug. Don't have time.
    """
    res = []
    v = []
    backtracking(res, v, sorted(candidates), target, 0)
    return res

def main():
    print(combo_sum_backtracking([2,3,6,7], 7))
main()