# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def leftheight(root):
            if not root:
                return 0
            h = 0
            while root:
                root = root.left
                h+=1
            return h
        
        def rightheight(root):
            if not root:
                return 0
            h = 0
            while root:
                root = root.right
                h+=1
            return h
        
        def count(root):
            if root is None:
                # print('none')
                return 0
            # print(root.val)
            lh = leftheight(root)
            rh = rightheight(root)
            # print(lh,rh)
            if lh == rh:
                return (2**(lh)) - 1
            return 1+count(root.left)+count(root.right)
        
        ans = count(root)
        return ans