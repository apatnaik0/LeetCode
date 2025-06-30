# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # prev = [None]
        # def flat(root):
        #     if not root:
        #         return
        #     flat(root.right)
        #     flat(root.left)
        #     root.right = prev[0]
        #     root.left = None
        #     prev[0] = root
        # flat(root)
        # return root

        if not root:
            return None
        st = []
        st.append(root)
        while st:
            node = st.pop()
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            if st:
                node.right = st[-1]
            node.left = None
        return root
        