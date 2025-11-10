class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = []
        fact = 1
        for i in range(1,n):
            nums.append(i)
            fact *= i
        nums.append(n)
        
        k = k-1
        ans = ''
        while True:
            ind = int(k//fact)
            ans += str(nums[ind])
            nums.pop(ind)
            if len(nums)==0:
                break
            k %= fact
            fact /= len(nums)
        
        return ans