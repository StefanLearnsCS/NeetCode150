# First solution 9/24/2024 - 40 mins:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashset = collections.defaultdict(set)
        unique = set(nums)

        for x in nums:
            if x - 1 in unique:
                continue
            else:
                hashset[x].add(x)
                count = x
                while count + 1 in unique:
                    count += 1
                    hashset[x].add(count)

        output = 0
        for key, value in hashset.items():
            if len(value) > output:
                output = len(value)

        return output

# Second solution 9/24/2024 - 10 mins:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        unique = set(nums)
        longest = 0

        for x in nums:
            if x - 1 not in unique:
                count = 1
                y = x
                while y + 1 in unique:
                    count += 1
                    y += 1
                if count > longest:
                    longest = count                    

        return longest
    
"""
Time: O(n)
Space: O(n)
Attempts: 1, Had to watch a little bit of video, then got on my own

Mistakes made:
Did not need to use a hashmap, could have just checked if next number exists in set like in 2nd solution
I KEEP THINKING MULTIPLE LOOPS MEANS O(n^2), BUT IT IS O(2n), etc.

Learned:


"""
