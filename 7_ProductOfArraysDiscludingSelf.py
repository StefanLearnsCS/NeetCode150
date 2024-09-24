# First solution 9/24/2024 - 30 mins:

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        length = len(nums)
        prefix = 1
        postfix = 1

        for i in range(length):
            output[i] = prefix
            prefix *= nums[i]

        for i in range(length - 1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]

        return output
    

"""
Time: O(n)
Space: O(1) output array doesn't count
Attempts: 1, Had to watch video, did coding by myself first try

Mistakes made:
No mistakes made. Just couldn't figure out solution of prefix and postfixs

Learned:
prefix and postfix method.
Looping backwards through array.
"""
            