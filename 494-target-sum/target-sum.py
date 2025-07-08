class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # def solve(ind,tar):
        #     if ind == 0:
        #         if tar==0 and nums[ind]==0:
        #             return 2
        #         if tar==0 or tar==nums[ind]:
        #             return 1
        #         return 0
        #     if dp[ind][tar]!=-1:
        #         return dp[ind][tar]
        #     notpick = solve(ind-1,tar)
        #     pick = 0
        #     if tar>=nums[ind]:
        #         pick = solve(ind-1,tar-nums[ind])
        #     dp[ind][tar] = pick + notpick
        #     return dp[ind][tar]
        n = len(nums)
        s = 0
        for i in nums:
            s += i
        tar = (s+target)
        if s<target or target<-s:
            return 0
        if tar%2!=0:
            return 0
        tar = tar//2
        dp = [[0 for _ in range(tar+1)] for _ in range(n)]
        for i in range(tar+1):
            if i==0 and nums[0]==0:
                dp[0][i] = 2
            elif i == 0 or i == nums[0]:
                dp[0][i] = 1

        for i in range(1,n):
            for j in range(tar+1):
                notpick = dp[i-1][j]
                pick = 0
                if j>=nums[i]:
                    pick = dp[i-1][j-nums[i]]
                dp[i][j] = pick + notpick
        return dp[n-1][tar]

        