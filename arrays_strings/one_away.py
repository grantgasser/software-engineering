"""
1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.

Like edit_dist < 1
"""

def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    # hashmap for both, iterate thru and count differences: O(max(len(s1), len(s2))) time, O(N) space  
    s1_chars = [0]*128 #97, 101, 108, 112
    for ch in s1:
        s1_chars[ord(ch)] += 1

    s2_chars = [0]*128 #97, 98, 101, 108
    for ch in s2:
        s2_chars[ord(ch)] += 1

    # compare
    i = 0
    diff = 0
    while i < 128:
        diff += abs(s2_chars[i] - s1_chars[i])

        if diff > 2:
            return False
        i += 1
    
    return True

print(one_away('pale', 'ple'))
print(one_away('pales', 'pale'))
print(one_away('pale', 'bale'))
print(one_away('pale', 'bake'))
print(one_away('hello', 'hi'))
print(one_away('falt', 'fart'))