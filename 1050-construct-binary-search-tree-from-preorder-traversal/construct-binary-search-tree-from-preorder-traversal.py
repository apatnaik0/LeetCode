# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bt(self,preorder,ub):
        if self.ind >= len(preorder) or preorder[self.ind]>ub:
            return None
        
        node = TreeNode(preorder[self.ind])
        self.ind += 1
        node.left = self.bt(preorder,node.val)
        node.right = self.bt(preorder,ub)
        return node

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.ind = 0
        ub = float('inf')
        return self.bt(preorder,ub)