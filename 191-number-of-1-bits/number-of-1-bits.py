class Solution:
    def hammingWeight(self, n: int) -> int:
        ct = 0
        for i in range(32):
            if (n >> i) & 1:
                ct += 1

        return ct