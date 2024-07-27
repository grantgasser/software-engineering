"""Article: https://codesignal.com/blog/interview-prep/example-codesignal-questions/"""

# Question 1
def manipulate(arr):
    new_arr = [None for _ in arr]
    for i, num in enumerate(arr):
        prev = 0 if i < 1 else arr[i-1]
        next = 0 if i >= len(arr) - 1 else arr[i+1]

        new_arr[i] = prev + num + next

    return new_arr

print(manipulate([4, 0, 1, -2, 3]))


# Question 2
def pattern_match(pattern, source):
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_matches = 0

    i = 0
    while i < len(source):
        j = 0
        while j < len(pattern) and (i+j) < len(source):
            if pattern[j] == "0" and source[i+j] not in vowels:
                break
            if pattern[j] == "1" and source[i+j] in vowels:
                break

            j += 1

        # If rule has not been violated, record a match
        if j == len(pattern):
            num_matches += 1

        i += 1

    return num_matches

print(pattern_match("010", "amazing"))
print(pattern_match("100", "codesignal"))
print(pattern_match("1000", "hawaii"))
print(pattern_match("001", "iamthegreatest"))
print(pattern_match("1", "iamthegreatest"))
print(pattern_match("0", "iamthegreatest"))


