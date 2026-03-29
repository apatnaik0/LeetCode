# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self,root):
        if not root:
            return

        
        self.inorder(root.left)
        self.ct -= 1
        if self.ct == 0:
            self.ans = root.val
            return
        self.inorder(root.right)
        return


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.ans = 0
        self.ct = k
        self.inorder(root)
        return self.ans

        