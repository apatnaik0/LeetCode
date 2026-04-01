class Solution:
    def valid(self,rate,hours,piles):
        n = len(piles)
        time = 0
        for i in range(n):
            time += ceil(piles[i]/rate)
            
        return time <= hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        piles.sort()

        low = 1
        high = max(piles)
        ans = 0

        while low <= high:
            mid = (low + high)//2
            if self.valid(mid,h,piles):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans