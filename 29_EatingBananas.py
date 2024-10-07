# First solution 10/6/2024 - 30 mins

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            total = 0
            for i in piles:
                total += math.ceil(i / m)
            
            if total <= h:
                res = m
                r = m - 1

            else:
                l = m + 1

        return res
            
"""
Time: O(log(maxp) * p)
Space: O(maxp)

Attempts: 3, syntax error, had to watch part of solution to get idea

Mistakes made:
- Couldn't figure out where to use binary search, didn't think to have seperate list of possible eating rates.

Learned:
math.ceil(a / b) gives upper part of decimal number 1/3 = 1  3/2 = 2
"""
