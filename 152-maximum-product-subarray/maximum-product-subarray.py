class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suf = 1
        maxi = nums[0]
        for i in range(len(nums)):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre *= nums[i]
            suf *= nums[len(nums)-1-i]
            maxi = max(maxi, max(pre,suf))
        return maxi

        