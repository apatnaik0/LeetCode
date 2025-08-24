class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        l = 0
        r = 0
        ml = 0
        while r<len(nums):
            if nums[r]==0:
                zero +=1
                while zero>1:
                    if nums[l]==0:
                        zero -= 1
                    l += 1
            r += 1
            ml = max(ml,r-l+1)
        return ml-2
