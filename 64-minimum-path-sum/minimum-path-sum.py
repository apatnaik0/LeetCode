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
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        # return self.solve(grid,m-1,n-1,dp)
        for i in range(m+1):
            dp[i][0] = float('inf')
        for j in range(n+1):
            dp[0][j] = float('inf')
        # dp[1][1] = grid[0][0]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i == 1 and j == 1:
                    dp[1][1] = grid[0][0]
                else:
                    up = grid[i-1][j-1] + dp[i-1][j]
                    left = grid[i-1][j-1] + dp[i][j-1]
                    dp[i][j] = min(up,left)
        print(dp)
        return dp[m][n]