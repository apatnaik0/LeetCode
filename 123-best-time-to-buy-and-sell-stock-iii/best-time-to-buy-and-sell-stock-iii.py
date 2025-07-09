class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        # dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        prev = [[0 for _ in range(3)] for _ in range(2)]
        for i in range(n-1,-1,-1):
            cur = [[0 for _ in range(3)] for _ in range(2)]
            for k in range(1,3):
                cur[1][k] = max(-prices[i]+prev[0][k],prev[1][k])
                cur[0][k] = max(prices[i]+prev[1][k-1],prev[0][k])
            prev = cur
        return prev[1][2]