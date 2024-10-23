# First solution 10/22/2024 - 20 mins

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
"""
Time: O(n)
Space: O(1)

Attempts: Read code right away, short on time and learning trees in python

Mistakes made:

Learned:
"""
        
