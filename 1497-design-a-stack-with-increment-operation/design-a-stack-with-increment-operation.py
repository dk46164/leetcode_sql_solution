class CustomStack:

    def __init__(self, maxSize: int):

        # init stack with empty
        self.stack = []
        # after each insert/delete update cur  size counter
        self.cur_size = -1
        self.max_size = maxSize-1
        

    def push(self, x: int) -> None:
        # check inf x<maxsize, then only insert else skip
        if self.cur_size<self.max_size:
            self.stack.append(x)
            self.cur_size+=1

    def pop(self) -> int:
        # tmp val 
        tmp_val = -1

        # check inf x<maxsize, then only pop else skip
        if self.cur_size>=0:
            tmp_val  = self.stack.pop(-1)
            self.cur_size-=1

        
        return tmp_val
        

    def increment(self, k: int, val: int) -> None:
        #  check if self.cur_size >k 
        if k>self.cur_size:
            max_idx = k
        else:
            max_idx = self.cur_size
            
        # update  k elements by val
        self.stack[:k] = list(map(lambda key:key+val ,self.stack[:k]))
        
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)