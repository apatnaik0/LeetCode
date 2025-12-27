class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev2 = 1
        prev = 2

        for i in range(3,n+1):
            cur = prev + prev2
            prev2 = prev
            prev = cur
        return cur