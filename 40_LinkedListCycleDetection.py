# First solution 10/15/2024 - 10 mins

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False
    
"""
Time: O(n)
Space: O(1)

Attempts: 1

Mistakes made:

Learned:
- We can store LinkedList nodes in a set.
"""
        