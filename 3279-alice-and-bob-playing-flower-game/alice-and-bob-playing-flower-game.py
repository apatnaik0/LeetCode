class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        on = (n+1)//2
        en = (n)//2
        om = (m+1)//2
        em = (m)//2
        return (on*em) + (en*om)