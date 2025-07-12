class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def solve(i,j):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            maxi = float('-inf')
            for k in range(i,j+1):
                ans = nums[i-1] * nums[k] * nums[j+1] + solve(i,k-1) + solve(k+1,j)
                maxi = max(maxi,ans)
            dp[i][j] = maxi
            return dp[i][j]
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
        # return solve(1,n)
        for i in range(n,0,-1):
            for j in range(i,n+1):
                maxi = float('-inf')
                for k in range(i,j+1):
                    ans = nums[i-1]* nums[k] * nums[j+1] + dp[i][k-1] + dp[k+1][j]
                    maxi = max(maxi,ans)
                dp[i][j] = maxi
        return dp[1][n]
