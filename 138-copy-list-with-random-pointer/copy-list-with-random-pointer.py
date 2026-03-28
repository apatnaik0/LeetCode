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

        if not head:
            return None

        cur = head
        while cur:
            temp = Node(cur.val)
            front = cur.next
            cur.next = temp
            temp.next = front
            cur = front

        cur = head
        while cur:
            temp = cur.next
            if cur.random:
                temp.random = cur.random.next
            cur = cur.next.next

        
        newhead = head.next
        temp = newhead
        cur = head
        while cur:
            front = cur.next.next
            if temp.next:
                temp.next = front.next
                temp = front.next
            cur = front 
        
        return newhead
        