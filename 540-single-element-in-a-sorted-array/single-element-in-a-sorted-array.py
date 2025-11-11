class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[n-1]!= nums[n-2]:
            return nums[n-1]
        
        l = 1
        r = n-2
        while l<=r:
            mid = (l+r)//2
            if nums[mid] != nums[mid-1] and nums[mid]!= nums[mid+1]:
                    return nums[mid]
            if mid%2 == 0:
                if nums[mid] == nums[mid+1]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[mid] == nums[mid-1]:
                    l = mid+1
                else:
                    r = mid-1
        