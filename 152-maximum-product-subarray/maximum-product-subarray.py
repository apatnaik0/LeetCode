class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suf = 1
        n = len(nums)
        maxi = nums[0]
        for i in range(n):
            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
            pre *= nums[i]
            suf *= nums[n-i-1]
            maxi = max(maxi,pre,suf)
        return maxi
