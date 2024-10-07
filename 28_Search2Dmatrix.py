# First solution 10/6/2024 - 20 mins

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        t, b = 0, len(matrix) - 1

        while t <= b:
            m = b + ((t - b) // 2)

            if target > matrix[m][-1]:
                t = m + 1
            elif target < matrix[m][0]:
                b = m - 1
            elif matrix[m][0] <= target and matrix[m][-1] >= target:
                break
            else:
                return False

        if not (t <= b):
            return False

        l, r = 0, len(matrix[m])
        while l <= r:
            k = l + ((r - l) // 2)
            if matrix[m][k] < target:
                l = k + 1
            elif matrix[m][k] > target:
                r = k - 1
            else:
                return True

        return False


"""
Time: O(log (m * n))
Space: O(1)

Attempts: 2, Dealing with syntax issues
Mistakes made:
- Didnt include if not (t <= b):
            return False

Learned:
"""