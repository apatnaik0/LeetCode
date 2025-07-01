# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(root):
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            n1 = root.right
            temp = root.left
            while temp.right:
                temp = temp.right
            temp.right = n1
            return root.left
        cur = root
        while cur:
            # print(cur.val)
            if key == cur.val:
                # print('in if 1')
                return helper(cur)
            if key<cur.val:
                # print('in if 2',cur.val)
                if cur.left and cur.left.val==key:
                   cur.left = helper(cur.left)
                   break
                else:
                    cur = cur.left
            else:
                # print('in else',cur.val)
                if cur.right and cur.right.val==key:
                   cur.right = helper(cur.right)
                   break
                else:
                    cur = cur.right
        return root
                
            
        