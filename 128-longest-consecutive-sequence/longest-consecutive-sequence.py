class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxi = 0
        s = set(nums)
        for i in s:
            if i-1 not in s:
                l = 1
                while i+1 in s:
                    l += 1
                    i += 1
                maxi = max(maxi,l)
        return maxi