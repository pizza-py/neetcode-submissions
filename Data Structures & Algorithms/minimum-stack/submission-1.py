class MinStack:

    def __init__(self):
        self.elements = []
        self.minimum = []

    def push(self, val: int) -> None:
        if len(self.elements) != 0:
            self.minimum.append(min(val,self.minimum[-1]))
        else:
            self.minimum.append(val)
        self.elements.append(val)

    def pop(self) -> None:
        self.elements.pop()
        self.minimum.pop()

    def top(self) -> int:
        return self.elements[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]

