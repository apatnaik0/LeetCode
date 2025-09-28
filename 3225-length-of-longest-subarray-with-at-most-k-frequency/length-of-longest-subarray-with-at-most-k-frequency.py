class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        l = 0
        ans = 0
        for r in range(len(nums)):
            hmap[nums[r]] += 1
            while hmap[nums[r]]>k:
                hmap[nums[l]] -= 1
                l += 1
            # print(hmap,l,r)
            ans = max(ans, r-l+1)
            # print(ans)
        return ans