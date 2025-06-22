class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        def getnse(arr):
            n = len(arr)
            st = []
            nse = [n]*(n)
            for i in range(n-1,-1,-1):
                while st and arr[i]<arr[st[-1]]:
                    st.pop()
                nse[i] = st[-1] if st else n
                st.append(i)
            return nse
        
        def getpse(arr):
            n = len(arr)
            st = []
            pse = [-1]*(n)
            for i in range(n):
                while st and arr[i]<=arr[st[-1]]:
                    st.pop()
                pse[i] = st[-1] if st else -1
                st.append(i)
            return pse

        def getnge(arr):
            n = len(arr)
            st = []
            nge = [n]*(n)
            for i in range(n-1,-1,-1):
                while st and arr[i]>arr[st[-1]]:
                    st.pop()
                nge[i] = st[-1] if st else n
                st.append(i)
            return nge
        
        def getpge(arr):
            n = len(arr)
            st = []
            pge = [-1]*(n)
            for i in range(n):
                while st and arr[i]>=arr[st[-1]]:
                    st.pop()
                pge[i] = st[-1] if st else -1
                st.append(i)
            return pge

        nse = getnse(nums)
        pse = getpse(nums)
        nge = getnge(nums)
        pge = getpge(nums)

        mini = 0
        maxi = 0

        for i in range(len(nums)):
            ls = i - pse[i]
            rs = nse[i] - i
            mini += ls*rs*nums[i]
            lg = i - pge[i]
            rg = nge[i] - i
            maxi += lg*rg*nums[i]

        return maxi-mini
