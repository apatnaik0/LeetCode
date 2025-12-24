class Solution:
    def solve(self,text1,text2,n1,n2,i,j,dp):
        if i<0 or j<0:
            return 0
        if dp[i][j]!=0:
            return dp[i][j]
        if text1[i] == text2[j]:
            ans = 1 + self.solve(text1,text2,n1,n2,i-1,j-1,dp)
        else:
            ans = max(self.solve(text1,text2,n1,n2,i-1,j,dp),self.solve(text1,text2,n1,n2,i,j-1,dp))
        return ans

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        # return self.solve(text1,text2,n1,n2,n1-1,n2-1,dp)
        prev = [0 for _ in range(n2+1)]
        for i in range(1,n1+1):
            curr = [0 for _ in range(n2+1)]
            for j in range(1,n2+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j] = max(prev[j],curr[j-1])
            prev = curr
        return curr[n2]