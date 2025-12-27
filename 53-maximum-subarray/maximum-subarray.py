class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tsum = 0
        maxi = float('-inf')
        for i in nums:
            tsum += i
            maxi = max(maxi,tsum)
            if tsum < 0:
                tsum = 0
        return maxi