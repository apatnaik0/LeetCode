class Solution:
    def countCommas(self, n: int) -> int:
        if n <= 999:
            return 0

        commas = 0
        start = 1000
        end = start * 1000 - 1
        ct = 1

        while start <= n:
            nums = min(n,end) - start + 1
            commas += ct * nums

            if end > n:
                break
            start *= 1000
            end = start * 1000 - 1
            ct += 1

        return commas