class Solution:
    def bfs(self,grid,i,j,vis,m,n):
        q = deque()
        q.append((i,j))
        vis[i][j] = 1

        while q:
            r,c = q.popleft()
            dr = [0,0,1,-1]
            dc = [1,-1,0,0]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < m and 0 <= nc < n and vis[nr][nc] == 0 and grid[nr][nc] == '1':
                    q.append((nr,nc))
                    vis[nr][nc] = 1

        return 

    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        ct = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and vis[i][j] == 0:
                    self.bfs(grid,i,j,vis,m,n)
                    ct += 1

        return ct