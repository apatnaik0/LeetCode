class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        ct = [1]*n
        maxi = 1
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                    ct[i] = ct[j]
                elif nums[i]>nums[j] and dp[j]+1==dp[i]:
                    ct[i] += ct[j]
            maxi = max(maxi,dp[i])
        c = 0
        for i in range(n):
            if dp[i]==maxi:
                c += ct[i]
        return c