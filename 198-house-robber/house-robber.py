class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = nums[0]
        prev2 = 0
        for i in range(1,len(nums)):
            pick = nums[i]
            if i>1:
                pick += prev2
            nonpick = prev
            cur = max(pick,nonpick)
            prev2 = prev
            prev = cur
        return prev