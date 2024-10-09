class MinStack:

    def __init__(self):
        self.stack = []
        self.min_list = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_list.append(min(self.min_list[-1],val))

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_list = self.min_list[:-1]
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_list[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
