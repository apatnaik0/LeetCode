class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        bp=prices[0]
        for i in prices:
            if i>bp:
                p+= i-bp
            bp = i
        return p
        