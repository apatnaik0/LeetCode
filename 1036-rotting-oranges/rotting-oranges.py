class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        rot = 0
        dr = [0,0,1,-1]
        dc = [1,-1,0,0]
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        minutes = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
                    # rot += 1
                    vis[i][j] = 1

        while rotten and fresh > 0:
            l = len(rotten)
            for _ in range(l):
                r,c = rotten.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < n and 0 <= nc < m and vis[nr][nc] == 0 and grid[nr][nc] == 1:
                        vis[nr][nc] = 1
                        rotten.append((nr,nc))
                        fresh -= 1
            minutes += 1


        return minutes if fresh == 0 else -1
        

