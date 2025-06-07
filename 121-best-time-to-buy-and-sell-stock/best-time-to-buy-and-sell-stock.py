class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        mp = 0
        for i in prices:
            if i > bp:
                p = i-bp
                mp = max(p,mp)
            else:
                bp = i
        return mp
        