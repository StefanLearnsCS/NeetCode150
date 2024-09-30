# First solution 9/30/2024 - 10 mins

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1 + val2))
            elif c == '-':
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1 - val2))
            elif c == '*':
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1 * val2))
            elif c == '/':
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1 / val2))
            else:
                stack.append(int(c))
        return int(stack.pop())
    

"""
Time: O(n)
Space: O(n)

Attempts: 1
Mistakes made:
- Had to run few times to deal with syntax errors and rounding, forgot to use int()

Learned:
"""
