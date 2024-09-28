# First solution 9/28/2024 - 45 mins

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def matches(sMap, tMap):
            for key, value in tMap.items():
                if sMap.get(key, 0) < value:
                    return False
            return True

        if len(t) > len(s):
            return ""

        sMap = {}
        tMap = {}

        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)

        l, r = 0, 0
        minimum = 9999
        output = ""

        l = 0
        for r in range(len(s)):
            sMap[s[r]] = 1 + sMap.get(s[r], 0)

            while matches(sMap, tMap):
                if r - l + 1 < minimum:
                    minimum = r - l + 1
                    output = s[l:r+1]

                sMap[s[l]] -= 1
                l += 1

        return output

"""
Time: O(n)
Space: O(s + t)
Attempts: 3, Had to watch video for part of solution, matched what I had in mind, did coding alone took a while to debug had to use chatgpt

Mistakes made:
- Using a while loop at first to move r instead of a for loop

Learned:
- My solution is similar to video, but id review it again, he does it without helper function which would be better.
"""




                