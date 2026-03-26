class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        low = 0
        high = n-1
        leftmax = 0
        rightmax = 0
        total = 0

        while low < high:

            leftmax = max(leftmax,height[low])
            rightmax = max(rightmax,height[high])

            if leftmax < rightmax:
                total += leftmax - height[low]
                low += 1
            else:
                total += rightmax - height[high]
                high -= 1
        
        return total
