# First solution 10/15/2024 - 20 mins


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


"""
Time: O(n)
Space: O(1)

Attempts: 1, Watched solution  

Mistakes made:

Learned:
- Identifying this type of problem as a linkedlist even though its an array
- Floyd's algorithm, cycle detection by using a fast and slow pointer
"""