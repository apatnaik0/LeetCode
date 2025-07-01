# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        while root:
            if root.left:
                node = root.left
                while node.right and node.right!=root:
                    node = node.right
                if not node.right:
                    node.right = root
                    root = root.left
                if node.right == root:
                    node.right = None
                    k-=1
                    if k==0:
                        return root.val
                    root = root.right
            else:
                k-=1
                if k==0:
                    return root.val
                root = root.right
        