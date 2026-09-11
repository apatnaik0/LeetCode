class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_ct = [0]*10
        for digit in digits:
            digit_ct[digit] += 1

        ans = 0

        for num in range(100,1000,2):
            a = num //100
            b = (num//10) % 10
            c = num%10

            digit_ct[a] -= 1
            digit_ct[b] -= 1
            digit_ct[c] -= 1

            if digit_ct[a]>=0 and digit_ct[b]>=0 and digit_ct[c]>=0:
                ans += 1

            digit_ct[a] += 1
            digit_ct[b] += 1
            digit_ct[c] += 1
        
        return ans