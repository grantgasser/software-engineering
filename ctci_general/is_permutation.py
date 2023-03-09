"""Check if 2 strings are permutations of each other"""

# 'a' => 56
# 'z' => 78

"""O(N) time, O(N) space where N = len(s1) = len(s2)"""
def is_permutation(s1, s2):
    # Can't be permutations if diff length
    if len(s1) != len(s2): return False

    #char_count = [0]*128  # Assumption

    # Create a count map
    concat = s1 + s2
    max_ord = ord(max(concat))
    min_ord = ord(min(concat))
    char_count = [0]*(max_ord - min_ord + 1)


    # Count freq of chars in s1 (could also do a freq_map = {} thing, but this more efficient)
    for c in s1:
        char_count[ord(c) - min_ord] += 1

    # Subtract each time we see char in s2, if we go below 0 they're not permutations
    for c in s2:
        char_count[ord(c) - min_ord] -= 1

        if char_count[ord(c) - min_ord] < 0:
            return False
    
    return True


print(is_permutation("foot", "foto"))
print(is_permutation("hannah", "hannah"))
print(is_permutation("one", "seventy"))
print(is_permutation("gal", "lag"))
print(is_permutation("top", "tap"))