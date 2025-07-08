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
        prev = [0 for _ in range(n+1)]
        # return solve(n-1,n-1)
        # for i in range(n+1):
        #     dp[i][0] = 0
        #     dp[0][i] = 0
        # prev[0] = 0
        for i1 in range(1,n+1):
            cur = [0 for _ in range(n+1)]
            for i2 in range(1,n+1):
                if s[i1-1]==rs[i2-1]:
                    cur[i2] = 1 + prev[i2-1]
                else:
                    cur[i2] = max(cur[i2-1],prev[i2])
            prev = cur[:]
        return prev[n]