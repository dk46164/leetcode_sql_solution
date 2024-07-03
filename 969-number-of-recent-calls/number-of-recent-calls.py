from collections import deque as dq
class RecentCounter:

    def __init__(self):
        # init deque for making faster pop and push operations
        self.call_dq = dq()

    def ping(self, t: int) -> int:
        
        # add call to deque
        self.call_dq.append(t)

        # set the current frame 
        while self.call_dq[0]<max(t-3000,1):
            self.call_dq.popleft()
        
        # return current frame length
        return len(self.call_dq)


        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)