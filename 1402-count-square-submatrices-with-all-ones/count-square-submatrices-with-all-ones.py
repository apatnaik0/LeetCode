class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(n):
            dp[0][i] = matrix[0][i]
            ans += dp[0][i]
        for i in range(1,m):
            dp[i][0] = matrix[i][0]
            ans += dp[i][0]
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 1:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    ans += dp[i][j]
        print(dp)
        return ans