class OrderedStream:

    def __init__(self, n: int):
        self.stream_set = [None]*n
        self.size = n
        self.cur_pnt = 0        

    def insert(self, idKey: int, value: str) -> List[str]:
        # insert values in stream
        self.stream_set[idKey-1] = value
        
        if self.cur_pnt<idKey-1:
            return []
        else:
            while self.cur_pnt<len(self.stream_set) and self.stream_set[self.cur_pnt] is not None:
                self.cur_pnt+=1

            return self.stream_set[idKey-1:self.cur_pnt]

       


        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)