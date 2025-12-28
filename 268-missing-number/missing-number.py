class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # n = len(nums)
        # tot = n*(n+1)//2
        # for i in nums:
        #     tot-=i
        # return tot

        xor1 = 0
        xor2 = 0
        n = len(nums)
        for i in range(n):
            xor1 = xor1^nums[i]
            xor2 = xor2^(i+1)
        return xor1^xor2