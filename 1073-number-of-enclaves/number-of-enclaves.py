class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        vis = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if (i==0 or i==n-1 or j==0 or j==m-1) and grid[i][j]==1:
                    q.append([i,j])
                    vis[i][j] = 1
        delr = [0,0,1,-1]
        delc = [1,-1,0,0]
        while q:
            node = q.popleft()
            r = node[0]
            c = node[1]
            for i in range(4):
                nr = r + delr[i]
                nc = c + delc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]==1 and vis[nr][nc]==0:
                    q.append([nr,nc])
                    vis[nr][nc]=1
        ct = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and vis[i][j]==0:
                    ct+=1
        return ct