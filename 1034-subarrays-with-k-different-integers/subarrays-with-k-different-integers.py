class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def solve(goal):
            if goal<0:
                return 0
            vis = {}
            l = 0
            r = 0
            ct = 0
            while r<len(nums):
                vis[nums[r]] = 1 + vis.get(nums[r],0)
                while len(vis)>goal:
                    vis[nums[l]]-=1
                    if vis[nums[l]]==0:
                         del vis[nums[l]]
                    l += 1
                ct += r-l+1
                r+=1
            return ct
        return solve(k)-solve(k-1)