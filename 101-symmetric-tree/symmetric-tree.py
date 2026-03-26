# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def symm(node1, node2):
            if not node1 or not node2:
                return node1 == node2

            return node1.val == node2.val and symm(node1.left,node2.right) and symm(node2.left,node1.right)

        return symm(root.left,root.right)
        