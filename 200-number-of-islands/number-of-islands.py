class Solution:

    def dfs(self,grid,i,j,m,n):
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if 0 <= nr < m and 0 <= nc < n and self.vis[nr][nc]==0 and grid[nr][nc] == '1':
                self.vis[nr][nc] = 1
                self.dfs(grid,nr,nc,m,n)

    def bfs(self,grid,i,j,m,n):
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        q = deque()
        q.append((i,j))
        self.vis[i][j] = 1
        while q:
            r,c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < m and 0 <= nc < n and self.vis[nr][nc]==0 and grid[nr][nc] == '1':
                    q.append((nr,nc))
                    self.vis[nr][nc] = 1

    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        self.vis = [[0 for _ in range(n)] for _ in range(m)]
        ct = 0

        for i in range(m):
            for j in range(n):
                # print(grid[i][j])
                if grid[i][j]=='1' and self.vis[i][j]==0:
                    # print('inside if')
                    self.dfs(grid,i,j,m,n)
                    ct += 1
        
        return ct