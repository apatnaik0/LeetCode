class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        t,b,l,r = -1,-1,-1,-1
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    t = i
                    break
            if t!=-1:
                break
        
        for i in range(n-1,-1,-1):
            for j in range(m):
                if grid[i][j]==1:
                    b = i
                    break
            if b!=-1:
                break

        for j in range(m):
            for i in range(n):
                if grid[i][j]==1:
                    l = j
                    break
            if l!=-1:
                break

        for j in range(m-1,-1,-1):
            for i in range(n):
                if grid[i][j]==1:
                    r = j
                    break
            if r!=-1:
                break
        
        return (b-t+1)*(r-l+1)
        