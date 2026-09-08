class MyStack:

    def __init__(self):
        self.que1 = []

    def push(self, x: int) -> None:
        self.que1.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.que1)-1):
            self.que1.append(self.que1.pop(0))
        return self.que1.pop(0)
        

    def top(self) -> int:
        for i in range(len(self.que1)-1):
            self.que1.append(self.que1.pop(0))
        val = self.que1.pop(0)
        self.que1.append(val)
        return val
        
    def empty(self) -> bool:
        return True if not self.que1 else False
        
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()