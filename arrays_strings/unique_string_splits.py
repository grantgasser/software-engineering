"""
input: xzxzx

x, z, xzx (first split is 2 singles and then the rest)
x, zx, zx
x, zxz, x
-> cant take anymore from c
xz, xz, x
xzx, z, x
-> can't take anymore from b -> DONE (5)

input: xzy

x, z, y
-> can't take anymore from c or b -> DONE (1)

input: xxx

x,x,x, BUT a != b !=c is NOT TRUE!, so don't increment count
can't take anymore from c or b -> DONE (0)

input: xyzxy

x, y, zxy
x, yz, xy
x, yzx, y
xy, zx, y
xyz, x, y
-> DONE (5)

input: xyyx

x, y, yx (+1)
x, yy, x 
xy, y, x (+1)


Just need two pointers: i and j to make 3 splits (a,b,c):
    a, b, c = s[:i], s[i:j], s[j:]
    - simple nested loop approach
    - O(N^2) time and O(N)
"""

def solution(s):
    count = 0
   
    for i in range(1, len(s) - 1):
        for j in range(i + 1, len(s)):
            a, b, c = s[:i], s[i:j], s[j:]
            if (a+b) != (b+c) and (b+c) != (c+a) and (a+b) != (c+a):
                count += 1
    return count