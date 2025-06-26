# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]  # list to hold max value

        def dia(node):
            if not node:
                return 0
            lh = dia(node.left)
            rh = dia(node.right)
            maxi[0] = max(maxi[0], lh + rh)
            return 1 + max(lh, rh)

        dia(root)
        return maxi[0]