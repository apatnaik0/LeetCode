# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def avgTree(self,node):
        if not node:
            return 0,0

        ls, ln = self.avgTree(node.left)
        rs, rn = self.avgTree(node.right)

        s = node.val +ls +rs
        n = 1 + ln + rn 
        
        if s//n == node.val:
            self.ans += 1
        
        return s,n
        


    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        self.avgTree(root)
        return self.ans
