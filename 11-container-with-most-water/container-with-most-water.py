class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        ans = 0
        while l<r:
            if height[l] < height[r]:
                ans = max(ans,(r-l)* height[l])
                l += 1
            else:
                ans = max(ans,(r-l)* height[r])
                r -= 1
        return ans