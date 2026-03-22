class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        area = 0

        while l < r:
            area = max(area,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1

        return area