class Solution:
    def compressedString(self, word: str) -> str:
        ans = ''
        ct = 0
        can = ''
        for i in word:
            if can == '':
                can = i
            if i == can:
                ct += 1
                if ct == 9:
                    ans += str(ct) + can
                    can = ''
                    ct = 0
            else:
                ans += str(ct) + can
                can = i
                ct = 1
        if ct > 0:
            ans += str(ct) + can
        return ans
