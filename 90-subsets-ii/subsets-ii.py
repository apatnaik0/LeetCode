class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def rec(ind):
            ans.append(sub[:])
            for i in range(ind,len(nums)):
                if i!=ind and nums[i]==nums[i-1]:
                    continue
                sub.append(nums[i])
                rec(i+1)
                sub.pop()
        ans = []
        sub = []
        nums.sort()
        rec(0)
        return ans
        