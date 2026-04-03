class Solution:

    def valid(self,rate,piles,hours):
        time = 0
        for pile in piles:
            time += ceil(pile/rate)
        
        return time <= hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)
        ans = 0

        while low <= high:
            mid = (low +high)//2
            if self.valid(mid,piles,h):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        
        return ans