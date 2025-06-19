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
        if head is None:
            return head
        temp = head
        while temp:
            newnode = Node(temp.val)
            newnode.next = temp.next
            temp.next = newnode
            temp = newnode.next
        
        temp = head
        while temp:
            newnode = temp.next
            if temp.random:
                newnode.random = temp.random.next
            else:
                newnode.random = None
            temp = newnode.next
        
        ans = head.next
        res = ans
        temp = head
        while res:
            temp.next = res.next
            if res.next:
                res.next = res.next.next
            temp = temp.next
            res = res.next
        return ans



        