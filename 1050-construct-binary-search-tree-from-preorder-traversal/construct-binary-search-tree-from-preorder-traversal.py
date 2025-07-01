# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def build(preorder,i,ub):
            if (i[0]==len(preorder) )or preorder[i[0]] >= ub:
                return None
            root = TreeNode(preorder[i[0]])
            i[0] += 1
            root.left = build(preorder, i, root.val)
            root.right = build(preorder, i, ub)
            return root

        i = [0]
        ub = float('inf')
        root = build(preorder,i,ub)
        return root
        