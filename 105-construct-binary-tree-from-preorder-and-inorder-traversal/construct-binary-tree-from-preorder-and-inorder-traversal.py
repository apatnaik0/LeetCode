# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indict = {}
        for i in range(len(inorder)):
            indict[inorder[i]]=i
        
        def build(preorder,prestart,preend,inorder,instart,inend,indict):
            if prestart>preend or instart > inend:
                return None
            rootval = preorder[prestart]
            rootind = indict[rootval]
            root = TreeNode(rootval)
            numsleft = rootind - instart
            
            root.left =  build(preorder,prestart+1,prestart+numsleft,inorder,instart,rootind-1,indict)
            root.right =  build(preorder,prestart+numsleft+1,preend,inorder,rootind+1,inend,indict)
            return root

        root = build(preorder,0,len(preorder)-1,inorder,0,len(inorder),indict)
        return root