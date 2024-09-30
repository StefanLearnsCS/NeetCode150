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
    
# Second solution 9/29/2024 - N/A - No idea how to do this..

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):

            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output