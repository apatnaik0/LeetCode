class Solution:
    def solve(self,n,dp,pi,i,nums):
        if i == n:
            return 0
        
        if dp[pi][i] != 0:
            return dp[pi][i]
        
        pick = float('-inf')
        if pi == -1 or nums[i]>nums[pi]:
            pick = 1 + self.solve(n,dp,i,i+1,nums)
        not_pick = self.solve(n,dp,pi,i+1,nums)

        dp[pi][i] = max(pick,not_pick)
        return dp[pi][i]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        # return self.solve(n,dp,-1,0,nums)
        
        for i in range(n-1,-1,-1):
            for pi in range(i-1,-2,-1):
                pick = float('-inf')
                if pi == -1 or nums[i]>nums[pi]:
                    pick = 1 + dp[i+1][i+1]
                not_pick = dp[i+1][pi+1]

                dp[i][pi+1] = max(pick,not_pick)
        
        return dp[0][0]