class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        dup = n
        while dup > 0:
            digit_sum += dup%10
            digit_product *= dup%10
            dup = dup//10
        
        return n % (digit_sum + digit_product) == 0

        