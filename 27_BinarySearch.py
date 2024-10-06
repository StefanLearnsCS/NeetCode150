# First solution 10/5/2024 - 20 mins

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            k = l + ((r - l) // 2)
            if nums[k] < target:
                l = k + 1
            elif nums[k] > target:
                r = k - 1
            else:
                return k

        return -1
    
    
"""
Time: O(logn)
Space: O(1)

Attempts: 3, Dealing with syntax issues
Mistakes made:
- Used wrong formula for midpoint

Learned:
- l + r // 2 can cause overflow, so we use this one above instead for midpoint.
"""