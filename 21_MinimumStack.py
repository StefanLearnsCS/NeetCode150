# First solution 9/30/2024 - 15 mins

class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        self.minlist = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        previous = self.minimum
        if val <= self.minimum:
            self.minimum = val
            self.minlist.append([val, previous])

    def pop(self) -> None:
        if self.stack[-1] == self.minimum:
            self.minimum = self.minlist[-1][1]
            del self.minlist[-1]
        del self.stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum
        
"""
Time: O(1)

Attempts: 2, No video
Mistakes made:
- First attempt had a syntax error
- Could've written cleaner code without using a mimimum value and by treating the min array as another stack that tracks min values

Learned:
- How to use variables in a class
"""
