class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # def solve(i,j):
        #     if j<0 or j>=n:
        #         return int(1e9)
        #     if i==0:
        #         return matrix[i][j]
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     up = matrix[i][j] + solve(i-1,j)
        #     ld = matrix[i][j] + solve(i-1,j-1)
        #     rd = matrix[i][j] + solve(i-1,j+1)
        #     dp[i][j] = min(up,ld,rd)
        #     return dp[i][j]
        mini = int(1e9)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        # for i in range(n):
        #     mini = min(mini,solve(n-1,i))
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1,n):
            for j in range(n):
                up = matrix[i][j] + dp[i-1][j]
                ld = matrix[i][j] 
                if j>0:
                    ld += dp[i-1][j-1]
                else:
                    ld += int(1e9)
                rd = matrix[i][j]
                if j<n-1:
                    rd += dp[i-1][j+1]
                else:
                    rd += int(1e9)
                dp[i][j] = min(up,ld,rd)
            
        for i in range(n):
            mini = min(mini,dp[n-1][i])
        return mini
            
        