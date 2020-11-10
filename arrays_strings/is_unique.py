"""
1.1 
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?

Assuming ASCII, could store in array of bools where index i is ascii val instead of hash table
"""

# NOTE: there's a subtlety I initially missed here. If we assume ASCII, then we know theres only 128
# or 256 characters. Thus, if len(s) > 128, we can return False. Thus, time is actually O(1). Or, 
# more accurately, O(c) time where c is the size of the character set.

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
    # Sort first: O(N LOG N)
    # NOTE: this isn't good because Python sorted() creates a new sorted string
    s_sorted = sorted(s)

    # O(N), 2 points, 1 curr, 1 prev; if curr == prev: return False
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
