class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        ans = 0

        hmap = defaultdict(int)
        hmap[0] = 1
        for num in nums:
            prefix_sum += num
            rem = prefix_sum - k
            if rem in hmap:
                ans += hmap[rem]
            hmap[prefix_sum] += 1


        return ans