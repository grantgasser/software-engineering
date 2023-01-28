"""
1641

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
Example 3:

Input: n = 33
Output: 66045
"""

"""Correct but inefficient solution"""
def countVowelStrings(n):
    """
    :type n: int
    :rtype: int
    """
    counts = [5]

    for i in range(1, n):
        prev_counts = counts.copy()
        for idx, c in enumerate(prev_counts):
            for j in range(c-1, 0, -1):
                print('inserting:', j)
                counts.insert(idx + (c-j), j)

    print(counts)
    return sum(counts)

print(countVowelStrings(3))


"""
More efficient DP (O(N)) solution (beats 95% runtime)
n = 1

first letter is:
   a  e  i  o  u
1  1  1  1  1  1
2  5  4  3  2  1
3  15 10 6  3  1

dp[i][v] = dp[i-1][j] + dp[i-1][j+1] for j in range(v, 0). #i.e. sum the row above [j:]
"""

class Solution:
    def countVowelStrings(self, n: int) -> int:
        v = 5
        dp = [[1]*v]

        for i in range(1, n):
            dp.append([0]*v)

            for j in range(0, v):
                dp[i][j] = sum(dp[i-1][j:])

        return sum(dp[-1])