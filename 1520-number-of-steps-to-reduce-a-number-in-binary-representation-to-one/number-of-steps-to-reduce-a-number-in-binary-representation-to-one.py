class Solution:

    def bin_to_int(self,s):
        n = len(s)
        ans = 0
        for i in range(n):
            ans += (2**i) * int(s[n-i-1])
        return ans

    def numSteps(self, s: str) -> int:
        n = self.bin_to_int(s)
        # print(n)
        steps = 0
        while n>1:
            if n % 2 == 0:
                n //= 2
            else:
                n += 1
            # print(n)
            steps += 1
        return steps
        