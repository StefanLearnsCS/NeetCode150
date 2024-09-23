# First solution 9/23/2024 - 15 mins:

class Solution:

    def encode(self, strs: List[str]) -> str:
        single = ""
        for i in strs:
            single += str(len(i)) + "#" + i
        return single

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return result

"""
Time: O(n)
Attempts: 5, Had to watch video

Mistakes made:
I had the correct logic first try, but did not account for strings with higher length than 9. Was only looking for
the first sign of a number and then # after.

Learned:
Consider all edge cases!
Slicing "hello world"   string[0:5] would equal "hello"
"""