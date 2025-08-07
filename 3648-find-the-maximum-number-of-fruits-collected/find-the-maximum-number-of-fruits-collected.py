class Solution:
    def init(self,n,dp):
        for i in range(n):
            for j in range(n):
                if i + j < n - 1:
                    dp[i][j] = 0  # Upper-left triangle → invalid region
                else:
                    dp[i][j] = -1  # Valid region to be filled via DP

    def solve2(self,i,j,dp,n,fruits):
        if i<0 or i>=n or j<0 or j>=n:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j] = fruits[i][j] + max(self.solve2(i-1,j+1,dp,n,fruits), self.solve2(i-1,j,dp,n,fruits), self.solve2(i-1,j-1,dp,n,fruits))
        return dp[i][j]

    def solve3(self,i,j,dp,n,fruits):
        if i<0 or i>=n or j<0 or j>=n:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        dp[i][j] = fruits[i][j] + max(self.solve3(i,j-1,dp,n,fruits), self.solve3(i-1,j-1,dp,n,fruits), self.solve3(i+1,j-1,dp,n,fruits))
        return dp[i][j]

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:

        n = len(fruits)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        ans1 = sum(fruits[i][i] for i in range(n))
        self.init(n,dp)
        ans2 = self.solve2(n-2,n-1,dp,n,fruits)
        self.init(n,dp)
        ans3 = self.solve3(n-1,n-2,dp,n,fruits)
        
        # print(ans1,ans2,ans3)
        return ans1+ans2+ans3
        