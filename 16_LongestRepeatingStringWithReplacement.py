# First solution 9/27/2024 - 45 mins

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        maximum = 0

        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            maximum = max(maximum, r - l + 1)
        
        return maximum

"""
Time: O(n)
Space: O(1)
Attempts: 4

Mistakes made:
- Had the right idea about using a dictionary to store numbers, didn't know how to code
- After watching video had better idea of code but I used a while loop instead of for loop and was getting answers off by 1

Learned:
Noticing sliding window solutions are all using for loops instead of while loops.

"""