"""
Rotate NxN matrix 90 degrees.

Trick:

1. Transpose

2. Reverse rows ([::-1])

Ex. 

1 2 3
4 5 6
7 8 9

=>

1 4 7
2 5 8
3 6 9

=>

7 4 1
8 5 2
9 6 3
"""

# assuming nxn
def rotate_matrix(arr):
    n = len(arr)

    # 1. Transpose: remember that by definition, transposition is swapping of the indexes
    for i in range(n):
        for j in range(i, n):
            print(i, j)
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 2. Reverse
    for i in range(n):
        arr[i] = arr[i][::-1]

    return arr

print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))