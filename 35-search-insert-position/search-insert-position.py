class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = high+1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=target:
                ans = min(mid,ans)
                high=mid-1
            else:
                low=mid+1
        return ans