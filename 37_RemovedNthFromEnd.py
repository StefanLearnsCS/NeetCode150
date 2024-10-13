# First solution 10/13/2024 - 30 mins

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
        

"""
Time: O(n)
Space: O(1)

Attempts: 3, Had to watch video for solution

Mistakes made:
- my original solution was much more bruteforce

Learned:
- Left and Right with a dummy to get to a specific index from the end
"""
        