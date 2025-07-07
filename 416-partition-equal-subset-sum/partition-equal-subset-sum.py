class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def solve(ind,t):
            if t==0:
                return True
            if ind==0:
                return nums[0]==t
            
            if dp[ind][t]!=-1:
                return dp[ind][t]
            
            notpick = solve(ind-1,t)
            pick = False
            if nums[ind]<=t:
                pick = solve(ind-1,t-nums[ind])
            dp[ind][t] = pick or notpick
            return dp[ind][t]
        
        s = 0
        for i in nums:
            s += i
        if s%2:
            return False
        dp = [[-1 for _ in range(s//2+1)] for _ in range(len(nums))]
        return solve(len(nums)-1,s//2)

            