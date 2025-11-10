class Solution:
    # def next_permutation(self,nums):
    #     piv = -1
    #     n = len(nums)
    #     for i in range(n-2,-1,-1):
    #         if nums[i] < nums[i+1]:
    #             piv = i
    #             break
        
    #     if piv == -1:
    #         return nums[::-1]
        
    #     for i in range(n-1,piv,-1):
    #         if nums[i]>= nums[piv]:
    #             nums[i], nums[piv] = nums[piv], nums[i]
    #             break
        
    #     l = piv+1
    #     r = n-1
    #     while l<r:
    #         nums[l], nums[r] = nums[r], nums[l]
    #         l+=1
    #         r-=1
        
    #     return nums

    def rec(self,ind,nums,ans):
        if ind == len(nums):
            ans.append(nums[:])
            return ans
        
        for i in range(ind,len(nums)):
            nums[i], nums[ind] = nums[ind], nums[i]
            self.rec(ind+1, nums, ans)
            nums[i], nums[ind] = nums[ind], nums[i]
        
        return ans


    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # ans = []
        # ans.append(nums[:])
        # print(ans)
        # while True:
        #     new_nums = self.next_permutation(nums)
        #     if new_nums == ans[0]:
        #         break
        #     ans.append(new_nums[:])
        #     nums = new_nums
        #     print(ans)
        ans = []
        ans = self.rec(0,nums,ans)
        return ans