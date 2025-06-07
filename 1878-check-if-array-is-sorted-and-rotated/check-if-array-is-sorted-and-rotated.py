class Solution:
    def check(self, nums: List[int]) -> bool:
        ct = 0

        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                ct+=1
            if ct>1:
                return False
        return True