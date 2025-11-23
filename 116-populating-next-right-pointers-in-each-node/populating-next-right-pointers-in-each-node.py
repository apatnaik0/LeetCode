"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                if i!=0:
                    prev.next = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                prev = node
            prev.next = None
        return root
            

        
