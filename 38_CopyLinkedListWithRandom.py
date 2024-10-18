# First solution 10/18/2024 - 30 mins

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        current = head
        while current:
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next

        current = head
        while current:
            copy = oldToCopy[current]
            copy.next = oldToCopy[current.next]
            if current.random:
                copy.random = oldToCopy[current.random]
            else:
                copy.random = None
            copy = copy.next
            current = current.next

        return oldToCopy[head]


"""
Time: O(n)
Space: O(n)

Attempts: 2, Watched video for theory, I had right idea, did coding mostly alone

Mistakes made:
- Knew I had to loop over twice, but didn't think to use dictionary to route from old to copy
- I dont need the if else statement in the last loop

Learned:
- Can use linkedlist node as a key or value in dictionary
"""