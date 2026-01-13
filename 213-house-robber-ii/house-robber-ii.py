class Solution:
    def solve(self,arr):
        prev = arr[0]
        prev2 = 0

        for i in range(1,len(arr)):
            pick = arr[i]
            if i >1 :
                pick += prev2
            notpick = prev
            cur = max(pick,notpick)
            prev2 = prev
            prev = cur
        
        return prev

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        arr1 = []
        arr2 = []
        if n == 1:
            return nums[0]
        
        for i in range(n):
            if i != 0:
                arr1.append(nums[i])
            if i != n-1:
                arr2.append(nums[i])
        
        return max(self.solve(arr1), self.solve(arr2))