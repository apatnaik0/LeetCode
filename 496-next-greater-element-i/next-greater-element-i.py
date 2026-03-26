class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nge = {}
        n = len(nums2)
        st = []

        for i in range(n-1,-1,-1):
            if not st:
                st.append(nums2[i])
                nge[nums2[i]] = -1
            else:
                while st and nums2[i] > st[-1]:
                    st.pop()
                if len(st)==0:
                    nge[nums2[i]] = -1
                    st.append(nums2[i])
                else:
                    nge[nums2[i]] = st[-1]
                    st.append(nums2[i])
        
        ans = []
        for i in nums1:
            ans.append(nge[i])
        return ans

