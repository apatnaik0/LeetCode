class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def solve(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=0:
                return dp[i][j]
            if word1[i]==word2[j]:
                dp[i][j] = 1 + solve(i-1,j-1)
            else:
                dp[i][j] = max(solve(i-1,j),solve(i,j-1))
            return dp[i][j]
        n1 = len(word1)
        n2 = len(word2)
        # dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        prev = [0 for _ in range(n2+1)]
        # lcs = solve(n1-1,n2-1)
        for i in range(1,n1+1):
            cur = [0 for _ in range(n2+1)]
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:
                    cur[j] = 1 + prev[j-1]
                else:
                    cur[j] = max(cur[j-1],prev[j])
            prev = cur
        return n1 + n2 - 2*prev[n2]