# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,node,mini,maxi):
        if not node:
            return True
        
        if not (node.val > mini and node.val < maxi):
            return False

        return self.helper(node.left,mini, node.val) and self.helper(node.right,node.val, maxi)
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,float('-inf'),float('inf'))