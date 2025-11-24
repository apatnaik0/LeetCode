# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTI:
    def __init__(self,root,rev):
        self.st = []
        self.rev = rev
        self.pushall(root)

    def pushall(self,root):
        while root:
            self.st.append(root)
            if self.rev:
                root = root.right
            else:
                root = root.left

    def next(self):
        node = self.st.pop()
        if self.rev:
            self.pushall(node.left)
        else:
            self.pushall(node.right)
        return node.val

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        li = BSTI(root,False)
        ri = BSTI(root,True)

        lv = li.next()
        rv = ri.next()
        while lv < rv:
            if lv + rv == k:
                return True
            elif lv + rv > k:
                rv = ri.next()
            else:
                lv = li.next()
        return False