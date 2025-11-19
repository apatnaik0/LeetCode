# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,0))
        ans = 0
        while q:
            l = len(q)
            mini = q[0][1]
            for i in range(l):
                cur = q[0][1] - mini
                node = q.popleft()[0]
                if i == 0:
                    first = cur
                if i == l-1:
                    last = cur
                if node.left:
                    q.append((node.left,2*cur+1))
                if node.right:
                    q.append((node.right,2*cur+2))
            ans = max(ans,last-first+1)
        return ans
