class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def solve(i,j):
            if j==0:
                return 1
            if i==0:
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            if s[i-1]==t[j-1]:
                dp[i][j] = solve(i-1,j-1) + solve(i-1,j)
            else:
                dp[i][j] = solve(i-1,j)
            return dp[i][j]

        n1 = len(s)
        n2 = len(t)
        # dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        prev = [0 for _ in range(n2+1)]
        prev[0] = 1
        # return solve(n1,n2)
        # for i in range(n1+1):
        #     dp[i][0] = 1
        # for i in range(1,n2+1):
        #     dp[0][i] = 0
        for i in range(1,n1+1):
            # cur = [0 for _ in range(n2+1)]
            # cur[0] = 1
            for j in range(n2,0,-1):
                if s[i-1]==t[j-1]:
                    prev[j] = prev[j-1] + prev[j]
                else:
                    prev[j] = prev[j]
            # prev = cur
        return prev[n2]
        