# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mps(self,root):
        if not root:
            return 0
        
        ls = max(0,self.mps(root.left))
        rs = max(0,self.mps(root.right))

        self.maxi = max(self.maxi, root.val + ls + rs)
        return root.val + max(ls,rs)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = root.val
        self.mps(root)
        return self.maxi