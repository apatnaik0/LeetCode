class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ind = -1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break
            
        if ind == -1:
            return nums.reverse()
        
        for i in range(n-1,i,-1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        l = ind + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        

        


        
