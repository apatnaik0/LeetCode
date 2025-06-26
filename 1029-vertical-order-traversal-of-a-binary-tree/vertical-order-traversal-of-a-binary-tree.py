# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = {}
        q = deque()
        q.append((root,0))
        mini,maxi = 0,0
        y=0
        while q:
            for i in range(len(q)):
                node,x = q.popleft()
                if x not in res:
                    res[x] = {}
                if y not in res[x]:
                    res[x][y] = []
                res[x][y].append(node.val)
                mini = min(x,mini)
                maxi = max(x,maxi)
                if node.left:
                    q.append((node.left,x-1))
                if node.right:
                    q.append((node.right,x+1))
            y+=1

        ans = []
        for i in range(mini,maxi+1):
            v_level = []
            for j in range(y):
                if i in res and j in res[i]:
                    res[i][j].sort()
                    v_level.extend(res[i][j])
            ans.append(v_level)
        return ans


