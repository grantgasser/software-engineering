"""
Seeing if I can remember how to implement quicksort

[56, 30, 107, 104, 67]

p: 56
left: [30]
right: [107, 104, 67]
"""

import numpy as np

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([56, 30, 107, 104, 67]))

print(quicksort([np.random.randint(100) for _ in range(10)]))