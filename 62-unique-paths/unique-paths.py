class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def solve(i,j,dp):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            left = solve(i-1,j,dp)
            up = solve(i,j-1,dp)
            dp[i][j] = left + up
            return dp[i][j]
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1
        return solve(m-1,n-1,dp)
        