# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        cur = root
        while cur:
            if cur.left:
                node = cur.left
                while node.right and node.right!=cur:
                    node = node.right
                
                if not node.right:
                    node.right = cur
                    cur = cur.left
                else:
                    node.right = None
                    ans.append(cur.val)
                    cur = cur.right
            else:
                ans.append(cur.val)
                cur = cur.right
        return ans
                    
