class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = nums[0]
        s=0
        for i in range(len(nums)):
            s += nums[i]
            ms = max(ms,s)
            if s<0:
                s=0
        return ms



        