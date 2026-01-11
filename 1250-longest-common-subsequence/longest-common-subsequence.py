class Solution:

    def solve(self,i,j,text1,text2,dp):

        if i < 0 or j < 0:
            return 0
        
        if dp[i][j] != 0:
            return dp[i][j]

        if text1[i]==text2[j]:
            ans = 1 + self.solve(i-1,j-1,text1,text2,dp)
        else:
            ans = max(self.solve(i-1,j,text1,text2,dp),self.solve(i,j-1,text1,text2,dp))
        dp[i][j] = ans
        return ans

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        # return self.solve(n1-1,n2-1,text1,text2,dp)
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    ans = 1 + dp[i-1][j-1]
                else:
                    ans = max(dp[i-1][j],dp[i][j-1])
                dp[i][j] = ans
        return dp[n1][n2]
