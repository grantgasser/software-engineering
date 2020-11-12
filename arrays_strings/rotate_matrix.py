"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
Hints: #51, #100
"""

"""
1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3

-------
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
"""

def rotate_matrix(M):
    """
    Assumptions: rotate right 90 deg., if list, its 2D
    """
    if not M:
        raise ValueError('Matrix needs to be a 2d List')

    N = len(M)
    if N != len(M[0]):
        raise ValueError('matrix needs to be NxN, not {}x{}'.format(len(M), len(M[0])))

    # could do even more input validation..

    # rotate 90 degrees; do circular rotation layer by layer, starting on outer layer
    # O(N^2), best we can do since we have to touch all N^2 elements
    num_layers = N // 2
    for layer in range(num_layers):
        first = layer
        last = N - 1 - layer 
        for i in range(first, last):
            # offset, in both horiontal and vertical directions
            offset = i - first

            top = M[first][i]

            # left -> top
            M[first][i] = M[last-offset][first]

            # bottom -> left
            M[last-offset][first] = M[last][last-offset]

            # right -> bottom
            M[last][last-offset] = M[i][last]

            # top -> right
            M[i][last] = top 

    return M

#print(rotate_matrix([[1, 2, 5], [1, 2, 3]]))
print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # correct
print(rotate_matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])) # correct