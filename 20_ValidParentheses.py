# First solution 9/30/2024 - 10 mins

class Solution:
    def isValid(self, s: str) -> bool:
        validate = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []

        for bracket in s:
            if stack and (bracket in validate):
                if validate[bracket] != stack.pop():
                    return False
            else:
                stack.append(bracket)

        if stack:
            return False
        else:
            return True
        
"""
Time: O(n)
Space: O(n)
Attempts: 2, No video, but have seen tiktok about this problem
Mistakes made:
- First attempt forgot to check if stack was empty before popping

Learned:
"""