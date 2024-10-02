# First solution 10/1/2024 - 15 mins

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #index
        output = [0]*len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                cooler = stack.pop()
                output[cooler] = index - cooler

            stack.append(index)

        return output


"""
Time: O(n)
Space: O(n)

Attempts: 1, FIRST TRY
Mistakes made:
- Ran with output = []*len(temps) got error, changed to output=[0]*len(temps)

Learned:

"""