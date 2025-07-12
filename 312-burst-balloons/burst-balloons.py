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
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        return solve(1,n)