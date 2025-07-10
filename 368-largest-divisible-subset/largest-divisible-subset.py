class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1]*n
        ha = [i for i in range(n)]
        maxi = int(-1e9)
        lastindex = 0
        for i in range(1,n):
            for j in range(i):
                if nums[i]%nums[j]==0 and 1+dp[j]>dp[i]:
                    dp[i] = dp[j] + 1
                    ha[i] = j
            if dp[i]>maxi:
                maxi = dp[i]
                lastindex = i
        
        ans = [nums[lastindex]]
        while lastindex!=ha[lastindex]:
            lastindex = ha[lastindex]
            ans.append(nums[lastindex])
        
        return ans[::-1]