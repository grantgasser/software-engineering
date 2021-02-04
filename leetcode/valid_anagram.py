"""
242. Valid Anagram
Easy

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(N)
        Space: O(|characters|) => O(1)
        """
        # input validation
        if len(s) != len(t):
            return False
        
        # same string
        if not s and not t:
            return True
        
        # character frequency
        freq = {}
        for s_char, t_char in zip(s, t):
            freq[s_char] = freq.get(s_char, 0) + 1
            freq[t_char] = freq.get(t_char, 0) - 1
            
        # if anagram, all frequencies should be 0 now
        for val in freq.values():
            if val != 0:
                return False
        return True