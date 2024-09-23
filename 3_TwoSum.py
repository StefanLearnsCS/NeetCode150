# First solution 9/22/2024 - 40 mins:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        index1 = 0
        index2 = 0

        for index, value in enumerate(nums):
            if target - value in hashset:
                index1 = index
                index2 = hashset[target-value]
            else:
                hashset[value] = index

        if index1 < index2:
            return [index1, index2]
        else:
            return [index2, index1]

        

        

"""
Time: O(n)
Space: O(n)
Attempts: 4

Mistakes made:
Didn't use hashset to begin with. Tried using two pointers.
Watched video for theoretical solution, couldn't figure out alone.

Learned:

"""