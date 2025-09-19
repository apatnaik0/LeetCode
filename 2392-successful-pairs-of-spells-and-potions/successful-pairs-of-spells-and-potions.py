class Solution:
    def bs(self,potions,n,spell,success):
        low = 0
        high = n-1
        ans = 0
        while low<=high:
            mid = (low+high)//2
            if potions[mid]*spell>=success:
                ans = n-mid
                high = mid-1
            else:
                low = mid+1
        return ans

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        p = len(potions)
        ans = [0]*len(spells)
        for i in range(len(spells)):
            ans[i] = self.bs(potions,p,spells[i],success)
        return ans