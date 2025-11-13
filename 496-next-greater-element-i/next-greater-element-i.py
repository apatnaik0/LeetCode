class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        st = []
        n = len(nums2)
        for i in range(n-1,-1,-1):
            if not st:
                st.append(nums2[i])
                nge[nums2[i]] = -1
            else:
                while st and st[-1] < nums2[i]:
                    st.pop()
                if not st:
                    nge[nums2[i]] = -1
                    st.append(nums2[i])
                else:
                    nge[nums2[i]] = st[-1]
                    st.append(nums2[i])
        ans = []
        for i in nums1:
            ans.append(nge[i])
        
        return ans
