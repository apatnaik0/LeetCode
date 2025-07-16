class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        ct = 0
        fresh = 0
        t = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j])
                    vis[i][j] = 1
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh==0:
            return 0
        
        while q:
            l = len(q)
            for i in range(l):
                node = q.popleft()
                r = node[0]
                c = node[1]
                delr = [-1,0,1,0]
                delc = [0,1,0,-1]
                for i in range(4):
                    nr = r+delr[i]
                    nc = c+delc[i]
                    if nc>=0 and nc<m and nr>=0 and nr<n and grid[nr][nc]==1 and vis[nr][nc]==0:
                        q.append([nr,nc])
                        vis[nr][nc]=1
                        ct+=1
                # print(q)
            t+=1
        print(ct,fresh,t)
        return t-1 if ct==fresh else -1
