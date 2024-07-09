class BrowserHistory:

    def __init__(self, homepage: str):
        # init for the brower history
        self.browser_his = [homepage]
        self.curr_cursor = 0
        

    def visit(self, url: str) -> None:

        # clearup all history
        self.browser_his[self.curr_cursor+1:] = [None]
        

        # append  url  back to browser
        self.browser_his[self.curr_cursor+1] = (url)

        # increase pointer by one
        self.curr_cursor+=1

    def back(self, steps: int) -> str:
        # get lenght of stack
        n = len(self.browser_his)

        # set the cur cursor flag to steps back
        if self.curr_cursor-steps>0:
            self.curr_cursor = self.curr_cursor-steps
        else:
            self.curr_cursor=0
        
        # return homepage back
        return self.browser_his[self.curr_cursor]

    def forward(self, steps: int) -> str:
        # get lenght of stack
        n = len(self.browser_his)
        
        # set the cur cursor flag to steps back
        if self.curr_cursor+steps<n:
            self.curr_cursor = self.curr_cursor+steps
        else:
            self.curr_cursor=n-1
        
        # return homepage back
        return self.browser_his[self.curr_cursor]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)