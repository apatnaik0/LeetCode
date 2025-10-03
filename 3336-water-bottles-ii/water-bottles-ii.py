class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numEmpty = 0
        ans = 0
        while numBottles > 0:
            ans += numBottles
            numEmpty += numBottles
            numBottles = 0
            if numEmpty >= numExchange:
                numEmpty -= numExchange
                numExchange += 1
                numBottles += 1
            
        return ans