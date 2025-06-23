class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        area = 0
        for i in range(len(heights)):
            while st and heights[i]<heights[st[-1]]:
                bar = st.pop()
                pse = st[-1] if st else -1
                nse = i
                area = max(area,heights[bar]*(nse-pse-1))
            st.append(i)

        while st:
            bar = st.pop()
            pse = st[-1] if st else -1
            nse = len(heights)
            area = max(area,heights[bar]*(nse-pse-1))
            
        return area
        