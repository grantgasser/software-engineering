"""
CTCI CH 1: Arrays, Strings, Hash Tables 

Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

idea 1: hash table (or just a array of boolean values corresponding to ASCII encoding 
which uses less memory than chars)

idea 2: for each letter, check every other letter - O(N^2), but at least doesn't use additional data structure
"""

# idea 1; using array of bools is a bit more space efficient than hash table (not in terms of complexity tho, still O(1))
chars = [False]*128
chars[ord('a')] = True
print(chars)

# idea 2:
def is_unique(test):
    for i, c in enumerate(test):
        j = i + 1
        while j < len(test):
            if test[i] == test[j]:
                return False
            j += 1

    return True

print(is_unique('blah'))
print(is_unique('blahh'))

""""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.

If assuming ASCII, could use an array of bools instead of dictionary to be our hash table
that keeps track of char frequencies
"""
s1 = 'tree' # {t: 1, r: 1, e: 2}
s2 = 'teer' # {t: 1, r: 1, e: 2}

# Time: O(max(s1, s2)), Space: O(max(s1, s2))
def is_perm(s1, s2):
    hash_map1 = {}
    for s in s1:
        hash_map1[s] = hash_map1.get(s, 0) + 1

    hash_map2 = {}
    for s in s2:
        hash_map2[s] = hash_map2.get(s, 0) + 1

    for k in hash_map1.keys():
        if hash_map1[k] != hash_map2[k]:
            return False

    return True
    
print(is_perm(s1, s2))
print(is_perm('hello', 'helio'))
    
