# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indict = {}
        for i in range(len(inorder)):
            indict[inorder[i]] = i
        
        def build(inorder,ins,ine,postorder,pos,poe,indict):
            if pos>poe or ins>ine:
                return None
            rootval = postorder[poe]
            rootind = indict[rootval]
            numsleft = rootind - ins
            root = TreeNode(rootval)
            root.left = build(inorder,ins,rootind-1,postorder,pos,pos+numsleft-1,indict)
            root.right = build(inorder,rootind+1,ine,postorder,pos+numsleft,poe-1,indict)
            return root
        root = build(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,indict)
        return root
        