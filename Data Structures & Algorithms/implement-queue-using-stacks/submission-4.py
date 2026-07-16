class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        for i in range(1,self.size):
            self.stack2.append(self.stack1.pop())
        popped = self.stack1.pop()
        for i in range(1,self.size):
            self.stack1.append(self.stack2.pop())
        self.size -= 1
        return popped
        

    def peek(self) -> int:
        for i in range(1,self.size):
            self.stack2.append(self.stack1.pop())
        peeked = self.stack1[-1]
        for i in range(1,self.size):
            self.stack1.append(self.stack2.pop())
        return peeked
        

    def empty(self) -> bool:
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()