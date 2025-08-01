# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # ans = []
        # def inorder(node):
        #     if not node:
        #         return
        #     inorder(node.left)
        #     ans.append(node.val)
        #     inorder(node.right)
        # inorder(root)
        # return ans

        # if root is None:
        #     return []
        # ans = []
        # st = []
        # while True:
        #     if root:
        #         st.append(root)
        #         root = root.left
        #     else:
        #         if len(st)==0:
        #             break
        #         root = st.pop()
        #         ans.append(root.val)
        #         root = root.right
        # return ans

        inorder = []
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
                    inorder.append(cur.val)
                    cur = cur.right
            else:
                inorder.append(cur.val)
                cur = cur.right
        return inorder