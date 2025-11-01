class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1=-1
        ele2=-1
        c1, c2 = 0,0
        for i in nums:
            if c1 == 0 and i != ele2:
                ele1 = i
                c1 = 1
            elif c2 == 0 and i!=ele1:
                ele2 = i
                c2 = 1
            elif i == ele1:
                c1 += 1
            elif i == ele2:
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
                
        ct1, ct2 = 0, 0
        for i in nums:
            if i == ele1:
                ct1+=1
            elif i == ele2:
                ct2 += 1
        ans = []
        if ct1 > len(nums)//3:
            ans.append(ele1)
        if ct2 > len(nums)//3:
            ans.append(ele2)
        return ans
        