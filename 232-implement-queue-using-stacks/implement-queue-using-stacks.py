class MyQueue:

    def __init__(self):
        self.arr = []
        self.pop_idx = 0
        self.push_idx = 0
        

    def push(self, x: int) -> None:
        self.arr.append(x)
        self.push_idx+=1
        

    def pop(self) -> int:
        val  = self.arr[self.pop_idx]
        self.pop_idx+=1
        return val

    def peek(self) -> int:
        return self.arr[self.pop_idx]

    def empty(self) -> bool:
        return False if self.pop_idx-self.push_idx else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()