# First solution 9/26/2024 - 60 mins

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        water = 0
        l, r = 0, len(height) - 1
        maxl = height[l]
        maxr = height[r]

        while l < r:
            if maxl < maxr:
                l += 1
                maxl = max(maxl, height[l])
                water += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                water += maxr - height[r]

        return water

"""
Time: O(n)
Space: O(1)
Attempts: Had to watch video for full solution and coding

Mistakes made:
- Could not figure out solution or formulas or how to effectively code the solution

Learned:


"""