class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        max_area = 0
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]

        def dfs(r,c, ar):
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1 and vis[nr][nc] == 0:
                    vis[nr][nc] = 1
                    ar += 1
                    ar = dfs(nr,nc,ar)
            return ar

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    vis[i][j] = 1
                    area = dfs(i,j, 1)
                    # print(area)
                    max_area = max(max_area,area)
        
        return max_area