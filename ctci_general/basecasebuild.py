"""
CTCI Base Case and Build Technique

Example: Design an algorithm to print all permutations of a string. For simplicity, assume all characters
are unique.
Consider a test string abcdefg.
Case "a" --> {"a"}
Case " ab" --> {"ab", "ba"}
Case "abc" --> ?
"""

# O(?)

def perm_helper(ch, perms_list):
    new_list = []

    for perm in perms_list:
        pos = 0
        while pos <= len(perm):
            new_str = ''
            new_str += perm[:pos]
            new_str += ch
            new_str += perm[pos:]
            new_list.append(new_str)

            pos += 1

    return new_list

def permutations(s):
    perms = ['']
    for ch in s:
        perms = perm_helper(ch, perms)

    return perms

# works! 
print(perm_helper('c', ['ab', 'ba']))
print(permutations('abcd'))
print(len(permutations('abcd')))  # expect 4P4 = 24
print(len(permutations('abcdefg')))  # expect 7P7 = 5040