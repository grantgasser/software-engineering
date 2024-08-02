"""Article: https://codesignal.com/blog/interview-prep/example-codesignal-questions/"""

# Question 1
def manipulate(arr):
    new_arr = [None for _ in arr]
    for i, num in enumerate(arr):
        prev = 0 if i < 1 else arr[i-1]
        next = 0 if i >= len(arr) - 1 else arr[i+1]

        new_arr[i] = prev + num + next

    return new_arr

print(manipulate([4, 0, 1, -2, 3]))


# Question 2
def pattern_match(pattern, source):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_matches = 0

    i = 0
    while i < len(source):
        j = 0
        while j < len(pattern) and (i+j) < len(source):
            if pattern[j] == "0" and source[i+j] not in vowels:
                break
            if pattern[j] == "1" and source[i+j] in vowels:
                break

            j += 1

        # If rule has not been violated, record a match
        if j == len(pattern):
            num_matches += 1

        i += 1

    return num_matches

print(pattern_match("010", "amazing"))
print(pattern_match("100", "codesignal"))
print(pattern_match("1000", "hawaii"))
print(pattern_match("001", "iamthegreatest"))
print(pattern_match("1", "iamthegreatest"))
print(pattern_match("0", "iamthegreatest"))


# Question 3 - PASSES TESTS IN JUPYTER NOTEBOOK (question3.ipynb)
# def solution(field, figure):

#     # Loop across
#     col = 0
#     while col <= len(field[0]) - 3:
#         print('\ncol:', col)
#         # Loop down
#         row = 0
#         while row <= len(field) - 3:
#             # print('row:', row)
#             # print('blocked:', is_blocked(row, col, field, figure))

#             # If we have a full row - success
#             if is_row_full(row, col, field, figure):
#                 return col

#             # If the figure is blocked and cannot go further down
#             if is_blocked(row, col, field, figure):
#                 #print('breaking')
#                 break

#             row += 1

#         col += 1

#     return -1


# def is_blocked(curr_row, curr_col, field, figure):
#     figure_bottom_row = figure[-1]
#     next_row = field[curr_row + 3][curr_col:curr_col+3]

#     print('bottom row:', figure_bottom_row)
#     print('next row:', next_row)

#     for fig_val, field_val in zip(figure_bottom_row, next_row):
#         if fig_val + field_val == 2:
#             return True
        
#     return False

# # import numpy as np

# def is_row_full(curr_row, curr_col, field, figure):
#     figure = np.array(figure)
#     field = np.array(field)

#     # Overlay the figure on the field
#     field[curr_row:curr_row+3, curr_col:curr_col+3] = field[curr_row:curr_row+3, curr_col:curr_col+3] + figure

#     # Check if there is a row with all 1s
#     if np.all(field == 1, axis=1).sum(): 
#         return True
    
#     return False
    

# field = [[0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [1, 1, 0, 1, 0],
#           [1, 0, 1, 0, 1]]

# figure = [[1, 1, 1],
#           [1, 0, 1],
#           [1, 0, 1]]

print('\nQuestion 3:')
# print(solution(field, figure))  # couldn't switch to right env, see jupyter notebook


# Question 4 - Lookup Table
# O(N^2 * log(max(N)))
def get_num_pairs(numbers):
    num_pairs = 0

    # Edge case
    if len(numbers) == 0: return num_pairs
    elif len(numbers) == 1: return 1 if check_power_of_2(numbers[0]) else num_pairs

    # O(N^2) loop thru each pair
    i = 0
    while i < len(numbers):
        j = i
        while j < len(numbers):
            num_pairs += 1 if check_power_of_2(numbers[i] + numbers[j]) else 0
            j += 1
        i += 1

    return num_pairs


def check_power_of_2(value):
    # O(log(max(N)))
    while value >= 1:
        # If we get to 1, we know it's a power of 2
        if value == 1:
            return True

        # If resulting value is not divisible by 2, definitely is not a power -> stop early
        if value % 2 != 0:
            return False

        value /= 2

    return False

print('\nQuestion 4')
print(get_num_pairs([1, -1, 2, 3]))
print(get_num_pairs([2]))
print(get_num_pairs([-2, -1, 0, 1, 2]))
    