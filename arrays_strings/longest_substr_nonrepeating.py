"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb" => 3 ("abc")

Input: s = "bbbbb" => 1 ("b")

Input: s = "pwwkew" => 3 ("wke")
--------------------------------------------

# use set for O(1) lookup
visit a: a not in curr_substring_set, so add
{a}

visit b: b not in curr_substring_set, so add
{a, b}

visit c: c not in curr_substring_set, so add
{a, b, c}

visit a: a IS in curr_substring_set
    => increment outer loop count (beginning of substr index)
    => compare len(curr_substring_set) to max_substr



suboptimal: if we only move 1 over after seeing duplicate (e.g. "abcc"), BUT good place to start
and then optimize later

another optimization: stop/return at len(s) - max_substr
    => remaining substring can't be larger than the largest one we already have (max_substr)
"""

"""
Time: O(N^2), 17%
Space: O(S), 49% where S is the length of the longest substr (i.e. the result)
"""
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    max_substr = 0
    curr_substring_set = set([])

    # Loop through substrings
    for i in range(0, len(s)):
        j = i
        while j < len(s) and s[j] not in curr_substring_set:
            curr_substring_set.add(s[j])
            j += 1

        # If this substring is larger than the largest we've seen thus far, update max
        if len(curr_substring_set) > max_substr:
            max_substr = len(curr_substring_set)

        # Empty the set (clear the current substring)
        curr_substring_set.clear()

    return max_substr

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))


"""
O(N) solution
"""
def longest_subtr(s):
    max_substr = 0
    char_index = {}
    i = 0

    for j in range(len(s)):
        if s[j] in char_index:
            i = max(i, char_index[s[j]] + 1)
        char_index[s[j]] = j
        max_substr = max(max_substr, j - i + 1)

    return max_substr

