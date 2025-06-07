class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        maxp = 0
        for i in prices:
            if i > bp:
                p = i-bp
                maxp = max(p,maxp)
            else:
                bp = i
        return maxp
        