class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        
        while low<=high:
            mid = (low+high)//2
            # print(low,mid,high)
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[low]:
                # print('left sorted')
                if target >= nums[low] and target < nums[mid]:
                    # print('in sorted')
                    high = mid - 1
                    # print(low,high)
                else:
                    # print('not in sorted')
                    low = mid + 1
                    # print(low,high)
            elif nums[high] >= nums[mid]:
                # print('right sorted')
                if target > nums[mid] and target <= nums[high]:
                    # print('in sorted')
                    low = mid + 1
                    # print(low,high)
                else:
                    # print('not in sorted')
                    high = mid - 1
                    # print(low,high)
        return -1