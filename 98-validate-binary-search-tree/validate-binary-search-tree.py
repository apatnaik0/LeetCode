# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,maxi,mini):
        if not root:
            return True

        if root.val >= maxi or root.val <= mini:
            return False
        
        return self.check(root.left,root.val,mini) and self.check(root.right,maxi,root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxi = float('inf')
        mini = float('-inf')
        return self.check(root, maxi, mini)