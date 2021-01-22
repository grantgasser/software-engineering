def get_bit(num, i):
    # gets the ith bit of a number
    return (num & (1 << i)) != 0

print(get_bit(44, 5))

def set_bit(num, i):
    # sets the ith bit of a number
    return num | (1 << i)

print(set_bit(44, 5))  # no change
print(set_bit(44, 6))  # 6th bit is 64, so +64

def clear_bit(num, i):
    # clear the ith bit of a number
    return num & ~(1 << i)

print(clear_bit(44, 5))  # 5th bit is 32, so -32