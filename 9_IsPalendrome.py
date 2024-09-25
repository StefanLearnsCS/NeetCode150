# First solution 9/24/2024 - 15 mins:

class Solution:
    def isPalindrome(self, s: str) -> bool:

        p1 = 0
        p2 = len(s) - 1

        while p2 > p1:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1

        return True
    
"""
Time: O(n)
Space: O(1)
Attempts: 3, Did optimal solution without video.

Mistakes made:
- Didnt "continue" if pointer was not alphanumeric to reset the loop
- Did not account for Capital letters vs lowercase letters

Learned:


"""