import re

"""
findall()	- Returns a list containing all matches
search()	- Returns a Match object if there is a match anywhere in the string
split()	    - Returns a list where the string has been split at each match
sub()       - Replaces one or many matches with a string
"""

test = "hello world 10"
print(re.findall("llo", test))

# Metacharacters
print(re.findall("h..lo", test))  # any character except \n
print(re.findall("he.{2}o", test)) # exactly 2 occurences
print(re.findall("world|universe", test)) # either/or
print(re.findall("^he", test)) # starts with
print(re.findall("9$", test)) # ends with

# Special Sequences
print(re.findall("\d", test))  # find all digits
print(re.findall("\D", test)) # NO digits
print(re.findall("\s", test)) # white space

# Sets
print(re.findall("[aeiou]", test)) # ONE of the chars are present
print(re.findall("[^aeiou]", test))  # any char EXCEPT
print(re.findall("[a-j]", test))  # anything in between alphabetically

# Can do the same with digits: [0123], [0-9]

"""
searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned
"""
print(re.search("[a-j]", test))  # returns a Match object
x = re.search("[a-d]", test)
print(x.start())  # finds 'd' at index 10

txt = "The rain in Spain"
x = re.search("Portugal", txt)  # returns None if no match
print(x)

"""
The split() function returns a list where the string has been split at each match
"""
txt = "The rain in Spain"
x = re.split("\s", txt)  # split at each whitespace char, returns a list
print(x)

x = re.split("\s", txt, 1)  # split at just the first occurence
print(x)