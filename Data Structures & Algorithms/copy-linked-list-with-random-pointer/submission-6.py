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
        oldToCopy = {}

        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            oldToCopy[cur].next = oldToCopy.get(cur.next,None)
            oldToCopy[cur].random = oldToCopy.get(cur.random, None)
            cur = cur.next
        return oldToCopy.get(head, None)