# First solution 10/8/2024 - 15 mins

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
"""
Time: O(n)
Space: O(1)

Attempts: Looked at solution right away to remember linkedlists.
Mistakes made:

Learned:
- Using linked list in python
"""