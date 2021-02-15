"""
1.1 
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Assuming ASCII, could store in array of bools where index i is ascii val instead of hash table
"""

# w/ additional data structure: O(N) Time, O(1) space (only 26 characters)
def is_unique(s):
    chars = {}

    for ch in s:
        if chars.get(ch) is not None:
            return False

        chars[ch] = chars.get(ch, 0) + 1
        
    return True

print(is_unique('hello'))
print(is_unique('car'))
print(is_unique('foobar'))

# w/ no extra data structure: O(N LOG N) time, O(1) space
# so sacrifice some time for saving that space
def is_unique2(s):
    # sort first: O(N LOG N)
    # sorts in place, maintains O(1) space
    s.sort()

    # NOTE: sorted() creates a new list, less space efficient

    # O(N)
    for i, curr in enumerate(s_sorted):
        prev = s_sorted[i-1]
        
        if prev == curr:
            return False

    return True

# hello => ehllo
# car => acr 
# foobar => abfoor
print()
print(is_unique2('hello'))
print(is_unique2('car'))
print(is_unique2('foobar'))
