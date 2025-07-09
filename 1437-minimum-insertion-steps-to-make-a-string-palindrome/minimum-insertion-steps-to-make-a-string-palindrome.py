class Solution:
    def minInsertions(self, s: str) -> int:
        rs = s[::-1]
        n = len(s)
        def solve(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            if s[i]==rs[j]:
                dp[i][j] = 1 + solve(i-1,j-1)
            else:
                dp[i][j] = max(solve(i,j-1),solve(i-1,j))
            return dp[i][j]
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # pl = solve(n-1,n-1)
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s[i-1]==rs[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return n-dp[n][n]
