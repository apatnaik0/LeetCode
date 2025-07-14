class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def solve(g):
            if g<0:
                return 0
            l = 0
            r = 0
            ct = 0
            s = 0
            while r<n:
                s += nums[r]
                while s > g:
                    s -= nums[l]
                    l += 1
                if s<= g:
                    ct += r - l + 1
                r +=1
            return ct
        return solve(goal) - solve(goal-1)