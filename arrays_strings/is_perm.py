"""
1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
"""

def is_perm(s1, s2):
    """
    Qs: Case sensitive? Does whitespace count? 
    """
    if len(s1) != len(s2):
        raise ValueError('s1={} and s2={} need to be the same lengths!'.format(len(s1), len(s2)))

    # O(N) time, O(N) space, 2 hash tables and compare them
    # could assume ascii and do a 128 boolean array

    # BCR seems to be O(N) time

    chars = [0]*128
    for ch in s1:
        chars[ord(ch)] += 1

    for ch in s2:
        idx = ord(ch)
        chars[idx] -= 1

        if chars[idx] < 0:
            return False 

    return True

#print(is_perm('hello', 'car'))
print(is_perm('racecar', 'racecar'))
print(is_perm('car', 'rac'))
print(is_perm('cartoy', 'racyag'))