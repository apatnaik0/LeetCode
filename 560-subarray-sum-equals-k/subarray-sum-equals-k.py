class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        hmap = defaultdict(int)
        hmap[0] = 1
        ans = 0

        for num in nums:
            prefix_sum += num
            res = prefix_sum - k
            if res in hmap:
                ans += hmap[res]
            hmap[prefix_sum] += 1
        
        return ans