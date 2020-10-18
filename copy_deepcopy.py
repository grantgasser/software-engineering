# shallow copy and deepcopy in Python
# https://www.programiz.com/python-programming/shallow-deep-copy
from copy import copy, deepcopy

# Example using = operator
old_list = [1, 2, 3, 4, 'a']
new_list = old_list

new_list[4] = 5

print('Old list:', old_list)
print('Old list Id:', id(old_list))

print('New list:', new_list)
print('New list Id:', id(new_list))

# Shallow copy
print('\nShallow Copy:')
old_list = [1, 2, 3, 4]
new_list = copy(old_list)
print('old list:', old_list)
print('new_list:', new_list)

# add to original, new_list is not changed! 
print('\nadding to the original object changes only the original')
old_list.append(5)
print('old list:', old_list)
print('new_list:', new_list)

# same in nested case
print('\nsame deal for nested case')
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy(old_list)
old_list.append([4, 4, 4])
print("Old list:", old_list)
print("New list:", new_list)

# change original (so change [1,2,3,4])
print('\nchanging object inside original object changes both the original and copy')
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy(old_list)
old_list[1][1] = 'AA'
print("Old list:", old_list)
print("New list:", new_list)

# but doesn't change if not "nested" (i.e. objects within objects)
print('\ndoesnt change both if not nested objects')
old_list = [1, 2, 3, 4]
new_list = copy(old_list)
old_list[1] = 99
print("Old list:", old_list)
print("New list:", new_list)

# DeepCopy - completely independent! Probably safest
print('\nDeep Copy:')
print('even if nested, changing object w/in original object doesnt change the copy')
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = deepcopy(old_list)
old_list[1][0] = 'BB'
print("Old list:", old_list)
print("New list:", new_list)

# Clarification: shallow and deep differences only relevant for Objects within Objects
# hence the 2D lists in the examples, otherwise shallow copy should be sufficient
"""
https://docs.python.org/3/library/copy.html

The difference between shallow and deep copying is only relevant 
for compound objects (objects that contain other objects, like lists or class instances):

    A shallow copy constructs a new compound object and then (to the extent possible) 
    inserts references into it to the objects found in the original.

    A deep copy constructs a new compound object and then, recursively, 
    inserts copies into it of the objects found in the original.
"""