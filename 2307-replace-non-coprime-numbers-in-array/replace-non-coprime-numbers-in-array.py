from typing import List
from math import gcd

class Solution:
    def lcm(self, a, b):
        return a * b // gcd(a, b)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            # merge while top two are not coprime
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                a = stack.pop()
                b = stack.pop()
                stack.append(self.lcm(a, b))
        return stack