# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validbst(root,maxi,mini):
            if not root:
                return True
            if root.val <= mini or root.val >= maxi:
                return False
            return validbst(root.left,root.val,mini) and validbst(root.right,maxi,root.val)
        return validbst(root,float("inf"), float("-inf")) 
        