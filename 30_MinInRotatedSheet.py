# First solution 10/6/2024 - 20 mins

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start, end = 0, len(nums) - 1
        minimum = float("inf")

        while start < end:
            mid = start + (end-start) // 2
            minimum = min(minimum, nums[mid])

            if nums[mid] > nums[end]:
                start = mid + 1

            else:
                end = mid - 1

        return min(minimum, nums[start])
    
"""
Time: O(log n)
Space: O(1)

Attempts: Ended up reading code, gave up too early.
Mistakes made:

Learned:
"""