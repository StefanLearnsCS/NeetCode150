# First solution 9/27/2024 - 20 mins


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        unique = set()
        maximum = 0

        l, r = 0, 0

        while r < len(s):

            if not s[r] in unique:
                unique.add(s[r])
                r += 1
            elif s[r] in unique:
                unique.remove(s[l])
                l += 1
                
            maximum = max(maximum, len(unique))

        return maximum
    
"""
Time: O(n)
Space: O(n)
Attempts: 3

Mistakes made:
- Had theory/logic correct, was not coding correctly.

Learned:

"""