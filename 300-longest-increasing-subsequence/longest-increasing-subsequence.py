class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(i,pi):
            if i==n:
                return 0
            if dp[i][pi]!=-1:
                return dp[i][pi]
            ans = solve(i+1,pi)
            if pi==-1 or nums[i]>nums[pi]:
                ans = max(ans, 1 + solve(i+1,i))
            return ans
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        prev = [0 for _ in range(n+1)]
        # return solve(0,-1)
        for i in range(n-1,-1,-1):
            cur = [0 for _ in range(n+1)]
            for pi in range(i-1,-2,-1):
                cur[pi+1] = prev[pi+1]
                if pi==-1 or nums[i]>nums[pi]:
                    cur[pi+1] = max(cur[pi+1], 1 + prev[i+1])
            prev = cur
        return prev[0]
        
                

