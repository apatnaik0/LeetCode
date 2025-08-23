class Solution:
    def minarea(self,mat):
        if not mat or not mat[0]:
            return 0
        n,m = len(mat), len(mat[0])
        l,r,t,b = float('inf'), -1, float('inf'), -1
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    l = min(l,j)
                    r = max(r,j)
                    t = min(t,i)
                    b = max(b,i)
        if r == -1:
            return 0
        return (r-l+1)*(b-t+1)

    def rotate(self,mat):
        n,m = len(mat), len(mat[0])
        return [[mat[i][j] for i in range(n-1,-1,-1)] for j in range(m)]

    def minimumSum(self, grid: List[List[int]]) -> int:
        ans = float('inf')
        for _ in range(4):
            n,m = len(grid), len(grid[0])
            for i in range(1,n):
                a1 = self.minarea(grid[:i])
                for j in range(1,m):
                    a2 = self.minarea([row[:j] for row in grid[i:]])
                    a3 = self.minarea([row[j:] for row in grid[i:]])
                    ans = min(ans,a1+a2+a3)
                for i2 in range(i+1,n):
                    a2 = self.minarea(grid[i:i2])
                    a3 = self.minarea(grid[i2:])
                    ans = min(ans,a1+a2+a3)
            grid = self.rotate(grid)
        return ans