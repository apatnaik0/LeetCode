class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        maxi = 0
        while l < r:
            if height[l] < height[r]:
                maxi = max(maxi,height[l]*(r-l))
                l += 1
            else:
                maxi = max(maxi,height[r]*(r-l))
                r -= 1
        return maxi