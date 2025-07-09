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
        dp = [[0 for _ in range(n2)] for _ in range(n1)]
        lcs = solve(n1-1,n2-1)
        return n1 + n2 - 2*lcs