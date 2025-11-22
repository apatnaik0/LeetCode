# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bt(self,preorder, pres,pree,inorder, ins,ine, indict):
        if pres > pree or ins > ine:
            return None
        rootval = preorder[pres]
        rootind = indict[rootval]
        left = rootind-ins
        root = TreeNode(rootval)
        root.left = self.bt(preorder,pres+1,pres+left,inorder,ins,rootind-1,indict)
        root.right = self.bt(preorder,pres+left+1,pree,inorder,rootind+1,ine,indict)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indict = {}
        for i in range(len(inorder)):
            indict[inorder[i]] = i
        
        return self.bt(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,indict)
        