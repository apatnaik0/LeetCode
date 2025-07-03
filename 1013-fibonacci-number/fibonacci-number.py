class Solution:
    def fib(self, n: int) -> int:
        def rec(n):
            if n==0 or n==1:
                return n
            return rec(n-2) + rec(n-1)
        return rec(n)