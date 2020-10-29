"""
Runtime: 36 ms, 53%
Memory Usage: 14.2 MB

Looked and got some help but most on my own

Time: O(N)
Space: O(N) to create "reverse" string
"""
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        
        # O(N)
        if A == B:
            for i, ch in enumerate(A):
                if A[i] in A[i+1:]:
                    return True
            return False
        
        else:
            # O(N)
            diff = [] # (idx, val)
            for i, ch in enumerate(A):
                if A[i] != B[i]:
                    diff.append((i, A[i]))
                
                if len(diff) == 2:
                    reverse = list(A)
                    reverse[diff[0][0]] = diff[1][1]
                    reverse[diff[1][0]] = diff[0][1]
                    
                    if ''.join(reverse) == B:
                        return True
                    else:
                        return False
                    
            return False