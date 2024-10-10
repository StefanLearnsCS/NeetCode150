# First solution 10/9/2024 - 30 mins

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

"""
Time: O(n)
Space: O(1)

Attempts: 1, Had to watch video for solution and code

Mistakes made:
- Couldn't figure out in my head to reverse the second half of the list

Learned:
- Slow and Fast pointer to get middle and end
- Reversing a linkedlist
"""