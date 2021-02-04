"""
5 common Python mistakes

https://www.youtube.com/watch?v=zdJEYhA2AZQ
"""


# 1) mixing up tabs and spaces (editor should avoid this problem)
# maybe use pylint to catch errors like this
nums = [11, 30, 44, 54]

for num in nums:
    square = num**2
    print(square)


# 2) Name conflicts
# 2a) don't name your module the same as a module you're trying to import
# => if you get an import error, could be path issue or naming issue
from math import radians, sin  # don't name file math.py
rads = radians(90)
print(sin(rads))

# 2b) dont name vars same as func, like so:
# radians = radians(90)
# rad45 = radians(45)
# print(rad45)

# MAIN INSIGHT: 3 Mutable default arguments (be careful)
def add_employee(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

emps = ['John', 'Jane']

add_employee('Corey', emps)  # works fine

# but..
add_employee('Corey')
add_employee('John')  # => ['Corey', 'John'], not as expected!

# you would think it would create a NEW empty list each call
# NOpe! default args are evaluated once when the func is defined!
# not each time its called!
# don't notice this w/ immutable data types, but w/ mutable data
# types like a list, you have this problem

# solution:
def add_employee(emp, emp_list=None):
    if not emp_list:
        emp_list = []
    emp_list.append(emp)
    print(emp_list)

add_employee('Corey')
add_employee('John')

# similar idea of args being evaluated when func is defined
import time
from datetime import datetime

def display_time(time=datetime.now()):
    print(time.strftime('%B %d, %Y, %H:%M:%S'))

display_time()
time.sleep(1)
display_time()

# 4 Iterator (Zip)
names = ['Peter', 'Clark', 'Wade', 'Bruce']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# zip returns iterator (much more efficient, doesn't return all values at once), not list
identities = zip(names, heroes)

print(identities)
for ident in identities:
    print(ident[0], ident[1])

# nothing left once you've already "used" the generator 
# can only access value at one time!
print(list(identities))

# 5 Asterisks (bad practice when doing imports, yup)
from os import *

rename('test.txt')
remove('test.txt')

# hard to debug, where did rename() come from? 

from html import *
from glob import * 

# html and glob both have escape()!
print(help(escape))