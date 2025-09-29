class Solution:
    def helper(self,dp,i,j,values,n):
        ans = 0
        # if j == 0:
        #     j = n - 1
        if dp[i][j] != 0:
            return dp[i][j]
        for k in range(i+1,j):
            ans = min(ans if ans != 0 else float('inf'),self.helper(dp,i,k,values,n) + values[i]*values[j]*values[k] + self.helper(dp,k,j,values,n))
        dp[i][j] = ans
        return dp[i][j]

    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # Only intervals with length >= 3 matter (at least a triangle)
        for length in range(3, n+1):             # interval length
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')          # initialize large
                for k in range(i+1, j):          # try every possible third vertex
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k][j] + values[i]*values[j]*values[k]
                    )

        return dp[0][n-1]



