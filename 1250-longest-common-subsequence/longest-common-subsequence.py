class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        def solve(i1,i2):
            if i1<0 or i2<0:
                return 0
            if dp[i1][i2]!=-1:
                return dp[i1][i2]
            if text1[i1]==text2[i2]:
                dp[i1][i2] = 1 + solve(i1-1,i2-1)
            else:
                dp[i1][i2] = max(solve(i1,i2-1),solve(i1-1,i2))
            return dp[i1][i2]
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return solve(n1-1,n2-1)