class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]

    def visit(self, url: str) -> None:
        self.stack.append(url)
        if self.stack:
            self.idx = enumerate(self.stack[-1])


    def back(self, steps: int) -> str:
        if not self.stack:
            return None
        N = len(self.stack) - 1
        if steps < self.idx:
            self.cur = self.stack[self.idx - steps]
            return self.cur
        else:
            return self.stack[0] 


    def forward(self, steps: int) -> str:
        if not self.stack:
            return None
        N = len(self.stack) - 1
        if self.idx + steps < len(self.stack):
            self.cur = self.stack[self.idx + steps]
            return self.cur
        else:
            return self.stack[-1] 



# Your BrowserHistory object will be instantiated and called as such:
["BrowserHistory","back","visit","back","visit","visit","back","visit","visit","back","visit","visit","forward","visit","forward","forward","visit","forward","forward"]
obj = BrowserHistory('a')
obj.visit('b')
print(obj.stack)