class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        inc, prevInc, ans = 1,0,0
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                prevInc = inc
                inc = 1
            ans = max(ans, max(inc//2,min(inc,prevInc)))
        return ans
