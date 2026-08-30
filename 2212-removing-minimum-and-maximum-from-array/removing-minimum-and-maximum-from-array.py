class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini = float('inf')
        mini_ind = -1
        maxi = float('-inf')
        maxi_ind = -1
        n = len(nums)
        for i in range(n):
            if nums[i]>maxi:
                maxi = nums[i]
                maxi_ind = i
            if nums[i]<mini:
                mini = nums[i]
                mini_ind = i

        return min(max(mini_ind,maxi_ind)+1,n-min(mini_ind,maxi_ind),min(mini_ind,maxi_ind)+1 + n-max(mini_ind,maxi_ind))
        