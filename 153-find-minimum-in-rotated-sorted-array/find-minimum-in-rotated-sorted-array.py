class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        mini = float('inf')

        if nums[low] <= nums[high]:
            return nums[0]

        while low <= high:
            mid = (low + high)//2
            
            if nums[mid] >= nums[low]:
                mini = min(mini,nums[low])
                low = mid + 1
            else:
                mini = min(mini,nums[mid])
                high = mid - 1
        
        return mini
