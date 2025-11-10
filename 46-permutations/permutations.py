class Solution:
    def next_permutation(self,nums):
        piv = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                piv = i
                break
        
        if piv == -1:
            return nums[::-1]
        
        for i in range(n-1,piv,-1):
            if nums[i]>= nums[piv]:
                nums[i], nums[piv] = nums[piv], nums[i]
                break
        
        l = piv+1
        r = n-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        
        return nums


    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        ans.append(nums[:])
        print(ans)
        while True:
            new_nums = self.next_permutation(nums)
            if new_nums == ans[0]:
                break
            ans.append(new_nums[:])
            nums = new_nums
            print(ans)
        
        return ans