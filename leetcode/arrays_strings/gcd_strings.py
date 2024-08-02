"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB", ABABABABAB, ABABABABAB
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
"""

# INTUITION: add on either side, if not equal, there is no common substring
# Also, use math.gcd (i.e. math.gcd(10, 15) -> 5)
import math
def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    gcd_length = math.gcd(len(str1), len(str2))
    return str1[:gcd_length]