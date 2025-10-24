class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cd = nums[0]
        ct = 0
        for i in nums:
            if ct == 0:
                cd = i
            if i == cd:
                ct += 1
            else:
                ct -= 1
        return cd
            

        