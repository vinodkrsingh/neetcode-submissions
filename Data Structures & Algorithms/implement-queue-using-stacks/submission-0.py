class MyQueue:

    def __init__(self):
        self.stk1 = []
        self.stk2 = []
        

    def push(self, x: int) -> None:
        self.stk1.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.stk1)-1):
            self.stk2.append(self.stk1.pop())
        value = self.stk1.pop()

        for i in range(len(self.stk2)):
            self.stk1.append(self.stk2.pop())
        return value

    def peek(self) -> int:
        for i in range(len(self.stk1)):
            self.stk2.append(self.stk1.pop())
        value = self.stk2[-1]
        for i in range(len(self.stk2)):
            self.stk1.append(self.stk2.pop())
        return value

    def empty(self) -> bool:
        return False if self.stk1 else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()