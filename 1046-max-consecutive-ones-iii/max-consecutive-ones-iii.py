class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        z = 0
        ml = 0
        while r<n:
            if nums[r] == 0:
                z += 1
            if z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            else:
                ml = max(ml,r-l+1)
            r+=1
        return ml