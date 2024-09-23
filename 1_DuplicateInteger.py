# First solution 9/17/2024 - 10 mins:

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = []
        for i in range(len(nums)):
            if not nums[i] in unique:
                unique.append(nums[i])
            else:
                return True
        return False
    
"""
Time: O(n)
Space: O(n)
Attempts: 3
Mistakes made:
Didn't realize arrays could be unsorted i.e. [1 ,2 ,3, 1]

Learned:
I should have used a Set instead of List for storing values. unique = set()
O(nlogn) if you sort array and then loop through. Sorting is logn complexity
"""

# Second solution 9/23/2024 - 2 mins:

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        occur = set()

        for i in nums:
            if i in occur:
                return True
            else:
                occur.add(i)
        
        return False
    
"""
Time: O(n)
Space: O(n)
Attempts: 1
Mistakes made:
Forgot to return False after the loop


Learned:

"""
