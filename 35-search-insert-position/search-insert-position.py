class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        low = 0
        high = n-1

        while low <= high:
            mid = (low +high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                ans = mid + 1
                low = mid + 1
            else:
                ans = mid
                high = mid-1

        return ans