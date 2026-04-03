# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def max_sum(self,root):
        if not root:
            return 0

        left_sum = max(0,self.max_sum(root.left))
        right_sum = max(0,self.max_sum(root.right))

        self.maxi = max(self.maxi, root.val + left_sum + right_sum)
        return root.val + max(left_sum,right_sum)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = root.val
        self.max_sum(root)
        return self.maxi