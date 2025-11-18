# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = {}
        q = deque()
        y = 0
        mini = 0
        maxi = 0
        q.append((root,0))
        while q:
            l = len(q)
            for i in range(l):
                node, x = q.popleft()
                if x not in ans:
                    ans[x] = {}
                if y not in ans[x]:
                    ans[x][y] = []
                ans[x][y].append(node.val)
                mini = min(x,mini)
                maxi = max(x,maxi)
                if node.left:
                    q.append((node.left, x - 1))
                if node.right:
                    q.append((node.right, x + 1))
            y += 1
        
        final = []
        for i in range(mini, maxi + 1):
            v = []
            for j in range(y):
                if i in ans and j in ans[i]:
                    ans[i][j].sort()
                    v.extend(ans[i][j])
            final.append(v)
        
        return final

                