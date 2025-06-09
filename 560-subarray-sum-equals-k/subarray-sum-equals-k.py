class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ct = {}
        ct[0]=1
        presum=0
        tot=0
        for i in nums:
            presum += i
            rem = presum-k
            if rem in ct:
                tot+=ct[rem]
            if presum in ct:
                ct[presum]+=1
            else:
                ct[presum]=1
        return tot
            