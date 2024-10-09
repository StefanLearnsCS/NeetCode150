# First solution 10/8/2024 - 15 mins

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        A = list1
        B = list2

        if not A:
            return B
        if not B:
            return A

        head = A
        if A.val > B.val:
            head = B
            B = B.next
        else:
            A = A.next

        curr = head
        while A or B:
            if not A:
                curr.next = B
                B = B.next
            elif not B:
                curr.next = A
                A = A.next
            elif A.val <= B.val:
                curr.next = A
                A = A.next
            else:
                curr.next = B
                B = B.next

            curr = curr.next

        return head
    
"""
Time: O(n + m)
Space: O(n + m)

Attempts: 1

Mistakes made:
- Didn't create a new node instead of complicated code at beginning

Learned:
- How to create a new node
"""