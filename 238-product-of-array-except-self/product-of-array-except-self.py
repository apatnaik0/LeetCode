class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1]*n
        suffix_product = [1]*n
    
        pre = 1
        for i in range(1,n):
            pre = pre * nums[i-1]
            prefix_product[i] = pre
        
        # print(prefix_product)
        
        suf = 1
        for i in range(n-2,-1,-1):
            suf = suf * nums[i+1]
            suffix_product[i] = suf

        # print(suffix_product)
        
        ans = [0]*n
        for i in range(n):
            ans[i] = prefix_product[i] * suffix_product[i]

        return ans
