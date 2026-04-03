class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        for num in numset:
            if num - 1 not in numset:
                start = num
                l = 0
                while start in numset:
                    l += 1
                    start += 1
                
                ans = max(l,ans)
        return ans