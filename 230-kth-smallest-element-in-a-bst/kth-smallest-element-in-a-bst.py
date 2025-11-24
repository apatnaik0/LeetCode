# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur = root
        while cur:
            if cur.left:
                node = cur.left
                while node.right and node.right!=cur:
                    node = node.right
                if not node.right:
                    node.right = cur
                    cur = cur.left
                if node.right == cur:
                    node.right = None
                    k -= 1
                    if k == 0:
                        return cur.val
                    cur = cur.right
            else:
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.right