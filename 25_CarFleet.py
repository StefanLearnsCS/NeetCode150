# First solution 10/1/2024 - 30 mins

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]: #Reverse sorted order
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

"""
Time: O(nlogn)
Space: O(n)

Attempts: 3, Had to watch solution, didn't realize we had to sort and do it in nlogn
Mistakes made:
- Was trying to avoid appending the stack at beginning of loop because I couldn't imagine solution at first.

Learned:
- zip function

"""