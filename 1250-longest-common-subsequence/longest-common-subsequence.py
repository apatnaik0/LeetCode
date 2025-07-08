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
        # dp = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]
        # return solve(n1-1,n2-1)
        prev = [0 for _ in range(n2+1)]
        # for i in range(n2+1):
        #     dp[0][i] = 0
        # for i in range(n1+1):
        #     dp[i][0] = 0
        prev[0] = 0
        for i in range(1,n1+1):
            cur = [0 for _ in range(n2+1)]
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(prev[j],cur[j-1])
            prev = cur
        return prev[n2]