"""
48 Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.


        90 degree rotation trick

        * 1 2 3     7 8 9     7 4 1
        * 4 5 6  => 4 5 6  => 8 5 2
        * 7 8 9     1 2 3     9 6 3

        0,0 => 0,0
        1,0 => 0,1
        2,0 => 0,2
        """
        # Swap upside down
        for i in range(len(matrix)//2):
            for j in range(len(matrix)):
                first_val = matrix[i][j]
                second_val = matrix[len(matrix)-i-1][j]

                matrix[i][j] = second_val
                matrix[len(matrix)-i-1][j] = first_val

        # Swap symmetrical (n-i)
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                first = matrix[i][j]
                second = matrix[j][i]

                matrix[i][j] = second
                matrix[j][i] = first


