# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,preorder,inorder,preorder_start,preorder_end,inorder_start,inorder_end,indict):
        if preorder_start>preorder_end or inorder_start>inorder_end:
            return None

        rootval = preorder[preorder_start]
        rootind = indict[rootval]
        node = TreeNode(rootval)
        nums_left = rootind - inorder_start

        node.left = self.build(preorder,inorder,preorder_start+1,preorder_start+nums_left,inorder_start,rootind - 1,indict)
        node.right = self.build(preorder,inorder,preorder_start+nums_left+1,preorder_end,rootind + 1,inorder_end,indict)

        return node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_start = 0
        preorder_end = len(preorder) - 1
        inorder_start = 0
        inorder_end = len(inorder) - 1

        indict = {}
        for i in range(inorder_end+1):
            indict[inorder[i]] = i

        return self.build(preorder,inorder,preorder_start,preorder_end,inorder_start,inorder_end,indict)



        