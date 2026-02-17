class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn == 0:
            return ['0:00']

        q = (1 << turnedOn) - 1
        maxi = q << (10-turnedOn)
        mask = (1<<6)-1
        ans = []
        while q <= maxi:
            minute = q & mask
            hour = q>>6
            if hour < 12 and minute < 60:
                ans.append(f'{hour}:{minute:0>2}')
            r = q & -q
            n = q + r
            q = (((q^n)//r) >> 2) | n
        return ans