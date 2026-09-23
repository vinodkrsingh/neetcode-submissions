class FreqStack:

    def __init__(self):
        self.freq = {}
        self.feqdct = defaultdict(list)
        self.maxfreq = 0
        

    def push(self, val: int) -> None:
        f = 1 + self.freq.get(val, 0)
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.feqdct[f].append(val)

    def pop(self) -> int:
        x = self.feqdct[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.feqdct[self.maxfreq]:
            self.maxfreq -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()