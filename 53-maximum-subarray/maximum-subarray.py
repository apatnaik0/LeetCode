class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tsum = 0
        ans = nums[0]
        for i in nums:
            tsum += i
            ans = max(ans,tsum)
            if tsum < 0:
                tsum = 0
        return ans