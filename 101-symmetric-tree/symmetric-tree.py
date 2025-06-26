# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []
        l = root.left
        r = root.right
        def sym(left,right):
            if not left or not right:
                return left==right
            return left.val==right.val and sym(left.left,right.right) and sym(left.right,right.left)
        return sym(l,r)