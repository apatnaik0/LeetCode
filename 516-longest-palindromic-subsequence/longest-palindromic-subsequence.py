class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        def solve(i1,i2):
            if i1<0 or i2<0:
                return 0
            if dp[i1][i2]!=-1:
                return dp[i1][i2]
            if s[i1]==rs[i2]:
                dp[i1][i2] = 1 + solve(i1-1,i2-1)
            else:
                dp[i1][i2] = max(solve(i1-1,i2),solve(i1,i2-1))
            return dp[i1][i2]

        rs = s[::-1]
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        return solve(n-1,n-1)