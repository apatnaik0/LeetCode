class Solution:
    def solve(self,i,pi,nums,n,dp):
        if i == n:
            return 0
        if dp[i][pi]!=-1:
            return dp[i][pi]
        ans = self.solve(i+1,pi,nums,n,dp)
        if pi == -1 or nums[i]>nums[pi]:
            ans = max(ans,1+ self.solve(i+1,i,nums,n,dp))
        dp[i][pi] = ans
        return ans
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # return self.solve(0,-1,nums,n,dp)
        for i in range(n-1,-1,-1):
            for pi in range(i-1,-2,-1):
                dp[i][pi+1] = dp[i+1][pi+1]
                if pi == -1 or nums[i]>nums[pi]:
                    dp[i][pi+1] = max(dp[i][pi+1],1+ dp[i+1][i+1])
        return dp[0][0]
