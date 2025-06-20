class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ml = height[l]
        mr = height[r]
        tot = 0
        while l<=r:
            if height[l]<height[r]:
                if height[l]>ml:
                    ml = height[l]
                else:
                    tot += ml - height[l]
                l+=1
            else:
                if height[r]>mr:
                    mr = height[r]
                else:
                    tot += mr - height[r]
                r-=1
        return tot