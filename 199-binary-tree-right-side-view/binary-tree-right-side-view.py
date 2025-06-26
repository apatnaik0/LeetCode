# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def view(root, level):
            if root is None:
                return
            if len(ans)==level:
                ans.append(root.val)
            view(root.right,level+1)
            view(root.left,level+1)
        view(root,0)
        return ans