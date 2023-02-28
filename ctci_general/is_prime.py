"""
Check is a number is prime

16

sqrt(16) => 4, so check 2 (2*2=4),3 (3*3=9),4 (4*4=16, not prime)

32

sqrt(32) => 5.X, so check (2*2=4),3 (3*3=9),4 (4*4=16, and 32 % 16 == 0 so not prime)

11

sqrt(11) => 3.X, so check 2, 3
"""
import math

def is_prime(num):
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1

    return True

print('32:', is_prime(32))
print('11:', is_prime(11))
print('16:', is_prime(16))
print('5:', is_prime(5))
print('77:', is_prime(77))
print('1:', is_prime(1))