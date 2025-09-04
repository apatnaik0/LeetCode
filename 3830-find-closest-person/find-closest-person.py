class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dis12 = abs(z-x)
        dis23 = abs(z-y)
        if dis12 < dis23:
            return 1
        elif dis12 > dis23:
            return 2
        return 0