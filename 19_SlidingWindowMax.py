# First solution 9/29/2024 - 15 mins

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maximum = 0
        output = []

        for l in range(len(nums) - k + 1):
            maximum = nums[l]
            r = l + k - 1
            while r > l:
                maximum = max(maximum, nums[r])
                r -= 1
            output.append(maximum)
        
        return output