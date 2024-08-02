"""
10 Python Tips and Tricks: https://www.youtube.com/watch?v=C-gEQdGVXbk
"""

# 1 ternary conditionals, can be more concise and improve readability
condition = True
x = 1 if condition else 0
print(x)


# 2 large numbers, can use _ in place of commas
num1 = 10_000_000_000
num2 = 100_000_000
total = num1 + num2
print(f'{total:,}')


# 3 using 'with' context manager
# don't need to remember to close file
with open('test.txt') as f:
    contents = f.read()

# use context managers for threads, or DB connections
# any time you're manually managing resources


# 4 enumerate() takes another argument
# if you don't want to start at 0! :)
names = ['Jane', 'John', 'Walter White', 'Barney']
for i, name in enumerate(names, start=1):
    print(i, name)


# 5 loop over multiple lists in parallel using zip
names = ['Peter', 'Clark', 'Wade', 'Bruce']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

# don't use enumerate and use same index, instead use zip!
# zip returns a tuple
for name, hero in zip(names, heroes):
    print(f'{name} is actually {hero}')

# > 2 lists
universes = ['Marvel', 'DC', 'Marvel', 'DC']
for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

# if diff lengths, zip will stop at end of shortest list
short_list = ['foo', 'bar']
for short, name in zip(short_list, names):
    print(short, name)


# 6 Unpacking
# normal
items = (1, 2)
a, b = items

# OR
a, _ = items

# vars must be == to number of vals to unpack, unless use *
a, b, *c = (1, 2, 3, 4, 5)
print(a, b, c)

# or if don't want them
a, b, *_ = (1, 2, 3, 4, 5)


# 7 getting and setting attributes on object
class Person():
    pass

person = Person()
person.first = 'John'
person.last = 'Deere'
print(person.first, person.last)

# what if we want to use the value of a variable to be the attribute name?
first_key = 'first'  # so we want to create an attribute: person.first
first_val = 'Jane'

# use setattr()
person2 = Person()
setattr(person2, first_key, first_val)
print(person2.first)

# want to get attributes? say you want to loop over attributes: getattr()
person_info = {'first': 'Chuck', 'last': 'Norris'}
person3 = Person()
for key, val in person_info.items():
    setattr(person3, key, val)
print(person3.first, person3.last)

# we know what the keys (attributes) are, how to get the values? now use getattr()
for key in person_info.keys():
    print(getattr(person3, key))


# 8 inputting secret information

# use getpass()
from getpass import getpass
username = input('Username: ')
#password = input('Password: ')  # Bad! you can see the input in the console
password = getpass('Password: ')
print('Logging in...')


# 9 terminal stuff


# 10 use built in help
"""
>>> import smtpd
>>> help(smtpd)

or if you don't need as much info, just want methods and attributes
>>> from datetime import datetime
>>> dir(datetime)

is "today" a method in datetime
>>> datetime.today
<built-in method today ... >
>>> datetime.today()
datetime.datetime(2020, ...)
"""
