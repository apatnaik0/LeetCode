class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums):
            low = 0
            high = len(nums)-1
            first = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==target:
                    first = mid
                    high = mid-1
                elif nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            return first
        def last(nums):
            low = 0
            high = len(nums)-1
            last = -1
            while low<=high:
                mid = (low+high)//2
                if nums[mid]==target:
                    last = mid
                    low = mid+1
                elif nums[mid]>target:
                    high = mid-1
                else:
                    low = mid+1
            return last
        
        first = first(nums)
        if first == -1:
            return [-1,-1]
        last = last(nums)
        return [first,last]
