# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTI:
    def pushall(self,node):
        while node:
            self.st.append(node)
            if self.rev:
                node = node.right
            else:
                node = node.left

    def __init__(self,root,rev):
        self.st = []
        self.rev = rev
        self.pushall(root)

    def next(self):
        node = self.st.pop()
        temp = node
        if self.rev:
            self.pushall(temp.left)
        else:
            self.pushall(temp.right)
        return node.val
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = BSTI(root,False)
        r = BSTI(root,True)
        
        i = l.next()
        j = r.next()
        while i<j:
            if i+j==k:
                return True
            elif i+j > k:
                j = r.next()
            else:
                i = l.next()
        return False