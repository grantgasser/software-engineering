"""
5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a 0 to a 1. Write code to
find the length of the longest sequence of 1s you could create.

Ex. 
    In: 1775 (11011101111)
    Out: 8

Try to get O(b) where b is # of bits
"""
from common_functions import get_bit, set_bit

def flip_bit_to_win(binary_num_str):
    # view in binary, O(N), not the best but it works
    #print(bin(num))
    print(binary_num_str)

    count = 0
    running_ones_total = 0
    prev = None
    used_zero = False 
    for idx, bit in enumerate(binary_num_str):
        if bit == '1':
            count += 1
            running_ones_total += 1
            prev = bit
        else:
            if prev == '0' or used_zero:
                count = running_ones_total + 1
            elif prev == '1' or prev is None:
                used_zero = True
                count += 1

            running_ones_total = 0
            prev = bit

    return count         

print(flip_bit_to_win(bin(1775)[2:]))  # expect 8
print(flip_bit_to_win('00101100'))  # expect 4, FIX

# TODO: optimal algorithm
def optimal_flip_bit(num):
    pass