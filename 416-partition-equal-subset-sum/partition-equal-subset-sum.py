class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # def solve(ind,t):
        #     if t==0:
        #         return True
        #     if ind==0:
        #         return nums[0]==t
            
        #     if dp[ind][t]!=-1:
        #         return dp[ind][t]
            
        #     notpick = solve(ind-1,t)
        #     pick = False
        #     if nums[ind]<=t:
        #         pick = solve(ind-1,t-nums[ind])
        #     dp[ind][t] = pick or notpick
        #     return dp[ind][t]
        
        s = 0
        for i in nums:
            s += i
        if s%2:
            return False
        prev = [False for _ in range(s//2+1)]
        # return solve(len(nums)-1,s//2)
        for i in range(len(nums)):
            prev[0] = True
        if nums[0]<=s//2+1:
            prev[nums[0]] = True
    
        for i in range(1,len(nums)):
            cur = [False for _ in range(s//2+1)]
            for j in range(1,s//2+1):
                pick = False
                if nums[i]<=j:
                    pick = prev[j-nums[i]]
                notpick = prev[j]
                cur[j] = pick or notpick
            prev = cur
        return prev[s//2]

            