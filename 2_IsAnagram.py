# First solution 9/17/2024 - 15 mins:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for i in s:
            if i in smap:
                smap[i] += 1
            else:
                smap[i] = 1

        for i in t:
            if i in tmap:
                tmap[i] += 1
            else:
                tmap[i] = 1

        for key, value in smap.items():
            if key in tmap:
                if tmap[key] != value:
                    return False
            else:
                return False

        if len(t) != len(s):
            return False
        
        return True

"""
Time: O(s + t)
Space: O(s + t)
Attempts: 2

Mistakes made:
Didn't include edge case if length of strings are different.
Could have filled dictionaries using only one loop
Should use .get() function instead of .items()  [Watch video]

Learned:
Learned about .get()
"""