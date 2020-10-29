"""
Example: Given a smaller string s and a bigger string b, design an algorithm to find all permutations
of the shorter string within the longer one. Print the location of each permutation.
"""
s = 'abbc'
b = 'cbabadcbbabbcbabaabccbabc'

d = {'a': 1, 'b': 2, 'c': 1}
d2 = {'a': 0, 'b': 0, 'c': 0}

def permutation(small_str, big_str):
    """
    Time: O(B * S) 
    Space: O(B)
    """
    # edge cases
    if not small_str or not big_str:
        raise ValueError('small_str or big_str cannot be empty. small_str: {}, big_str: {}'.format(small_str, big_str))

    if len(small_str) >= len(big_str):
        return -1

    permutations = []

    # build hash maps for small string
    small_str_freq = {}
    small_str_count = {}
    for ch in small_str:
        small_str_freq[ch] = small_str_freq.get(ch, 0) + 1
        small_str_count[ch] = 0
    
    # check permutations of small string in big string, O(B)
    i = 0
    while i < (len(big_str) - len(small_str) - 1):
        is_permutation = True
        # zero out the counts for each first letter, O(S)
        for ch in small_str:
            small_str_count[ch] = 0

        j = i
        while j < (i + len(small_str)) and is_permutation:
            ch = big_str[j]
            if small_str_freq.get(ch):
                if small_str_count[ch] < small_str_freq[ch]:
                    # tally/increment
                    small_str_count[ch] = small_str_count.get(ch, 0) + 1
                else:
                    is_permutation = False
            else:
                #i = j + 1
                is_permutation = False

            j += 1

        if is_permutation:
            permutations.append(i)

        i += 1

    return permutations

print(permutation(s, b))

