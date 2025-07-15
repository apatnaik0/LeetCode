class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        c = n
        i = 1
        while i<n:
            if ratings[i-1]==ratings[i]:
                i += 1
            peak = 0
            while i<n and ratings[i]>ratings[i-1]:
                peak += 1
                c += peak
                i += 1
            valley = 0
            while i<n and ratings[i-1]>ratings[i]:
                valley += 1
                c += valley
                i += 1
            c -= min(peak,valley)
        return c
