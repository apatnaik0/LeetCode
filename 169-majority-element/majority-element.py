class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # candidate = nums[0]
        ct = 0

        for i in nums:
            if ct == 0:
                candidate = i
            if i == candidate:
                ct += 1
            else:
                ct -= 1
        
        return candidate