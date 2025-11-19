# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanced(self, root):
        if not root:
            return 0

        lh = self.balanced(root.left)
        rh = self.balanced(root.right)

        if lh == -1:
            return -1
        if rh == -1:
            return -1
        
        if abs(lh-rh)>1:
            return -1
        
        return 1 + max(lh,rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balanced(root) != -1