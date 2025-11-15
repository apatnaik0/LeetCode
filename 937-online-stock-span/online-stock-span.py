class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        cur_price, cur_span = price, 1
        while self.st and cur_price >= self.st[-1][0]:
            prev_price, prev_span = self.st.pop()
            cur_span += prev_span
        self.st.append((cur_price,cur_span))
        return cur_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)