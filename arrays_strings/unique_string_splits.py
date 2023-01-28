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
"""

def solution(s):
    count = 0
   
    a = s[0]
    b = s[1]
    c = s[2:]
    
    if a != b != c:
        count += 1
    
    # strip down 3rd split (c) first
    while len(c) > 1:
        print('a,b,c:', a,b,c)
        print('b:', b)
        print('adding c[0]:', c[0])
        b += c[0]
        c = c[1:]
        print('now b and c:', b, c)
        
        if a != b != c:
            #print('stripping c:', a, b, c)
            count += 1
            print('count incremented:', count)
        
    while len(b) > 1:
        a += b[0]
        b = b[1:]
        
        if a != b != c:
            #print('stripping b:', a, b, c)
            count += 1

    return count

print(solution("xzxzx"))