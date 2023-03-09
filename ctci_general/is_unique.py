"""
Check if string has all unique characters. Can you do w/o additional memory?
"""

"""O(N) time, O(N) space"""
def is_unique(given_str):
    chars = set([])
    for ch in given_str:
        if ch not in chars:
            chars.add(ch)
        else:
            return False
        
    return True

print(is_unique("cherry"))
print(is_unique("the sun rises"))
print(is_unique("Grant!"))
print(is_unique("car"))

import sys

"""
O(N) time, O(1) space

Although space complexity is O(1), we still have to store 1M+ (max unicode val) 'bits'
"""
def is_unique2(given_str):
    # get max ord by looking, just O(N)
    num_legit_chars = max(ord(ch) for ch in given_str)

    # num_legit_chars = sys.maxunicode  # maximum unicode value, i.e. max value from ord()
    # char_bit_vector = [0]*num_legit_chars

    for ch in given_str:
        idx = ord(ch)

        if idx < num_legit_chars:
            if char_bit_vector[idx]:
                return False
            char_bit_vector[idx] = 1
        else:
            raise ValueError(f'Unrecognized character: {ch}')
        
    return True

print('\n2nd implementation:\n')
print(is_unique2("cherry"))
print(is_unique2("the sun rises"))
print(is_unique2("Grant!"))
print(is_unique2("car"))

"""
NO additional memory at all

Nested loop check: O(N^2) and O(1)

or 

sort first (need to sort w/o additional memory though):

O(N log N) and O(1)

Unfortunately .sort() and sorted() use O(N) memory, so would need to implement
sort separately

=> Could do bucket sort

Bucket Sort: The general rule of thumb is to use a number of buckets 
that's proportional to the input size and proportional to the amount of memory available. 
A common choice is to use n buckets, where n is the square root of the input size.

I suppose you'd have to estimate the size of input.
"""
def is_unique3(given_str):
    pass