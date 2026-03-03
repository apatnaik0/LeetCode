class Solution:
    def invert(self,s):
        new_s = ''
        for c in s:
            if c == '1':
                new_s += '0'
            else:
                new_s += '1'
        return new_s

    def findKthBit(self, n: int, k: int) -> str:
        s = '0'

        for i in range(n):
            s = s + '1' + self.invert(s[::-1])
            # print(s)
        return s[k-1]