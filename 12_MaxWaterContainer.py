# First solution 9/25/2024 - 20 mins

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = 0

        l, r = 0, len(heights) - 1

        while l < r:
            water = 0
            if heights[l] < heights[r]:
                water = heights[l] * (r - l)
                l += 1
            else:
                water = heights[r] * (r - l)
                r -= 1

            if water > output:
                output = water
            
        return output
    
"""
Time: O(n)
Space: O(1)
Attempts: 1, FIRST TRY, DIDN'T WATCH ANY VIDEO, OPTIMAL SOLUTION

Mistakes made:
- Ran once using wrong array name and forgot to return output

Learned:


"""

