class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        conz = 0
        for i in nums:
            if i==0:
                conz +=1
                ans += conz
            else:
                conz = 0
        return ans