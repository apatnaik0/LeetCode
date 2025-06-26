# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(root):
            if root is None:
                return 0

            lh = depth(root.left)
            rh = depth(root.right)

            return 1+max(lh,rh)
        
        ans = depth(root)
        return ans