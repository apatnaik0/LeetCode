# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self,node,max_so_far):

        if not node:
            return 0

        count = 1 if node.val >= max_so_far else 0

        new_max = max(max_so_far,node.val)

        count += self.dfs(node.left, new_max)
        count += self.dfs(node.right,new_max)

        return count

    def goodNodes(self, root: TreeNode) -> int:
        
        return self.dfs(root, root.val)