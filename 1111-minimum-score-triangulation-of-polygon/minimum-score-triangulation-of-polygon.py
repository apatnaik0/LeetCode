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
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # ans = self.helper(dp,0,n-1,values,n)
        # return ans
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j] if dp[i][j]!=0 else float('inf'), dp[i][k] + dp[k][j] + values[i]*values[j]*values[k])
        return dp[0][n-1]



