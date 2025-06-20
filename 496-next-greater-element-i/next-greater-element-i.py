class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        st = []
        for i in range(len(nums2)-1,-1,-1):
            if len(st)==0:
                st.append(nums2[i])
                nge[nums2[i]]=-1
            else:
                while len(st)!=0 and nums2[i]>st[-1]:
                    st.pop()
                if len(st)==0:
                    nge[nums2[i]]=-1
                    st.append(nums2[i])
                else:
                    nge[nums2[i]]=st[-1]
                    st.append(nums2[i])
        ans = []
        for i in nums1:
            ans.append(nge[i])
        return ans


