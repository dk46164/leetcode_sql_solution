class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(1)
# print(obj.st,obj.minval)
# obj.push(0)
# print(obj.st,obj.minval)
# obj.push(1)
# print(obj.st,obj.minval)
# obj.pop()
# print(obj.st,obj.minval)
# param_5 = obj.getMin()
# param_4 = obj.getMin()
# param_3 = obj.top()
# print(param_3,param_4,param_5)