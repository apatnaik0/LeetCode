class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        st = self.stack

        current_price, price_span = price, 1

        while st and current_price>=st[-1][0]:
            prev_price, prev_span = st.pop()
            price_span += prev_span
        st.append([current_price, price_span])
        return price_span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)