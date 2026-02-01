class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for i in s:
            if i-1 not in s:
                l = 1
                num = i
                while num+1 in s:
                    l += 1
                    num += 1
                maxi = max(l,maxi)
        return maxi