# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bt(self,inorder, ins,ine, postorder, posts, poste, indict):
        if posts > poste or ins > ine:
            return None

        rootval = postorder[poste]
        rootind = indict[rootval]
        root = TreeNode(rootval)
        left = rootind - ins

        root.left = self.bt(inorder, ins, rootind-1, postorder, posts, posts + left-1, indict)
        root.right = self.bt(inorder, rootind+1, ine, postorder, posts+left, poste-1,indict)
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indict = {}
        for i in range(len(inorder)):
            indict[inorder[i]] = i
        
        return self.bt(inorder,0, len(inorder)-1, postorder, 0, len(postorder)-1,indict)