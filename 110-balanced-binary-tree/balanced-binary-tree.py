# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanced(self,root):
        if not root:
            return 0

        lt = self.balanced(root.left)
        rt = self.balanced(root.right)

        if lt == -1:
            return -1
        
        if rt == -1:
            return -1

        if abs(lt - rt) > 1:
            return -1

        return 1 + max(lt,rt)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balanced(root)!= -1