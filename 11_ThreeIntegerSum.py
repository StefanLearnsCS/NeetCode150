# First solution 9/25/2024 - 40 mins

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        nums.sort()

        for i, n in enumerate(nums):
            if n in used:
                continue
            p1 = i + 1
            p2 = len(nums) - 1

            if p1 >= p2:
                break

            used.add(n)
            sumbc = 0 - n

            while p1 < p2:
                if nums[p1] + nums[p2] < sumbc:
                    p1 += 1
                elif nums[p1] + nums[p2] > sumbc:
                    p2 -= 1
                elif  nums[p1] + nums[p2] == sumbc:
                    res.append([n, nums[p1], nums[p2]])
                    p1 += 1
                    while nums[p1] == nums[p1-1] and p1 < p2:
                        p1 += 1

        return res

            
"""
Time: O(n^2)
Space: O(n)
Attempts: 6, Had to watch video for solution, and some of the coding

Mistakes made:
- Had the idea of solution, but didn't think O(n^2) would be optimal so I got stuck
- Didn't think it would be appropriate to use .sort() but its okay since solution O(n^2).

Learned:


"""

