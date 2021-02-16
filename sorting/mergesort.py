"""
Implement Mergesort

https://www.youtube.com/watch?v=4VqmGXwpLqc
"""

# [2, 8, 5, 3, 9, 4, 1, 7]

def mergesort(array):
    """Halve the array - divide step"""
    # base case: array of 1 element: [2], [8], [5], ...
    if len(array) == 1:
        return array

    # divide current arrays in half
    array1 = array[:len(array)//2]
    array2 = array[len(array)//2:]

    # recursive call on division step
    array1 = mergesort(array1)
    array2 = mergesort(array2)

    # merge [2] and [8], merge [5] and [3] etc. then back up the stack
    # merge [2, 8] and [3, 5], etc.
    return merge(array1, array2)

def merge(array1, array2):
    """Merge two arrays - conquer/merge step"""
    array3 = []

    # while array1 and array2 still have elements
    while array1 and array2:
        if array1[0] < array2[0]:
            array3.append(array1[0])
            array1.pop(0)
        else:
            array3.append(array2[0])
            array2.pop(0)

    # at this point, either array1 and array2 are empty

    # while array1 still has elements
    while array1:
        array3.append(array1[0])
        array2.pop(0)

    # while array2 still has elements
    while array2:
        array3.append(array2[0])
        array2.pop(0)

    return array3

print(mergesort([2, 8, 5, 3, 9, 4, 1, 7]))