class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        mfreq = 0
        for i in nums:
            hmap[i] += 1
            mfreq = max(mfreq,hmap[i])
        ct = 0
        for i in hmap:
            if hmap[i] == mfreq:
                ct+=1
        return mfreq*ct