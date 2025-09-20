class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        pre = [0]*n
        st = []
        for i in range(n):
            if len(st)>=k:
                pre[i] = True
            if not st:
                st.append(nums[i])
            else:
                if nums[i]<=st[-1]:
                    st.append(nums[i])
                else:
                    st = [nums[i]]
        ans = []
        st = []
        for i in range(n-1,-1,-1):
            if len(st)>=k and pre[i]:
                ans.append(i)
            if not st:
                st.append(nums[i])
            else:
                if nums[i]<=st[-1]:
                    st.append(nums[i])
                else:
                    st = [nums[i]]
        return ans[::-1]

