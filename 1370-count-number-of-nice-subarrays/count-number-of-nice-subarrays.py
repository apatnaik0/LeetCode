class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        def solve(g):
            if g<0:
                return 0
            l = 0
            r = 0
            s = 0
            ct = 0
            while r<len(nums):
                s += (nums[r]%2)
                while s>g:
                    s -= nums[l]%2
                    l += 1
                ct += r-l+1
                r +=1
            return ct
        return solve(k) - solve(k-1)
                