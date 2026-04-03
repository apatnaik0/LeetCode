class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        # n = len(nums)
        ans = float('-inf')

        for num in nums:
            total += num
            ans = max(total,ans)
            if total < 0:
                total = 0
        
        return ans