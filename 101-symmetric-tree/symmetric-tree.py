# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sym(self,l,r):
        if not l or not r:
            return l == r
        
        return l.val == r.val and self.sym(l.left,r.right) and self.sym(l.right,r.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l = root.left
        r = root.right

        return self.sym(l,r)