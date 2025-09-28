class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        peri = 0
        n = len(nums)
        for i in range(n-1,1,-1):
            l = 0
            r = i-1
            while l<r:
                if nums[l] + nums[r] > nums[i]:
                    peri = nums[r-1] + nums[r] + nums[i]
                    return peri
                else:
                    l += 1
        return 0
