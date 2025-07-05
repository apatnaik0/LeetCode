class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            prev = arr[0]
            prev2 = 0
            for i in range(1,len(arr)):
                pick = arr[i]
                if i>1:
                    pick += prev2
                nonpick = prev
                cur = max(pick,nonpick)
                prev2 = prev
                prev = cur
            return prev
        if len(nums)==1:
            return nums[0]
        arr1 = []
        arr2 = []
        for i in range(len(nums)):
            if i!=0:
                arr1.append(nums[i])
            if i!=len(nums)-1:
                arr2.append(nums[i])
        return max(solve(arr1),solve(arr2))
