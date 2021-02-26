"""
Cheeky python quicksort implementation
https://cs231n.github.io/python-numpy-tutorial/
"""
def quicksort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    # more efficient if we just iterate once thru the list but this looks cooler
    left = [x for x in arr if x < pivot]  # put smaller values in left arr
    middle = [x for x in arr if x == pivot]  # pivot value(s) is/are sorted now
    right = [x for x in arr if x > pivot]  # put larger values in right arr

    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))