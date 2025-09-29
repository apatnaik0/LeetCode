class Solution:
    def helper(self,dp,i,j,values,n):
        ans = 0
        if j == 0:
            j = n - 1
        if dp[i][j] != 0:
            return dp[i][j]
        for k in range(i+1,j):
            ans = min(ans if ans != 0 else float('inf'),self.helper(dp,i,k,values,n) + values[i]*values[j]*values[k] + self.helper(dp,k,j,values,n))
        dp[i][j] = ans
        return dp[i][j]

    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0 for _ in range(50)] for _ in range(50)]
        ans = self.helper(dp,0,0,values,n)
        return ans



