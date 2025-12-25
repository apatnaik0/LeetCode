class Solution:
    def solve(self,nums,t,i,dp):
        if i == 0:
            return t == nums[0]
        if t == 0:
            return True
        if dp[i][t]!=-1:
            return dp[i][t]
        pick = False
        if t >= nums[i]:
            pick = self.solve(nums,t-nums[i],i-1,dp)
        not_pick = self.solve(nums,t,i-1,dp)
        dp[i][t] = pick or not_pick
        return dp[i][t]

    def canPartition(self, nums: List[int]) -> bool:
        s = 0
        for i in nums:
            s += i
        if s%2 != 0:
            return False
        n = len(nums)
        dp = [[-1 for _ in range(s//2+1)] for _ in range(n)]
        return self.solve(nums,s//2,n-1,dp)
