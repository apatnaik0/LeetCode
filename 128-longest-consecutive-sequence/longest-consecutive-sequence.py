class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for num in s:
            if num-1 not in s:
                l = 1
                while num+1 in s:
                    l += 1
                    num += 1
                maxi = max(maxi,l)
        
        return maxi