# First solution 10/15/2024 - 30 mins

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            newvalue = total % 10

            current.next = ListNode(newvalue)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


"""
Time: O(n)
Space: O(n)

Attempts: 3, Used GPT for solution

Mistakes made:
- Was originally trying to add together the sum and then indexing the sum string to create a new list for the result

Learned:
"""
        