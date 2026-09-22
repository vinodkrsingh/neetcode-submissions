class StockSpanner:

    def __init__(self):
        self.stk = []

    def next(self, price: int) -> int:
        out = 1
        while self.stk and self.stk[-1][0] <= price:
            popVal  = self.stk.pop()
            out += popVal[1]
        self.stk.append((price,out) )
        return out
        

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)