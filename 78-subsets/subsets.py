class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def rec(i):
            if i == len(nums):
                final.append(ans[:])
                return
            ans.append(nums[i])
            rec(i+1)
            ans.pop()
            rec(i+1)

        final = []
        ans = []
        rec(0)
        return final
        