# Complement of Base 10 Integer - Number Complement
def complement(N):
    return int(''.join(['1' if x == '0' else '0' for x in bin(N)[2:]]), 2)