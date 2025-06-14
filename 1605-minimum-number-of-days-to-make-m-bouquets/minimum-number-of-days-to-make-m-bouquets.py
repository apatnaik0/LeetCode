class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        if len(bloomDay)< m*k:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        ans = high

        def poss(days,mid,m,k):
            ct = 0
            boq = 0
            for i in days:
                if mid>=i:
                    ct+=1
                else:
                    boq+= ct//k
                    ct=0
            boq+= ct//k
            if boq>=m:
                return True
            else:
                return False

        while low<=high:
            mid = (low+high)//2
            if poss(bloomDay,mid,m,k):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        