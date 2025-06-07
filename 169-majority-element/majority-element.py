class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct=0
        for i in nums:
            if ct==0:
                cd = i
            if cd == i:
                ct+=1
            else:
                ct-=1
        return cd
        ''
        