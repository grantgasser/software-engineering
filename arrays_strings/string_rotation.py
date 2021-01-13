"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").
"""

# def rotate_string(s1, s2):
#     assert len(s1) == len(s2)

#     # get prefix of s2 (i.e. find the rotation point, axis)
#     prefix = ''
#     i, j = 0, 0
#     while i < len(s2):
#         if s2[i] != s1[j]:
#             prefix += s2[i]
#         else:
#             break

#         i += 1

#     print(prefix)

#     # or is_substr(); append pref to end of remainder of s2, should be equal to s1
#     append_to_end = s2[i:] + prefix 

#     if s1 == append_to_end:
#         return True
#     else:
#         return False
    
# print(rotate_string('erbottlewat', 'waterbottle'))
# #print(rotate_string('foo', 'bart'))
# print(rotate_string('falogreatwhitebuf', 'greatwhitebuffalo'))  # bad assumption

# NOTE: rotation? just add s1 + s1 and see if s2 is in the result
def rotate_string2(s1, s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False

    # O(N) if assume 'in' runs in O(A + B) where A = len(s2)
    s1s1 = s1 + s1
    print(s1s1)

    if s2 in s1s1:
        return True
    else:
        return False

print(rotate_string2('waterbottle', 'erbottlewat'))