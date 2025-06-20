class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        nge = []
        for i in range(2*len(nums)-1,-1,-1):
            j = i%len(nums)
            while len(st)!=0 and st[-1]<=nums[j]:
                st.pop()
            if i<len(nums):
                nge.append(-1 if len(st)==0 else st[-1])
            st.append(nums[j])
        return nge[::-1]
