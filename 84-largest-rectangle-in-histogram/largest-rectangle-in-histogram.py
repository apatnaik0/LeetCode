class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while st and heights[st[-1]] > heights[i]:
                bar = st.pop()
                pse = st[-1] if st else -1
                nse = i
                area = heights[bar] * (nse - pse - 1)
                max_area = max(max_area, area)
            st.append(i)
        
        while st:
            bar = st.pop()
            pse = st[-1] if st else -1
            nse = n
            area = heights[bar] * (nse - pse - 1)
            max_area = max(max_area, area)

        return max_area