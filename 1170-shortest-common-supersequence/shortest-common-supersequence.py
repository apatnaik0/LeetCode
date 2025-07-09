class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # def solve(i,j):
        #     if i==0 or j==0:
        #         return 0
        #     if dp[i][j]!=0:
        #         return dp[i][j]
        #     if str1[i-1]==str2[j-1]:
        #         dp[i][j] = 1 + solve(i-1,j-1)
        #     else:
        #         dp[i][j] = max(solve(i,j-1),solve(i-1,j))
        #     return dp[i][j]
        n1 = len(str1)
        n2 = len(str2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        # solve(n1,n2)
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        i = n1
        j = n2
        ans = ""
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                ans += str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                ans += str1[i-1]
                i-=1
            else:
                ans += str2[j-1]
                j-=1
        while i>0:
            ans += str1[i-1]
            i-=1
        while j>0:
            ans += str2[j-1]
            j-=1
        return ans[::-1]


