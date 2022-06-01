"""
Trapping Rain Water

[2, 0, 2] => 2

[3, 0, 2, 0, 4] => 7
[0, 3, 1, 3, 0].sum() => 7

optimal:
[0, 3, 3, 3, 3] - left inclusive (compute left to right)
[4, 4, 4, 4 ,0] - right inclusive (compute right to left)

[0, 3, 3, 3, 0] - [3, 0, 2, 0, 4] = 0 + 3 + 1 + 3 = 7 

[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] => 6
[0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0] => 6

https://www.geeksforgeeks.org/trapping-rain-water/
"""

# O(N^2) time
# O(1) space
def max_water(arr):
  water = 0

  i = 1
  while i < len(arr) - 1:
    left_max = max(arr[:i])
    right_max = max(arr[i+1:])

    min_of_maxes = min(left_max, right_max)

    water += max(min_of_maxes - arr[i], 0) 

    i += 1

  return water


print(max_water([2, 0, 2]))
print(max_water([3, 0, 2, 0, 4]))
print(max_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# O(N) time
# O(N) space
# store max_left arrays, max_right, take min, 
def max_water2(arr):
  water = 0
  max_left = [0]*len(arr)
  max_right = [0]*len(arr)

  # populate max lefts
  for i in range(1, len(arr)):
    max_left[i] = max(max_left[i-1], arr[i-1])

  # populate max rights
  for i in range(len(arr)-2, -1, -1):
    max_right[i] = max(max_right[i+1], arr[i+1])

  # get min of left and right max at i - then see if its > than arr[i]
  for i in range(1, len(arr)-1):
    water += max(min(max_left[i], max_right[i]) - arr[i], 0)

  return water

print('-'*50)
print(max_water2([2, 0, 2]))
print(max_water2([3, 0, 2, 0, 4]))
print(max_water2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

# O(N) time
# O(1) space
# instead of max left/right arrays, just  
def max_water2(arr):
  water = 0
  max_left = [0]*len(arr)
  max_right = [0]*len(arr)

  # populate max lefts
  for i in range(1, len(arr)):
    max_left[i] = max(max_left[i-1], arr[i-1])

  # populate max rights
  for i in range(len(arr)-2, -1, -1):
    max_right[i] = max(max_right[i+1], arr[i+1])

  # get min of left and right max at i - then see if its > than arr[i]
  for i in range(1, len(arr)-1):
    water += max(min(max_left[i], max_right[i]) - arr[i], 0)

  return water

print('-'*50)
print(max_water2([2, 0, 2]))
print(max_water2([3, 0, 2, 0, 4]))
print(max_water2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))