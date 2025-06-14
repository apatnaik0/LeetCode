import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        def total(piles,n):
            tot = 0
            for i in piles:
                tot+= math.ceil(float(i)/n)
            return tot
        while low<=high:
            mid = (low+high)//2
            tot = total(piles,mid)
            if tot<=h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
