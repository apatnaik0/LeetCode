class Solution:
    def rec(self,i,nums,ans,sub):
        ans.append(sub[:])
        for ix in range(i,len(nums)):
            if ix>i and nums[ix]==nums[ix-1]:
                continue
            sub.append(nums[ix])
            self.rec(ix+1,nums,ans,sub)
            sub.pop()
        return ans

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        sub = []
        i = 0
        ans = self.rec(i,nums,ans,sub)
        return ans