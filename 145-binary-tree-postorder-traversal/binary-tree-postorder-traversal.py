# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # ans = []
        # def postorder(node):
        #     if not node:
        #         return
        #     postorder(node.left)
        #     postorder(node.right)
        #     ans.append(node.val)
        # postorder(root)
        # return ans

        # if root is None:
        #     return []
        # st1 = []
        # st2 = []
        # st1.append(root)
        # while st1:
        #     node = st1.pop()
        #     st2.append(node)
        #     if node.left:
        #         st1.append(node.left)
        #     if node.right:
        #         st1.append(node.right)
        
        # ans = []
        # while st2:
        #     ans.append(st2.pop().val)
        # return ans

        if root is None:
            return []
        curr = root
        st = []
        ans = []
        while st or curr:
            if curr:
                st.append(curr)
                curr = curr.left
            else:
                temp = st[-1].right
                if temp is None:
                    node = st.pop()
                    ans.append(node.val)
                    while st and node == st[-1].right:
                        node = st.pop()
                        ans.append(node.val)
                else:
                    curr = temp
        return ans
        