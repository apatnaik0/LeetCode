# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        # def preorder(node):
        #     if node is None:
        #         return
        #     ans.append(node.val)
        #     preorder(node.left)
        #     preorder(node.right)
        # preorder(root)
        # return ans

        # if root is None:
        #     return []
        # ans = []
        # st = []
        # st.append(root)
        # while st:
        #     node = st.pop()
        #     ans.append(node.val)
        #     if node.right:
        #         st.append(node.right)
        #     if node.left:
        #         st.append(node.left)
        # return ans

        preorder = []
        cur = root
        while cur:
            if cur.left:
                node = cur.left
                while node.right and node.right!=cur:
                    node = node.right
                if not node.right:
                    node.right = cur
                    preorder.append(cur.val)
                    cur = cur.left
                if node.right == cur:
                    node.right = None
                    cur = cur.right
                
            else:
                preorder.append(cur.val)
                cur = cur.right
        return preorder
            
        