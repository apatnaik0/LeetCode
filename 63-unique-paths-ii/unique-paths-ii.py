class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def solve(i,j,dp):
            if i>=0 and j>=0 and obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            up = solve(i-1,j,dp)
            left = solve(i,j-1,dp)
            dp[i][j] = up + left
            return dp[i][j]

        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        return solve(len(obstacleGrid)-1,len(obstacleGrid[0])-1,dp)