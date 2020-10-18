"""
Unnecessary and Duplicated Work
I Example: Print all positive integer solutions to the equation a^3 + b^3 = c^3 + d^3
where a,b,c,d are integers between 1 and 1000. (or N)
"""

# BF is O(N^4), but this is O(N^2)!
def cube_sum(N):
    hash_map = {}

    for c in range(1, N+1):
        for d in range(1, N+1):
            val = c**3 + d**3
            
            curr_pairs = hash_map.get(val, [])
            curr_pairs.append((c, d))

            hash_map[val] = curr_pairs

    for key, val in hash_map.items():
        for pair in val:
            print('key:', key, '\t a,b or c,d pair:', pair[0], pair[1])

print(cube_sum(10))