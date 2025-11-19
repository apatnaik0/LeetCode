# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self,root):
        if not root:
            return 0
        
        lh = self.depth(root.left)
        rh = self.depth(root.right)

        return max(lh,rh) + 1


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)