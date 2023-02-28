"""
O(N) time, where N is the _number of characters_ in the array

O(1) space
"""
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    longest_prefix = strs[0]

    for i in range(1, len(strs)):
        word = strs[i]
        stopping_condition = False
        j = 0
        while j < len(word):
            if j >= len(longest_prefix) or word[j] != longest_prefix[j]:
                break

            j += 1
        longest_prefix = word[:j]

    return longest_prefix


"""More efficient"""
def longest_common_prefix(strs):
    if not strs:
        return ""

        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for word in strs:
                if word[i] != ch:
                    return shortest[:i]
        
        return shortest