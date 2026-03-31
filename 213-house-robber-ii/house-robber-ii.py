class Solution:
    def helper(self,nums):
        prev = nums[0]
        prev2 = 0

        for i in range(1,len(nums)):
            pick = nums[i] + prev2
            notpick = prev
            cur = max(pick,notpick)
            prev2 = prev
            prev = cur

        return prev 

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.helper(nums[:n-1]),self.helper(nums[1:n]))
        