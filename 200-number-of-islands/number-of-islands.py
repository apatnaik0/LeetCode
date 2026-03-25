class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        islands = 0
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]

        def dfs(r,c):
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0<=nr<m and 0<=nc<n and vis[nr][nc] == 0 and grid[nr][nc] == '1':
                    vis[nr][nc] = 1
                    dfs(nr,nc)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and vis[i][j]==0:
                    vis[i][j] = 1
                    dfs(i,j)
                    islands += 1
        
        return islands