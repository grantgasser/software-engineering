"""
451. Sort Characters By Frequency
Medium

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""
def frequencySort(self, s: str) -> str:
    result = ''
    
    # O(N)
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
        
    # O(1) bc char set is limited
    # HOW TO: sort dict keys based on value
    # key arg in sorted is a function that will be called on all the
    # elements before comparison, thus this returns the keys of freq in sorted order
    sorted_keys = sorted(freq, key=freq.get, reverse=True)  # max to min
    
    # O(N) [e, t, r] {t: 1, r: 1, e: 2}
    for key in sorted_keys:
        # for num in range(freq[key]):
        #     result += key
        # faster (28% => 59%)
        result += (key * freq[key])
    
    return result


"""Bucket Sort approach (slower and worse mem according to submission)"""
# trying bucket sort now
def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # {e: 2, r: 1, t: 1}

        # bucket sort 
        bucket = [[] for _ in range(len(s) + 1)]
        for k, v in freq.items():
            bucket[v].append(k);

        # bucket = [[], [r, t], [e]]
        result = ''
        for i in range(len(bucket) - 1, -1, -1):
            for j in bucket[i]:
                result += (i * j)

        return result