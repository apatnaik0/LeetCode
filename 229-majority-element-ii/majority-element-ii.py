class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return [nums[0]]
        ct1=0
        ct2=0
        el1=-1
        el2=-1
        ans=[]
        mct = (len(nums)//3)+1
        for i in nums:
            if ct1==0 and i!=el2:
                el1=i
                ct1=1
            elif ct2==0 and i!=el1:
                el2=i
                ct2=1
            elif i==el1:
                ct1+=1
                
            elif i==el2:
                ct2+=1
                
            else:
                ct1-=1
                ct2-=1
        
        ct1=0
        ct2=0
        for i in nums:
            if i == el1:
                ct1+=1
            elif i == el2:
                ct2+=1
        if ct1>=mct:
            ans.append(el1)
        if ct2>=mct:
            ans.append(el2)

        return ans
        