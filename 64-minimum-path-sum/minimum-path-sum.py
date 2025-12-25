class Solution:
    def solve(self,grid,i,j,dp):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]
        up = grid[i][j] + self.solve(grid,i-1,j,dp)
        left = grid[i][j] + self.solve(grid,i,j-1,dp)
        dp[i][j] = min(up,left)
        return dp[i][j]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.solve(grid,m-1,n-1,dp)