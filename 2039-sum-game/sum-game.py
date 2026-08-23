class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        l = 0
        r = n-1
        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0
        while l < r:
            if num[l] == '?':
                left_q += 1
            else:
                left_sum += int(num[l])
            if num[r] == '?':
                right_q += 1
            else:
                right_sum += int(num[r])
            l += 1
            r -= 1
        
        d = left_sum - right_sum
        q = left_q - right_q

        if q%2 == 1:
            return True
        
        return 2*d != -9*q
            