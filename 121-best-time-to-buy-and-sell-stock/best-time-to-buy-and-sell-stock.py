class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        p, mp = 0,0
        for i in prices:
            if i > bp:
                p = i - bp
                mp = max(mp,p)
            else:
                bp = i
        return mp