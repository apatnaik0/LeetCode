class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    vis[i][j]=1
        ans = [[0 for _ in range(m)] for _ in range(n)]
        while q:
            node = q.popleft()
            r = node[0]
            c = node[1]
            d = node[2]
            ans[r][c]=d
            delr = [0,0,1,-1]
            delc = [-1,1,0,0]
            for i in range(4):
                nr = r+delr[i]
                nc = c+delc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and vis[nr][nc]==0:
                    q.append([nr,nc,d+1])
                    vis[nr][nc]=1
            # print(ans)
        return ans

