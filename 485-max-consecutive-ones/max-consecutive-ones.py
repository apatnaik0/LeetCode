class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ml = 0
        l = 0
        for i in nums:
            if i == 1:
                l += 1
                ml = max(ml,l)
            else:
                l = 0
        return ml