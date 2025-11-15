class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        maxi = 0
        for i in range(n):
            while st and heights[i] < heights[st[-1]]:
                bar = st.pop()
                pse = st[-1] if st else -1
                nse = i
                area = heights[bar] * (nse-pse-1)
                # print(nse,pse,bar,area)
                maxi = max(area,maxi)
            st.append(i)
        
        while st:
            bar = st.pop()
            pse = st[-1] if st else -1
            nse = n
            area = heights[bar]* (nse-pse-1)
            maxi = max(area,maxi)
        
        return maxi
