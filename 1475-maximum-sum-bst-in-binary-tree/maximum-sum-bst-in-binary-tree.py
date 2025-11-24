# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,node):
        if not node:
            return 0, True, float('-inf'), float('inf')

        sl, bstl, maxil, minil = self.check(node.left)
        sr, bstr, maxir, minir = self.check(node.right)
        if bstl and bstr and maxil < node.val < minir:
            val = node.val + sl + sr
            self.ans = max(self.ans,val)
            return val,True, max(maxir,node.val), min(node.val, minil)
        return 0, False, float('-inf'), float('inf')

    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.check(root)
        return self.ans