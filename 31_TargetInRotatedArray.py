# First try 10/6/2024 - 45 mins

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            mid = start + (end-start) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if nums[start] <= target or nums[end] > target:
                    end = mid - 1
                else:
                    start = mid + 1

            else:
                if nums[end] >= target or nums[start] > target:
                    start = mid + 1
                else:
                    end = mid - 1

        return -1

# Need to try again, this is close but not enough, need to rethink.

# Second solution:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        
        while start <= end:
            m = start + ((end - start) // 2)

            if nums[m] == target:
                return m

            if nums[start] <= nums[m]:
                if nums[start] <= target < nums[m]:
                    end = m - 1
                else:
                    start = m + 1

            else:
                if nums[m] < target <= nums[end]:
                    start = m + 1
                else:
                    end = m - 1

        return -1
