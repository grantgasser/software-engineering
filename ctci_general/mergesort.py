"""
Trying to see if I can remember merge sort - divide & conquer

[38, 27, 43, 3, 9, 82, 10]

left half:
[38, 27, 43, 3] [9, 82, 10]

    [38, 27] 
        [38] [27] 
    
    [43, 3]
        [43] [3]

    merge([27, 38], [3, 43]) -> [3, 27, 38, 43]

right half: 
    [9, 82]
        [9, 82]

    [10]
        [10]

    merge([9, 82], [10]) -> [9, 10, 82]

merge([3, 27, 38, 43], [9, 10, 82]) -> [3, 9, 10, 27, 38, 43, 82]
"""

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    # Split arrays
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recurse all the way down to one element each
    left_merged = mergesort(left)
    right_merged = mergesort(right)

    # Actual merge logic
    sorted_array = merge(left_merged, right_merged)
    return sorted_array

def merge(left, right):
    merged = []

    # Merge two arrays into a resulting sorted array
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Missed these lines in 1st implementation
    # We know left and right are independently sorted, so if there are remaining values
    # we can jsut append them to the result
    merged += left[i:]
    merged += right[j:]
    
    return merged

print('Test merge:', merge([3, 27, 38, 43], [9, 10, 82]))
print('\nTest mergesort:', mergesort([38, 27, 43, 3, 9, 82, 10]))
