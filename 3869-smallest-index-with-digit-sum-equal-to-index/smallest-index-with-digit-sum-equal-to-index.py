class Solution:
    def sumOfDigits(self,n):
        ans = 0
        while n>0:
            digit = n%10
            ans += digit
            n = n//10
        return ans

    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            s = self.sumOfDigits(nums[i])
            if i == s:
                return i
        return -1
        