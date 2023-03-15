"""
Turn sorted array into bst

[2, 4, 5, 8, 11, 16, 21, 24]

                11
        5               21
    4       8               24
2
    

[2, 4, 5, 8, 11, 16, 21]

                8
        4               16
    2       5       11      21 
        
"""

arr1 = [2, 4, 5, 8, 11, 16, 21, 24]
arr2 = [2, 4, 5, 8, 11, 16, 21]

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None


def array_to_bst(arr, left_idx, right_idx):
    mid = (left_idx + right_idx) // 2

    root = Node(arr[mid])

    root.left = array_to_bst(arr, left_idx, mid - 1)
    root.right = array_to_bst(arr, mid + 1, right_idx)

    return root

print(array_to_bst(arr1, 0, len(arr1)-1))
print(array_to_bst(arr2, 0, len(arr2)-1))