# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        last = None
        middle = None
        prev = TreeNode(float('-inf'))
        while root:
            if root.left:
                node = root.left
                while node.right and node.right!=root:
                    node = node.right
                if not node.right:
                    node.right = root
                    root = root.left
                if node.right==root:
                    if (root.val < prev.val):
                        if not first:
                            first = prev
                            middle = root
                        else:
                            last = root
                    else:
                        prev = root
                    node.right = None
                    root = root.right
            else:
                if (root.val < prev.val):
                    if not first:
                        first = prev
                        middle = root
                    else:
                        last = root
                else:
                    prev = root
                root = root.right
        if first and last:
            first.val, last.val = last.val, first.val
        else:
            first.val, middle.val = middle.val, first.val
        