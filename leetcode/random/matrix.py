"""
Leetcode 74
"""
test = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3

def search2d(matrix, target):
    found = False
        
    # O(m x n)
    # for row in matrix:
    #     for val in row:
    #         if val == target:
    #             found = True
    #             break
    
    # special case: empty
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return found            
    
    # kind of binary search
    for row in matrix:
        start_idx = 0
        end_idx = len(row) - 1

        # side cases
        if len(row) == 1:
            return row[0] == target

        if target >= row[start_idx] and target <= row[end_idx]:
            while start_idx < end_idx - 1:
                # binary search on this row
                mid_idx = (end_idx - start_idx) // 2
                print('mid:', mid_idx, 'val:', row[mid_idx])
                # have we found it?
                if target == row[mid_idx]:
                    found = True
                    break

                elif target < row[mid_idx]:
                    end_idx = mid_idx - 1

                else:
                    start_idx = mid_idx + 1
                    
    return found

    
print(search2d(test, target))

test2 = [[1]]
print(search2d(test2, target))
