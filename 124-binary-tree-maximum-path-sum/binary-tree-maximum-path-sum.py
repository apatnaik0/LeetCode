# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = [root.val]
        def mps(root):
            if not root:
                return 0
            ls = max(0,mps(root.left))
            rs = max(0,mps(root.right))
            maxi[0] = max(maxi[0],ls+rs+root.val)
            return root.val + max(ls,rs)
        mps(root)
        return maxi[0]