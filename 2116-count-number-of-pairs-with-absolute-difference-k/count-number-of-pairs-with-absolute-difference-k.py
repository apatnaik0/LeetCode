class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        for i in nums:
            hmap[i] += 1
        ct = 0
        for i in hmap:
            if i+k in hmap:
                ct += hmap[i+k] * hmap[i]
        return ct