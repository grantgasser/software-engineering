"""
Write a method to replace all spaces in a string with '%20:

input: "Mr John Smith    "
output: "Mr%20John%20Smith"
"""

"""Pythonic"""
def urlify(s):
    return s.strip().replace(' ', '%20')

print(urlify("Mr John Smith    "), '<eol>')

def urlify2(s):
    pass