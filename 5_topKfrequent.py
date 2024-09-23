# First solution 9/22/2024 - 30 mins:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for x, y in count.items():
            freq[y].append(x)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

"""
Time: O(n)
Attempts: Had to watch video

Mistakes made:
Didn't think it would be viable answer to use so many loops and space

Learned:
count.get(n, 0)  if n isnt in the count dictionary than assume the value as 0

"""