class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ct = 0
        zct = 0
        ans = 0
        l = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == 1:
                ct += 1
            else:
                zct += 1
                while zct > k:
                    if nums[l] == 0:
                        zct -= 1
                    else:
                        ct -= 1
                    l += 1
        
            ans = max(ans,r-l+1)
        return ans