# First solution 9/24/2024 - 15 mins
# Second solution 9/24/2024 - 10 mins:


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    
        l, r = 0, len(numbers) - 1

        while r > l:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

"""
Time: O(n)
Space: O(1)
Attempts: 2, Did less-optimal solution without video, then corrected on 2nd attempt after watching bideo

Mistakes made:
- Was doing O(n^2) solution at first by nesting loops
- should've used pointers on both sides and recognized we can get to answer by my moving the pointers in when sum too large or too small

Learned:


"""
