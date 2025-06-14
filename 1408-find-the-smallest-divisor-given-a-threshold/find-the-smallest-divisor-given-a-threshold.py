import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        if len(nums)>threshold:
            return -1
        
        low = 1
        high = max(nums)
        ans = high

        def poss(nums,d,lim):
            s = 0
            for i in nums:
                s += math.ceil(float(i)/d)
            if s<=lim:
                return True
            return False

        while low<=high:
            mid = (low+high)//2
            if poss(nums,mid,threshold):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans