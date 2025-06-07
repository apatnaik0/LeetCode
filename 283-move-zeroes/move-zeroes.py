class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        for i in range(0,len(nums)):
            if nums[k]==0:
                if nums[i]!=0:
                    nums[k],nums[i]=nums[i],nums[k]
                    k+=1
            else:
                k+=1
            # print(i,k,nums)
            

        