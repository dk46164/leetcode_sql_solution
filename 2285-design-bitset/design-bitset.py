from math import pow
class Bitset:

    def __init__(self, size: int):
        # init
        self.bit_set = [0]*size
        self.bit_flip = [1]*size

        # get max int value
        self.ones_cnt = 0

        # bit size var
        self.n = size
        

    def fix(self, idx: int) -> None:
        # check update the indx
        if not self.bit_set[idx]:
            self.bit_set[idx] = 1
            self.bit_flip[idx] = 0
            self.ones_cnt+=1
        
    def unfix(self, idx: int) -> None:
       # check update the indx
        if self.bit_set[idx]:
            self.bit_set[idx] = 0
            self.bit_flip[idx] = 1
            self.ones_cnt-=1

    def flip(self) -> None:

        # update one cnt
        self.ones_cnt =self.n-self.ones_cnt

        # sswap two list
        self.bit_set,self.bit_flip = self.bit_flip,self.bit_set

        
    def all(self) -> bool:
        # check one cnt var 
        return  self.ones_cnt==self.n
        
    def one(self) -> bool:
        # check if greater than equals to 1 
        return self.ones_cnt>=1

    def count(self) -> int:    
        # count occurence of 1
        return self.ones_cnt 

    def toString(self) -> str:
        # join and return string
        return ''.join(list(map(str,self.bit_set)))
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()