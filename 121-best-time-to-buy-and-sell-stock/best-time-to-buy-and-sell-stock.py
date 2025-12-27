class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp = prices[0]
        n = len(prices)
        maxi = 0
        for i in range(1,n):
            if prices[i] > bp:
                maxi = max(maxi,prices[i]-bp)
            else:
                bp = prices[i]
        return maxi