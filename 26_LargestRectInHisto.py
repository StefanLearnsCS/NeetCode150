# First solution 10/3/2024 - 60 mins


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maximum = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maximum = max(maximum, height*(i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maximum = max(maximum, h * (len(heights) - i))

        return maximum
    
"""
Time: O(n)
Space: O(n)

Attempts: 4, Had to watch full solution
Mistakes made:
- Could not figure out how to code it.

Learned:

"""